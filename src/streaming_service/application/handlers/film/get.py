from streaming_service.application.ports.repositories.film import FilmRepository
from streaming_service.entities.film import FilmId


class GetFilmHandler:
    def __init__(self, film_repository: FilmRepository) -> None:
        self._film_repository = film_repository

    async def handle(self, film_id: FilmId) -> None:
        return await self._film_repository.get(film_id)
