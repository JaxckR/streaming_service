__all__ = [
    "mapper_registry",
    "setup_tables",
    "film_table",
    "film_genre_table",
    "genre_table",
    "user_table",
]

from typing import Final, Callable

from sqlalchemy.exc import ArgumentError

from .base import mapper_registry
from .film import map_film_table, map_film_genre_table, film_genre_table, film_table
from .genre import map_genre_table, genre_table
from .user import map_user_table, user_table

MAPPERS: Final[list[Callable]] = [
    map_genre_table,
    map_film_table,
    map_film_genre_table,
    map_user_table,
]


def setup_tables() -> None:
    for mapper in MAPPERS:
        try:
            mapper()
        except ArgumentError:
            pass
