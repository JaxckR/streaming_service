from typing import Annotated

from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter, Body

from streaming_service.application.handlers.genre import (
    CreateGenreHandler,
    GetAllGenresHandler,
)

genre_router = APIRouter(prefix="/genres", tags=["genre"], route_class=DishkaRoute)


@genre_router.get("/")
async def get_genre(handler: FromDishka[GetAllGenresHandler]):
    return await handler.handle()


@genre_router.post("/")
async def create_genre(
    name: Annotated[str, Body()], handler: FromDishka[CreateGenreHandler]
):
    await handler.handle(name)
