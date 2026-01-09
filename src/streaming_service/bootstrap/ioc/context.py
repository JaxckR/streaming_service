from dishka import Provider, Scope, from_context

from streaming_service.bootstrap.config import PostgresConfig


class ContextProvider(Provider):
    scope = Scope.APP

    postgres_config = from_context(PostgresConfig)
