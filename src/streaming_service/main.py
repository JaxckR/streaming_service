import asyncio
import sys

import uvicorn
from dishka.integrations.fastapi import setup_dishka as fastapi_setup_dishka
from dishka.integrations.faststream import setup_dishka as faststream_setup_dishka
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from faststream import FastStream

from streaming_service.bootstrap.config import config
from streaming_service.bootstrap.ioc import container
from streaming_service.bootstrap.logging import setup_logging
from streaming_service.controllers.amqp import ROUTERS
from streaming_service.controllers.http import (
    setup_exceptions,
    setup_routes,
    setup_middlewares,
)
from streaming_service.infrastructure.broker import get_broker
from streaming_service.infrastructure.persistence.tables import setup_tables


def faststream_app() -> FastStream:
    broker = get_broker(config.rabbit)
    app = FastStream(broker)
    setup_logging()

    setup_tables()
    faststream_setup_dishka(container, app, auto_inject=True)
    broker.include_routers(*ROUTERS)

    return app


def fastapi_app() -> FastAPI:
    app = FastAPI(
        title="FastAPI",
        description="Streaming service",
        version="1.0.0",
        default_response_class=ORJSONResponse,
    )
    setup_logging()
    fastapi_setup_dishka(container, app)
    setup_routes(app)
    setup_middlewares(app)
    setup_tables()
    setup_exceptions(app)
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
    uvicorn.run(
        "main:get_app",
        host="0.0.0.0",
        port=8000,
        loop="none",
        factory=True,
        log_config=None,
    )
