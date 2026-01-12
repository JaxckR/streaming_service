from datetime import datetime
from typing import cast

from streaming_service.application.ports import TransactionManager
from streaming_service.application.ports.repositories.genre import GenreRepository
from streaming_service.entities.genre import Genre


class CreateGenreHandler:
    def __init__(
        self, genre_repository: GenreRepository, transaction_manager: TransactionManager
    ) -> None:
        self._genre_repository = genre_repository
        self._transaction_manager = transaction_manager

    async def handle(self, name: str) -> None:
        genre = Genre(
            id=cast(int, None),
            name=name,
            created_at=cast(datetime, None),
            updated_at=None,
        )

        self._genre_repository.add(genre)
        await self._transaction_manager.commit()
