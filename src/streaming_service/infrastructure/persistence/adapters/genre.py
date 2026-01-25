from sqlalchemy import select, and_
from sqlalchemy.sql.operators import in_op

from streaming_service.application.ports.repositories.genre import GenreRepository
from streaming_service.entities.genre import Genre, GenreId
from streaming_service.infrastructure.persistence.adapters.mixins import SQLAMixin


class GenreRepositoryImpl(SQLAMixin, GenreRepository):
    async def get_many(self, ids: list[GenreId]) -> list[Genre]:
        query = await self._session.execute(
            select(Genre).where(and_(in_op(Genre.id, ids)))
        )
        return list(query.scalars().all())

    async def get_all(self) -> list[Genre]:
        query = await self._session.execute(select(Genre))
        return list(query.scalars().all())

    async def get(self, genre_id: GenreId) -> Genre | None:
        query = await self._session.execute(
            select(Genre).where(and_(Genre.id == genre_id))
        )
        return query.scalar_one_or_none()

    def add(self, instance: Genre) -> None:
        self._session.add(instance)
