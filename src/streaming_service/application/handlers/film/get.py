from streaming_service.application.exceptions import NotFoundError
from streaming_service.application.ports.repositories import FilmRepository
from streaming_service.entities.film import FilmId, Film


class GetFilmHandler:
    def __init__(self, film_repository: FilmRepository) -> None:
        self._film_repository = film_repository

    async def handle(self, film_id: FilmId) -> Film | None:
        film = await self._film_repository.get(film_id)

        if not film:
            raise NotFoundError("")

        return film
