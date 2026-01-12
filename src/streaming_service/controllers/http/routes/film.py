from typing import Annotated

from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter, Path

from streaming_service.application.handlers.film import (
    CreateFilmRequest,
    DeleteFilmHandler,
    GetFilmHandler,
    GetAllFilmsHandler,
)
from streaming_service.application.ports import Publisher
from streaming_service.entities.film import FilmId

film_router = APIRouter(prefix="/films", tags=["films"], route_class=DishkaRoute)


@film_router.get("/")
async def get_all(handler: FromDishka[GetAllFilmsHandler]):
    return await handler.handle()


@film_router.post("/")
async def create_film(request: CreateFilmRequest, publisher: FromDishka[Publisher]):
    await publisher.publish(queue="create_film", message=request)


@film_router.delete("/{id}")
async def delete_film(
    film_id: Annotated[FilmId, Path(alias="id")], handler: FromDishka[DeleteFilmHandler]
):
    await handler.handle(film_id)


@film_router.get("/{id}")
async def get_film(
    film_id: Annotated[FilmId, Path(alias="id")], handler: FromDishka[GetFilmHandler]
):
    return await handler.handle(film_id)
