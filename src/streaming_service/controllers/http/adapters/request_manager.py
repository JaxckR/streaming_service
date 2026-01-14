from uuid import uuid4

from starlette.requests import Request

from streaming_service.application.ports import (
    RequestManager,
    Token,
    AuthPayloadCodec,
    AuthPayload,
)
from streaming_service.application.ports.request_manager import Name
from streaming_service.bootstrap.config import JWTConfig


class CookieRequestManager(RequestManager):
    def __init__(
        self, request: Request, auth_codec: AuthPayloadCodec, config: JWTConfig
    ) -> None:
        self._request = request
        self._auth_codec = auth_codec
        self._config = config

    def set_refresh(self, payload: AuthPayload) -> None:
        value = str(self._auth_codec.encode(payload, token_type="refresh"))
        max_age = 60 * 60 * 24 * self._config.refresh_days_expires
        self.set(Token(name="refresh", value=value, max_age=max_age, secure=True))

    def set_access(self, payload: AuthPayload) -> None:
        value = str(self._auth_codec.encode(payload, token_type="access"))
        max_age = 60 * 60 * self._config.access_minutes_expires
        self.set(Token(name="access", value=value, max_age=max_age, secure=True))

    def set(self, token: Token) -> None:
        setattr(self._request.state, f"set_cookie_{uuid4().hex}", token)

    def get(self, name: Name) -> str:
        return self._request.cookies.get(name)

    def remove(self, name: Name) -> None:
        setattr(self._request.state, f"remove_cookie__{uuid4().hex}", name)
