from streaming_service.application.ports import RequestManager


class LogoutHandler:
    def __init__(self, request_manager: RequestManager) -> None:
        self._request_manager = request_manager

    async def handle(self) -> None:
        self._request_manager.remove("refresh")
        self._request_manager.remove("access")
