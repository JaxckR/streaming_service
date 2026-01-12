from abc import abstractmethod
from typing import Protocol, Any


class Publisher(Protocol):
    @abstractmethod
    async def publish(self, queue: str, message: Any) -> None: ...
