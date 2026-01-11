import asyncio
import sys

import uvicorn
from dishka import make_async_container
from dishka.integrations.fastapi import setup_dishka as fastapi_setup_dishka
from dishka.integrations.faststream import setup_dishka as faststream_setup_dishka
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from faststream import FastStream

from streaming_service.bootstrap.config import PostgresConfig, config
from streaming_service.bootstrap.ioc import get_providers
from streaming_service.controllers.http.routes import setup_routes
from streaming_service.controllers.middlewares import setup_middlewares
from streaming_service.infrastructure.adapters.broker_provider import get_broker
from streaming_service.infrastructure.persistence.tables import setup_tables

container = make_async_container(
    *get_providers(), context={PostgresConfig: config.postgres}
)


def faststream_app() -> FastStream:
    broker = get_broker(config.rabbit)
    app = FastStream(broker)
    faststream_setup_dishka(container, app, auto_inject=True)

    return app


def fastapi_app() -> FastAPI:
    app = FastAPI(
        title="FastAPI",
        description="Streaming service",
        version="1.0.0",
        default_response_class=ORJSONResponse,
    )
    fastapi_setup_dishka(container, app)
    setup_routes(app)
    setup_middlewares(app)
    setup_tables()
    return app


def get_app() -> FastAPI:
    fastapi = fastapi_app()
    faststream = faststream_app()

    fastapi.add_event_handler("startup", faststream.broker.start)
    fastapi.add_event_handler("shutdown", faststream.broker.stop)
    fastapi.add_event_handler("shutdown", fastapi.state.dishka_container.close)

    return fastapi


if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

if __name__ == "__main__":
    uvicorn.run("main:get_app", host="0.0.0.0", port=8000, loop="none", factory=True)
