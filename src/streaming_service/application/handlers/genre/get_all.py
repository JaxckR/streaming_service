from streaming_service.application.ports.repositories import GenreRepository
from streaming_service.entities.genre import Genre


class GetAllGenresHandler:
    def __init__(self, genre_repository: GenreRepository) -> None:
        self._genre_repository = genre_repository

    async def handle(self) -> list[Genre]:
        return await self._genre_repository.get_all()
