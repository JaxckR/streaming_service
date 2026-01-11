from dishka import Provider, Scope, provide_all, WithParents

from streaming_service.infrastructure.persistence.adapters.film import (
    FilmRepositoryImpl,
)
from streaming_service.infrastructure.persistence.adapters.genre import (
    GenreRepositoryImpl,
)


class InfrastructureProvider(Provider):
    scope = Scope.REQUEST

    repositories = provide_all(
        WithParents[GenreRepositoryImpl], WithParents[FilmRepositoryImpl]
    )
