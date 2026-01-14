from dishka import Provider, Scope, provide_all, WithParents

from streaming_service.controllers.http.adapters.request_manager import (
    CookieRequestManager,
)


class PresentationProvider(Provider):
    scope = Scope.REQUEST

    adapters = provide_all(WithParents[CookieRequestManager])
