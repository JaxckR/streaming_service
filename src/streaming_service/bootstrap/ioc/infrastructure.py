from dishka import Provider, Scope, provide_all, WithParents

from streaming_service.infrastructure.adapters.id_generator import IdGeneratorImpl
from streaming_service.infrastructure.persistence.adapters.film import (
    FilmRepositoryImpl,
)
from streaming_service.infrastructure.persistence.adapters.genre import (
    GenreRepositoryImpl,
)


class InfrastructureProvider(Provider):
    scope = Scope.REQUEST

    adapters_app = provide_all(WithParents[IdGeneratorImpl])

    repositories = provide_all(
        WithParents[GenreRepositoryImpl], WithParents[FilmRepositoryImpl]
    )
