from dishka import Provider, Scope, provide_all

from streaming_service.application.factories import FilmFactory, UserFactory
from streaming_service.application.handlers.auth import (
    LoginHandler,
    LogoutHandler,
    SignUpHandler,
)
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

    fabrics = provide_all(FilmFactory, UserFactory, scope=Scope.APP)

    handlers = provide_all(
        CreateFilmHandler,
        DeleteFilmHandler,
        GetFilmHandler,
        GetAllFilmsHandler,
        CreateGenreHandler,
        GetAllGenresHandler,
        LoginHandler,
        LogoutHandler,
        SignUpHandler,
    )
