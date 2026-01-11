from sqlalchemy import delete, and_, select

from streaming_service.application.ports.repositories.film import FilmRepository
from streaming_service.entities.film import FilmId, Film
from streaming_service.infrastructure.persistence.adapters.mixins import SQLAMixin


class FilmRepositoryImpl(SQLAMixin, FilmRepository):
    async def get(self, film_id: FilmId) -> Film | None:
        query = await self._session.execute(
            select(Film).where(and_(Film.id == film_id))
        )
        return query.scalar_one_or_none()

    async def get_all(self) -> list[Film]:
        query = await self._session.execute(select(Film))
        return list(query.scalars().all())

    async def delete(self, film_id: FilmId) -> None:
        await self._session.execute(delete(Film).where(and_(Film.id == film_id)))

    def add(self, instance: Film) -> None:
        self._session.add(instance)
