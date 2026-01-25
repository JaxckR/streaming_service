import re

from datetime import datetime
from typing import cast, Final, Pattern

from streaming_service.application.exceptions import FieldError
from streaming_service.application.ports import IdGenerator, Hasher
from streaming_service.entities.user import User


class UserFactory:
    PASSWORD_MIN_LENGTH: Final[int] = 8
    EMAIL_REGEX: Final[Pattern[str]] = re.compile(
        r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    )
    USERNAME_REGEX: Final[Pattern[str]] = re.compile(
        r"^[a-zA-Z0-9][a-zA-Z0-9_]{1,253}[a-zA-Z0-9]$"
    )

    def __init__(self, id_generator: IdGenerator, hasher: Hasher) -> None:
        self._id_generator = id_generator
        self._hasher = hasher

    def create(self, username: str, password: str, email: str) -> User:
        if len(password) < self.PASSWORD_MIN_LENGTH:
            raise FieldError(
                f"Password must be at least {self.PASSWORD_MIN_LENGTH} length"
            )

        if not self.USERNAME_REGEX.match(username):
            raise FieldError("Incorrect username")

        if not self.EMAIL_REGEX.match(email):
            raise FieldError("Incorrect email")

        hashed_password = self._hasher.hash_password(password)
        return User(
            id=self._id_generator.user_id(),
            username=username,
            password=hashed_password,
            email=email,
            created_at=cast(datetime, None),
            updated_at=None,
            deleted_at=None,
        )
