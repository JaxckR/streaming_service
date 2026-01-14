from dataclasses import dataclass

from streaming_service.application.factories.user import UserFactory
from streaming_service.application.ports import TransactionManager
from streaming_service.application.ports.repositories import UserRepository


@dataclass(slots=True, frozen=True)
class SignUpRequest:
    username: str
    password: str
    email: str


class SignUpHandler:
    def __init__(
        self,
        user_factory: UserFactory,
        user_repository: UserRepository,
        transaction_manager: TransactionManager,
    ) -> None:
        self._user_factory = user_factory
        self._user_repository = user_repository
        self._transaction_manager = transaction_manager

    async def handle(self, request: SignUpRequest) -> None:
        user = self._user_factory.create(
            username=request.username,
            password=request.password,
            email=request.email,
        )
        self._user_repository.add(user)
        await self._transaction_manager.commit()
