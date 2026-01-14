from abc import abstractmethod
from typing import Protocol

from streaming_service.entities.user import User


class UserRepository(Protocol):
    @abstractmethod
    def add(self, instance: User) -> None: ...

    @abstractmethod
    async def get(self, user_id: int) -> User | None: ...

    @abstractmethod
    async def get_by_username(self, username: str) -> User | None: ...
