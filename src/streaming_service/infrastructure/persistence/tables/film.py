import sqlalchemy as sa
from sqlalchemy.orm import relationship

from streaming_service.entities.film import Film, FilmGenre
from streaming_service.entities.genre import Genre
from streaming_service.infrastructure.persistence.tables import mapper_registry

film_table = sa.Table(
    "films",
    mapper_registry.metadata,
    sa.Column("id", sa.UUID(as_uuid=True), primary_key=True),
    sa.Column("title", sa.String, nullable=False),
    sa.Column("description", sa.String),
    sa.Column("rating", sa.Integer, nullable=False),
    sa.Column("country", sa.String, nullable=False),
    sa.Column("release_date", sa.DateTime, nullable=False),
    sa.Column("created_at", sa.DateTime, server_default=sa.func.now()),
    sa.Column("updated_at", sa.DateTime, server_onupdate=sa.func.now(), nullable=True),
    sa.Column("deleted_at", sa.DateTime, nullable=True),
)

film_genre_table = sa.Table(
    "films_genres",
    mapper_registry.metadata,
    sa.Column("id", sa.BigInteger, primary_key=True, autoincrement=True),
    sa.Column(
        "film_id", sa.UUID(as_uuid=True), sa.ForeignKey("films.id"), nullable=False
    ),
    sa.Column("genre_id", sa.Integer, sa.ForeignKey("genres.id"), nullable=False),
)


def map_film_table() -> None:
    _ = mapper_registry.map_imperatively(
        Film,
        film_table,
        properties={
            "id": film_table.c.id,
            "title": film_table.c.title,
            "description": film_table.c.description,
            "rating": film_table.c.rating,
            "country": film_table.c.country,
            "release_date": film_table.c.release_date,
            "created_at": film_table.c.created_at,
            "updated_at": film_table.c.updated_at,
            "deleted_at": film_table.c.deleted_at,
            "genres": relationship(Genre, secondary=film_genre_table, lazy="selectin"),
        },
        column_prefix="_",
    )


def map_film_genre_table() -> None:
    _ = mapper_registry.map_imperatively(
        FilmGenre,
        film_genre_table,
        properties={
            "id": film_genre_table.c.id,
            "film_id": film_genre_table.c.film_id,
            "genre_id": film_genre_table.c.genre_id,
        },
        column_prefix="_",
    )
