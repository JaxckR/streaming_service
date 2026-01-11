from datetime import datetime
from typing import NewType

from pydantic.dataclasses import dataclass

from streaming_service.entities.common import IdEntity

GenreId = NewType("GenreId", int)


@dataclass
class Genre(IdEntity[GenreId]):
    name: str

    created_at: datetime
    updated_at: datetime | None
