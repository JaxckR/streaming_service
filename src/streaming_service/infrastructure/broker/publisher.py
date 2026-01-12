from typing import Any

from faststream.rabbit import RabbitBroker

from streaming_service.application.ports import Publisher


class RabbitPublisher(Publisher):
    def __init__(self, broker: RabbitBroker) -> None:
        self._broker = broker

    async def publish(self, queue: str, message: Any) -> None:
        await self._broker.publish(message, queue)
