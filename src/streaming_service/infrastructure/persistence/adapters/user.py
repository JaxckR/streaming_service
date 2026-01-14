from sqlalchemy import select, and_

from streaming_service.application.ports.repositories import UserRepository
from streaming_service.entities.user import User
from streaming_service.infrastructure.persistence.adapters.mixins import SQLAMixin


class UserRepositoryImpl(SQLAMixin, UserRepository):
    def add(self, instance: User) -> None:
        self._session.add(instance)

    async def get(self, user_id: int) -> User | None:
        query = await self._session.execute(
            select(User).where(and_(User.id == user_id))
        )
        return query.scalar_one_or_none()

    async def get_by_username(self, username: str) -> User | None:
        query = await self._session.execute(
            select(User).where(and_(User.username == username))
        )
        return query.scalar_one_or_none()
