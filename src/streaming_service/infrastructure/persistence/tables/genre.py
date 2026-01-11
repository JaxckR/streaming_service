import sqlalchemy as sa

from streaming_service.entities.genre import Genre
from streaming_service.infrastructure.persistence.tables import mapper_registry

genre_table = sa.Table(
    "genres",
    mapper_registry.metadata,
    sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
    sa.Column("name", sa.String, nullable=False),
)


def map_genre_table() -> None:
    _ = mapper_registry.map_imperatively(
        Genre,
        genre_table,
        properties={
            "id": genre_table.c.id,
            "name": genre_table.c.name,
        },
        column_prefix="_",
    )
