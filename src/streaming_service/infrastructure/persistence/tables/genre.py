import sqlalchemy as sa

from streaming_service.entities.genre import Genre
from streaming_service.infrastructure.persistence.tables import mapper_registry

genre_table = sa.Table(
    "genres",
    mapper_registry.metadata,
    sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
    sa.Column("name", sa.String, nullable=False),
    sa.Column("created_at", sa.DateTime, server_default=sa.func.now()),
    sa.Column("updated_at", sa.DateTime, server_onupdate=sa.func.now(), nullable=True),
)


def map_genre_table() -> None:
    _ = mapper_registry.map_imperatively(
        Genre,
        genre_table,
        properties={
            "id": genre_table.c.id,
            "name": genre_table.c.name,
            "created_at": genre_table.c.created_at,
            "updated_at": genre_table.c.updated_at,
        },
        column_prefix="_",
    )
