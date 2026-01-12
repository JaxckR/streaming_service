from dataclasses import dataclass
from datetime import datetime
from typing import TypeVar, Generic

IdType = TypeVar("IdType")


@dataclass
class IdEntity(Generic[IdType]):
    id: IdType


class Timestamp:
    created_at: datetime
    updated_at: datetime | None
    deleted_at: datetime | None
