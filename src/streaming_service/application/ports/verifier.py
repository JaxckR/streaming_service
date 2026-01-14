from abc import abstractmethod
from typing import Protocol


class Verifier(Protocol):
    @abstractmethod
    def verify_password(self, password: str, hashed_password: str) -> bool: ...
