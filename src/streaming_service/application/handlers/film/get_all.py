from streaming_service.application.ports.repositories.film import FilmRepository
from streaming_service.entities.film import Film


class GetAllFilmsHandler:
    def __init__(self, film_repository: FilmRepository) -> None:
        self._film_repository = film_repository

    async def handle(self) -> list[Film]:
        return await self._film_repository.get_all()
