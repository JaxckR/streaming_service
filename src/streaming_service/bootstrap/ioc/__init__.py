__all__ = ["container", "PROVIDERS"]

from typing import Final

from dishka import make_async_container, Provider
from dishka.integrations.fastapi import FastapiProvider

from streaming_service.bootstrap.config import (
    PostgresConfig,
    config,
    RabbitConfig,
    JWTConfig,
)
from streaming_service.bootstrap.ioc.application import ApplicationProvider
from streaming_service.bootstrap.ioc.context import ContextProvider
from streaming_service.bootstrap.ioc.database import DatabaseProvider
from streaming_service.bootstrap.ioc.infrastructure import InfrastructureProvider
from streaming_service.bootstrap.ioc.presentation import PresentationProvider

PROVIDERS: Final[list[Provider]] = [
    ContextProvider(),
    ApplicationProvider(),
    DatabaseProvider(),
    InfrastructureProvider(),
    PresentationProvider(),
    FastapiProvider(),
]

container = make_async_container(
    *PROVIDERS,
    context={
        PostgresConfig: config.postgres,
        RabbitConfig: config.rabbit,
        JWTConfig: config.jwt,
    },
)
