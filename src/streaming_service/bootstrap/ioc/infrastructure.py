from typing import AsyncIterator

from dishka import Provider, Scope, provide_all, WithParents, provide
from faststream.rabbit import RabbitBroker

from streaming_service.bootstrap.config import RabbitConfig
from streaming_service.infrastructure.adapters import IdGeneratorImpl
from streaming_service.infrastructure.broker import RabbitPublisher, get_broker
from streaming_service.infrastructure.persistence.adapters import (
    FilmRepositoryImpl,
    GenreRepositoryImpl,
)


class InfrastructureProvider(Provider):
    scope = Scope.REQUEST

    @provide(scope=Scope.APP)
    async def broker(self, config: RabbitConfig) -> AsyncIterator[RabbitBroker]:
        async with get_broker(config) as broker:
            yield broker

    adapters_app = provide_all(WithParents[IdGeneratorImpl])

    repositories = provide_all(
        WithParents[GenreRepositoryImpl],
        WithParents[FilmRepositoryImpl],
        WithParents[RabbitPublisher],
    )
