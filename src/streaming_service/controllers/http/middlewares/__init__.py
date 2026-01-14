__all__ = ["setup_middlewares"]

from typing import Final

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from streaming_service.controllers.http.middlewares.auth import ASGIAuthMiddleware
from streaming_service.controllers.http.middlewares.metrics import MetricsMiddleware

MIDDLEWARES: Final[list] = [MetricsMiddleware, ASGIAuthMiddleware]


def setup_middlewares(app: FastAPI) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
        allow_credentials=True,
    )
    for middleware in MIDDLEWARES:
        app.add_middleware(middleware)
