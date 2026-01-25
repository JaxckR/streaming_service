from abc import abstractmethod
from typing import Protocol

from streaming_service.entities.genre import Genre, GenreId


class GenreRepository(Protocol):
    @abstractmethod
    async def get_many(self, ids: list[GenreId]) -> list[Genre]: ...

    @abstractmethod
    async def get_all(self) -> list[Genre]: ...

    @abstractmethod
    async def get(self, genre_id: GenreId) -> Genre | None: ...

    @abstractmethod
    def add(self, instance: Genre) -> None: ...
