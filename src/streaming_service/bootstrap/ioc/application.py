from dishka import Provider, Scope, provide_all

from streaming_service.application.factories.film import FilmFactory
from streaming_service.application.handlers.film import (
    CreateFilmHandler,
    DeleteFilmHandler,
    GetAllFilmsHandler,
    GetFilmHandler,
)
from streaming_service.application.handlers.genre import (
    CreateGenreHandler,
    GetAllGenresHandler,
)


class ApplicationProvider(Provider):
    scope = Scope.REQUEST

    fabrics = provide_all(FilmFactory)

    handlers = provide_all(
        CreateFilmHandler,
        DeleteFilmHandler,
        GetFilmHandler,
        GetAllFilmsHandler,
        CreateGenreHandler,
        GetAllGenresHandler,
    )
