from abc import abstractmethod
from typing import Protocol

from streaming_service.entities.genre import Genre


class GenreRepository(Protocol):
    @abstractmethod
    async def get_all(self) -> list[Genre]: ...

    @abstractmethod
    def add(self, instance: Genre) -> None: ...
