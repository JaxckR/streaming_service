from abc import abstractmethod
from typing import Protocol

from streaming_service.entities.film import FilmId


class IdGenerator(Protocol):
    @abstractmethod
    def film_id(self) -> FilmId: ...
