import sqlalchemy as sa

from streaming_service.entities.user import User
from streaming_service.infrastructure.persistence.tables import mapper_registry

user_table = sa.Table(
    "users",
    mapper_registry.metadata,
    sa.Column("id", sa.UUID(as_uuid=True), primary_key=True),
    sa.Column("username", sa.String(255), unique=True, nullable=False),
    sa.Column("password", sa.String, nullable=False),
    sa.Column("email", sa.String(255), unique=True, nullable=False),
    sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
    sa.Column(
        "updated_at",
        sa.DateTime(timezone=True),
        server_onupdate=sa.func.now(),
        nullable=True,
    ),
    sa.Column("deleted_at", sa.DateTime(timezone=True), nullable=True),
)


def map_user_table() -> None:
    _ = mapper_registry.map_imperatively(
        User,
        user_table,
        properties={
            "id": user_table.c.id,
            "username": user_table.c.username,
            "password": user_table.c.password,
            "email": user_table.c.email,
            "created_at": user_table.c.created_at,
            "updated_at": user_table.c.updated_at,
            "deleted_at": user_table.c.deleted_at,
        },
        column_prefix="_",
    )
