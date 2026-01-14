from abc import abstractmethod
from typing import Protocol

from streaming_service.entities.film import FilmId
from streaming_service.entities.user import UserId


class IdGenerator(Protocol):
    @abstractmethod
    def film_id(self) -> FilmId: ...

    @abstractmethod
    def user_id(self) -> UserId: ...
