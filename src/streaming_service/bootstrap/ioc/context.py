from dishka import Provider, Scope, from_context

from streaming_service.bootstrap.config import PostgresConfig, RabbitConfig, JWTConfig


class ContextProvider(Provider):
    scope = Scope.APP

    postgres_config = from_context(PostgresConfig)
    rabbit_config = from_context(RabbitConfig)
    jwt_config = from_context(JWTConfig)
