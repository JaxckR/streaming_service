from abc import abstractmethod
from typing import Protocol

from streaming_service.entities.film import Film, FilmId


class FilmRepository(Protocol):
    @abstractmethod
    async def get(self, film_id: FilmId) -> Film | None: ...

    @abstractmethod
    async def get_all(self) -> list[Film]: ...

    @abstractmethod
    async def delete(self, film_id: FilmId) -> None: ...

    @abstractmethod
    def add(self, instance: Film) -> None: ...
