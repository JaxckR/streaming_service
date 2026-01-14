from abc import abstractmethod
from dataclasses import dataclass
from typing import Protocol, TypeAlias, Literal

from streaming_service.application.ports import AuthPayload

Name: TypeAlias = str | Literal["refresh", "access"]


@dataclass(slots=True, frozen=True)
class Token:
    name: Name
    value: str
    max_age: int
    secure: bool


class RequestManager(Protocol):
    @abstractmethod
    def set_refresh(self, payload: AuthPayload) -> None: ...

    @abstractmethod
    def set_access(self, payload: AuthPayload) -> None: ...

    @abstractmethod
    def set(self, token: Token) -> None: ...

    @abstractmethod
    def get(self, name: Name) -> str: ...

    @abstractmethod
    def remove(self, name: Name) -> None: ...
