from datetime import datetime
from uuid import UUID

import pytest
from dishka import AsyncContainer

from streaming_service.application.handlers.film import (
    CreateFilmHandler,
    CreateFilmRequest,
    DeleteFilmHandler,
    GetFilmHandler,
)
from streaming_service.entities.film import FilmId, Film
from streaming_service.entities.genre import GenreId


@pytest.mark.parametrize(
    ("title", "description", "genres", "country", "release_date", "rating", "exc"),
    [
        (
            "Garry Potter",
            "Magic world",
            [GenreId(1)],
            "UK",
            datetime(year=2020, month=1, day=1),
            89,
            None,
        ),
    ],
)
async def test_create(
    title: str,
    description: str,
    genres: list[GenreId],
    country: str,
    release_date: datetime,
    rating: int,
    exc: type[Exception] | None,
    container: AsyncContainer,
) -> None:
    handler = await container.get(CreateFilmHandler)
    transaction_manager = handler._transaction_manager

    if exc is not None:
        with pytest.raises(exc):
            await handler.handle(
                CreateFilmRequest(
                    title=title,
                    description=description,
                    genres=genres,
                    country=country,
                    release_date=release_date,
                    rating=rating,
                )
            )
    else:
        await handler.handle(
            CreateFilmRequest(
                title=title,
                description=description,
                genres=genres,
                country=country,
                release_date=release_date,
                rating=rating,
            )
        )
        transaction_manager.commit.assert_called()


async def test_delete(container: AsyncContainer) -> None:
    handler = await container.get(DeleteFilmHandler)

    await handler.handle(FilmId(UUID("0696424f-090b-720a-8000-80d6a0f0733d")))


async def test_get(container: AsyncContainer) -> None:
    handler = await container.get(GetFilmHandler)
    film = await container.get(Film)

    result = await handler.handle(film.id)
    assert result.id == film.id
    assert result.title == film.title
    assert result.description == film.description
    assert result.genres == film.genres
    assert result.release_date == film.release_date
    assert result.rating == film.rating
    assert result.created_at == film.created_at
    assert result.updated_at == film.updated_at
    assert result.deleted_at == film.deleted_at
