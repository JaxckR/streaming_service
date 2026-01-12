__all__ = ["ROUTERS"]

from typing import Final

from streaming_service.controllers.amqp.index import index_router

ROUTERS: Final[list] = [index_router]
