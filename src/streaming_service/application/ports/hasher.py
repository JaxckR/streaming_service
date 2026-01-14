from abc import abstractmethod
from typing import Protocol


class Hasher(Protocol):
    @abstractmethod
    def hash_password(self, password: str) -> str: ...
