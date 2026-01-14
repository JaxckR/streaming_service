from datetime import datetime, timezone, timedelta
from typing import Literal

import jwt

from streaming_service.application.ports import AuthPayloadCodec, AuthPayload
from streaming_service.bootstrap.config import JWTConfig


class PyJWTPayloadCodec(AuthPayloadCodec):
    def __init__(self, config: JWTConfig) -> None:
        self._config = config

    def encode(
        self, payload: AuthPayload, token_type: Literal["access", "refresh"]
    ) -> bytes:
        now = datetime.now(timezone.utc)
        if token_type == "access":
            expires = now + timedelta(minutes=self._config.access_minutes_expires)
        else:
            expires = now + timedelta(days=self._config.refresh_days_expires)

        payload = {
            "sub": str(payload.user_id),
            "iat": now,
            "exp": expires,
        }
        result = jwt.encode(
            payload=payload,
            key=self._config.secret_key,
            algorithm=self._config.algorithm,
        )
        return result

    def decode(self, token: str | bytes) -> dict:
        if type(token) is str:
            token = token.encode("utf-8")

        result = jwt.decode(
            token,
            key=self._config.public_key,
            algorithms=[self._config.algorithm],
        )

        return result
