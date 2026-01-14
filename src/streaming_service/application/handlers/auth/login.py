from dataclasses import dataclass

from streaming_service.application.exceptions import UnauthorizedError
from streaming_service.application.ports import Verifier, RequestManager, AuthPayload
from streaming_service.application.ports.repositories import UserRepository


@dataclass(slots=True, frozen=True)
class LoginRequest:
    username: str
    password: str


class LoginHandler:
    def __init__(
        self,
        verifier: Verifier,
        user_repository: UserRepository,
        request_manager: RequestManager,
    ) -> None:
        self._verifier = verifier
        self._user_repository = user_repository
        self._request_manager = request_manager

    async def handle(self, request: LoginRequest) -> None:
        user = await self._user_repository.get_by_username(request.username)

        if not user:
            raise UnauthorizedError("Invalid username or password")

        is_verify = self._verifier.verify_password(request.password, user.password)

        if not is_verify:
            raise UnauthorizedError("Invalid username or password")

        payload = AuthPayload(user.id)
        self._request_manager.set_access(payload)
        self._request_manager.set_refresh(payload)
