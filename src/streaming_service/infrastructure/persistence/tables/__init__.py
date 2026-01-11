__all__ = [
    "mapper_registry",
    "setup_tables",
    "film_table",
    "film_genre_table",
    "genre_table",
]

from .base import mapper_registry
from .film import map_film_table, map_film_genre_table, film_genre_table, film_table
from .genre import map_genre_table, genre_table


def setup_tables() -> None:
    map_genre_table()
    map_film_table()
    map_film_genre_table()
