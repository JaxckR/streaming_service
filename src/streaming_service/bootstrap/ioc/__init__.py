__all__ = ["container"]

from dishka import make_async_container

from streaming_service.bootstrap.config import PostgresConfig, config, RabbitConfig
from streaming_service.bootstrap.ioc.application import ApplicationProvider
from streaming_service.bootstrap.ioc.context import ContextProvider
from streaming_service.bootstrap.ioc.database import DatabaseProvider
from streaming_service.bootstrap.ioc.infrastructure import InfrastructureProvider

container = make_async_container(
    *[
        ContextProvider(),
        ApplicationProvider(),
        DatabaseProvider(),
        InfrastructureProvider(),
    ],
    context={
        PostgresConfig: config.postgres,
        RabbitConfig: config.rabbit,
    },
)
