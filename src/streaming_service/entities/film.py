from dataclasses import dataclass
from datetime import datetime
from typing import NewType
from uuid import UUID

from streaming_service.entities.common import IdEntity
from streaming_service.entities.genre import Genre, GenreId

FilmId = NewType("FilmId", UUID)
FilmGenreId = NewType("FilmGenreId", int)


@dataclass
class Film(IdEntity[FilmId]):
    title: str
    description: str
    rating: int
    genres: list[Genre]
    country: str
    release_date: datetime

    created_at: datetime
    updated_at: datetime | None
    deleted_at: datetime | None

    def __post_init__(self) -> None:
        if self.rating > 100:
            self.rating = 100


@dataclass
class FilmGenre(IdEntity[FilmGenreId]):
    film_id: FilmId
    genre_id: GenreId
