from dataclasses import dataclass
from functools import cached_property
from os import getenv
from pathlib import Path
from typing import Literal

BASE_DIR = Path(__file__).resolve().parents[2]


@dataclass(frozen=True, slots=True)
class PostgresConfig:
    user: str
    password: str
    host: str
    port: int
    database: str

    @property
    def url(self) -> str:
        return f"postgresql+psycopg://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"


@dataclass(frozen=True)
class JWTConfig:
    algorithm: Literal[
        "HS256",
        "HS384",
        "HS512",
        "RS256",
        "RS384",
        "RS512",
    ]
    access_minutes_expires: int
    refresh_days_expires: int

    @cached_property
    def secret_key(self) -> str:
        with open(BASE_DIR.parent / "jwt_private.key") as r:
            return r.read()

    @cached_property
    def public_key(self) -> str:
        with open(BASE_DIR.parent / "jwt_public.key") as r:
            return r.read()


@dataclass(slots=True, frozen=True)
class RabbitConfig:
    host: str
    port: int
    username: str
    password: str


@dataclass(frozen=True, slots=True)
class Config:
    postgres: PostgresConfig
    rabbit: RabbitConfig
    jwt: JWTConfig


config = Config(
    postgres=PostgresConfig(
        user=getenv("POSTGRES_USER"),
        password=getenv("POSTGRES_PASSWORD"),
        host=getenv("POSTGRES_HOST"),
        port=int(getenv("POSTGRES_PORT")),
        database=getenv("POSTGRES_DB"),
    ),
    rabbit=RabbitConfig(
        host=getenv("RABBITMQ_HOST"),
        port=int(getenv("RABBITMQ_PORT")),
        username=getenv("RABBITMQ_USERNAME"),
        password=getenv("RABBITMQ_PASSWORD"),
    ),
    jwt=JWTConfig(
        algorithm=getenv("JWT_ALGORITHM"),
        access_minutes_expires=int(getenv("JWT_ACCESS_MINUTES_EXPIRES")),
        refresh_days_expires=int(getenv("JWT_REFRESH_DAYS_EXPIRES")),
    ),
)
