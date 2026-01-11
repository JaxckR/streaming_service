from sqlalchemy import select

from streaming_service.application.ports.repositories.genre import GenreRepository
from streaming_service.entities.genre import Genre
from streaming_service.infrastructure.persistence.adapters.mixins import SQLAMixin


class GenreRepositoryImpl(SQLAMixin, GenreRepository):
    async def get_all(self) -> list[Genre]:
        query = await self._session.execute(select(Genre))
        return list(query.scalars().all())

    def add(self, instance: Genre) -> None:
        self._session.add(instance)
