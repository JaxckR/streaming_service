__all__ = ["setup_middlewares"]

from typing import Final

from fastapi import FastAPI

from streaming_service.controllers.middlewares.metrics import MetricsMiddleware

MIDDLEWARES: Final[list] = [MetricsMiddleware]


def setup_middlewares(app: FastAPI) -> None:
    for middleware in MIDDLEWARES:
        app.add_middleware(middleware)
