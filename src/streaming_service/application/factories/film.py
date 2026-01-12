from datetime import datetime
from typing import cast

from streaming_service.application.ports.id_generator import IdGenerator
from streaming_service.entities.film import Film
from streaming_service.entities.genre import Genre


class FilmFactory:
    def __init__(self, id_generator: IdGenerator) -> None:
        self._id_generator = id_generator

    def create(
        self,
        title: str,
        description: str,
        genres: list[Genre],
        country: str,
        release_date: datetime,
        rating: int | None = None,
    ) -> Film:
        return Film(
            id=self._id_generator.film_id(),
            title=title,
            description=description,
            genres=genres,
            country=country,
            release_date=release_date,
            rating=rating or 0,
            created_at=cast(datetime, None),
            updated_at=None,
            deleted_at=None,
        )
