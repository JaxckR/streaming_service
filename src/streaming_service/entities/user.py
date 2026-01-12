from dataclasses import dataclass
from typing import NewType
from uuid import UUID

from streaming_service.entities.common import IdEntity, Timestamp

UserId = NewType("UserId", UUID)


@dataclass
class User(IdEntity[UserId], Timestamp):
    username: str
    password: str
    email: str
