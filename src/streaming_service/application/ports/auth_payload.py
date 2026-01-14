from abc import abstractmethod
from dataclasses import dataclass
from typing import Protocol, Literal

from streaming_service.entities.user import UserId


@dataclass(slots=True, frozen=True)
class AuthPayload:
    user_id: UserId


class AuthPayloadCodec(Protocol):
    @abstractmethod
    def decode(self, token: str | bytes) -> dict: ...

    @abstractmethod
    def encode(
        self, payload: AuthPayload, token_type: Literal["access", "refresh"]
    ) -> bytes: ...
