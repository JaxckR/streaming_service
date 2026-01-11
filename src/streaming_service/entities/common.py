from dataclasses import dataclass
from typing import TypeVar, Generic

IdType = TypeVar("IdType")


@dataclass
class IdEntity(Generic[IdType]):
    id: IdType
