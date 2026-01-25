from dataclasses import dataclass
from datetime import datetime

from streaming_service.application.factories import FilmFactory
from streaming_service.application.ports import TransactionManager
from streaming_service.application.ports.repositories import (
    FilmRepository,
    GenreRepository,
)
from streaming_service.entities.genre import GenreId


@dataclass(frozen=True, slots=True)
class CreateFilmRequest:
    title: str
    description: str
    genres: list[GenreId]
    country: str
    release_date: datetime
    rating: int | None = None


class CreateFilmHandler:
    def __init__(
        self,
        film_factory: FilmFactory,
        film_repository: FilmRepository,
        transaction_manager: TransactionManager,
        genre_repository: GenreRepository,
    ) -> None:
        self._film_repository = film_repository
        self._film_factory = film_factory
        self._transaction_manager = transaction_manager
        self._genre_repository = genre_repository

    async def handle(self, request: CreateFilmRequest) -> None:
        genres = await self._genre_repository.get_many(request.genres)

        film = self._film_factory.create(
            title=request.title,
            description=request.description,
            genres=genres,
            country=request.country,
            release_date=request.release_date,
            rating=request.rating,
        )
        self._film_repository.add(film)
        await self._transaction_manager.commit()
