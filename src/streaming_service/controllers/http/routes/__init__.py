__all__ = ["setup_routes"]

from typing import Final

from fastapi import FastAPI, APIRouter

from streaming_service.controllers.http.routes.auth import auth_router
from streaming_service.controllers.http.routes.film import film_router
from streaming_service.controllers.http.routes.genre import genre_router
from streaming_service.controllers.http.routes.healthcheck import healthcheck_router
from streaming_service.controllers.http.routes.index import index_router

ROUTERS: Final[list[APIRouter]] = [
    healthcheck_router,
    index_router,
    genre_router,
    film_router,
    auth_router,
]


def setup_routes(app: FastAPI) -> None:
    for router in ROUTERS:
        app.include_router(router)
