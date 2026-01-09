__all__ = ["get_providers"]

from dishka import Provider

from streaming_service.bootstrap.ioc.context import ContextProvider
from streaming_service.bootstrap.ioc.database import DatabaseProvider


def get_providers() -> list[Provider]:
    return [ContextProvider(), DatabaseProvider()]
