from dataclasses import dataclass
from os import getenv


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
)
