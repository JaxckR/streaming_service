from dishka import FromDishka
from faststream.rabbit import RabbitRouter

from streaming_service.application.handlers.film import (
    CreateFilmRequest,
    CreateFilmHandler,
)

index_router = RabbitRouter()


@index_router.subscriber("create_film")
async def create_film(
    request: CreateFilmRequest, handler: FromDishka[CreateFilmHandler]
) -> None:
    await handler.handle(request)
