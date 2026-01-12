from streaming_service.application.ports import TransactionManager
from streaming_service.application.ports.repositories import FilmRepository
from streaming_service.entities.film import FilmId


class DeleteFilmHandler:
    def __init__(
        self, film_repository: FilmRepository, transaction_manager: TransactionManager
    ) -> None:
        self._film_repository = film_repository
        self._transaction_manager = transaction_manager

    async def handle(self, film_id: FilmId) -> None:
        await self._film_repository.delete(film_id)
        await self._transaction_manager.commit()
