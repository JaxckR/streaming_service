from faststream.rabbit import RabbitBroker
from faststream.security import SASLPlaintext

from streaming_service.bootstrap.config import RabbitConfig


def get_broker(config: RabbitConfig) -> RabbitBroker:
    return RabbitBroker(
        host=config.host,
        port=config.port,
        security=SASLPlaintext(
            username=config.username,
            password=config.password,
        ),
        virtualhost="/",
    )
