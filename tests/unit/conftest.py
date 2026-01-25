from datetime import datetime
from typing import AsyncIterable
from unittest.mock import AsyncMock, Mock
from uuid import UUID

import pytest
from dishka import AsyncContainer, Provider, provide, Scope, AnyOf, make_async_container
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.requests import Request

from streaming_service.application.ports import TransactionManager, RequestManager
from streaming_service.application.ports.repositories import (
    UserRepository,
    FilmRepository,
)
from streaming_service.bootstrap.config import (
    PostgresConfig,
    config,
    RabbitConfig,
    JWTConfig,
)
from streaming_service.bootstrap.ioc import PROVIDERS
from streaming_service.entities.film import Film, FilmId
from streaming_service.entities.genre import Genre, GenreId
from streaming_service.entities.user import User
from streaming_service.infrastructure.persistence.tables import setup_tables


class MockProvider(Provider):
    scope = Scope.REQUEST

    @provide
    def user(self) -> User:
        """
        Password is "qwerty12345"
        """
        return User(
            id="06967909-03d2-70f2-8000-62ca51b0f29d",
            username="testUsername",
            password="$2b$12$4z0aTfiHbc4tLK575dJsZ.v/Yc6aTYysbj4nn7YPlhcil2a.ajYsS",
            email="test@gmail.com",
            created_at=datetime(year=2026, month=1, day=1, hour=0, minute=0, second=0),
            updated_at=None,
            deleted_at=None,
        )

    @provide
    def film(self) -> Film:
        created_at = datetime(year=2026, month=1, day=1)
        return Film(
            id=FilmId(UUID("0696424f-090b-720a-8000-80d6a0f0733d")),
            title="Garry Potter",
            description="Magic world!",
            rating=89,
            country="UK",
            release_date=datetime(year=2025, month=1, day=1),
            genres=[
                Genre(
                    id=GenreId(1),
                    name="Adventure",
                    created_at=created_at,
                    updated_at=None,
                ),
                Genre(
                    id=GenreId(2), name="Drama", created_at=created_at, updated_at=None
                ),
            ],
            created_at=created_at,
            updated_at=None,
            deleted_at=None,
        )

    @provide(override=True)
    def transaction_manager(self) -> AnyOf[TransactionManager, AsyncSession]:
        tm = AsyncMock()
        tm.add = Mock()
        return tm

    @provide(override=True)
    def request(self) -> Request:
        return Mock()

    @provide(override=True)
    def user_repository(self, user: User) -> UserRepository:
        repository = AsyncMock()
        repository.add = Mock()
        repository.get_by_username = AsyncMock(return_value=user)
        return repository

    @provide(override=True)
    def film_repository(self, film: Film) -> FilmRepository:
        repository = AsyncMock()
        repository.add = Mock()
        repository.get = AsyncMock(return_value=film)
        return repository

    @provide(override=True)
    def request_manager(self) -> RequestManager:
        return Mock()


@pytest.fixture
async def container() -> AsyncIterable[AsyncContainer]:
    container = make_async_container(
        *PROVIDERS,
        MockProvider(),
        context={
            PostgresConfig: config.postgres,
            RabbitConfig: config.rabbit,
            JWTConfig: config.jwt,
        },
    )

    async with container() as c:
        yield c


@pytest.fixture(scope="session", autouse=True)
def setup() -> None:
    setup_tables()
