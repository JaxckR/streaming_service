__all__ = ["get_providers"]

from dishka import Provider

from streaming_service.bootstrap.ioc.context import ContextProvider
from streaming_service.bootstrap.ioc.database import DatabaseProvider
from streaming_service.bootstrap.ioc.infrastructure import InfrastructureProvider


def get_providers() -> list[Provider]:
    return [ContextProvider(), DatabaseProvider(), InfrastructureProvider()]
