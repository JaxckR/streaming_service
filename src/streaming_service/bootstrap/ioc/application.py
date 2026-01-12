from dishka import Provider, Scope, provide_all

from streaming_service.application.factories.film import FilmFactory
from streaming_service.application.handlers.film.create import CreateFilmHandler
from streaming_service.application.handlers.film.delete import DeleteFilmHandler
from streaming_service.application.handlers.film.get import GetFilmHandler
from streaming_service.application.handlers.film.get_all import GetAllFilmsHandler
from streaming_service.application.handlers.genre.create import CreateGenreHandler
from streaming_service.application.handlers.genre.get_all import GetAllGenresHandler


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
