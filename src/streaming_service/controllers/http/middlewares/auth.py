from http.cookies import SimpleCookie

from fastapi import FastAPI
from starlette.datastructures import MutableHeaders
from starlette.requests import Request
from starlette.types import Message, Receive, Scope, Send


class ASGIAuthMiddleware:
    def __init__(self, app: FastAPI):
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        request: Request = Request(scope)

        async def modify_cookies(message: Message) -> None:
            if message["type"] != "http.response.start":
                await send(message)
                return

            headers: MutableHeaders = MutableHeaders(scope=message)

            self._set_cookie(request, headers)
            self._delete_cookie(request, headers)

            await send(message)

        await self.app(scope, receive, modify_cookies)

    def _set_cookie(
        self,
        request: Request,
        headers: MutableHeaders,
    ) -> None:
        state_dict = request.state.__dict__["_state"]
        for key, cookie_data in state_dict.items():
            if key.startswith("set_cookie_"):
                cookie = SimpleCookie()

                cookie[cookie_data.name] = cookie_data.value
                cookie[cookie_data.name]["path"] = "/"
                cookie[cookie_data.name]["httponly"] = True
                cookie[cookie_data.name]["max-age"] = cookie_data.max_age
                cookie[cookie_data.name]["secure"] = cookie_data.secure
                cookie[cookie_data.name]["samesite"] = "none"

                headers.append("Set-Cookie", cookie.output(header="").strip())

    def _delete_cookie(self, request: Request, headers: MutableHeaders) -> None:
        state_dict = request.state.__dict__["_state"]
        for key, value in state_dict.items():
            if key.startswith("remove_cookie_"):
                cookie: SimpleCookie = SimpleCookie()

                cookie[value] = ""
                cookie[value]["path"] = "/"
                cookie[value]["httponly"] = True
                cookie[value]["max-age"] = 0

                headers.append("Set-Cookie", cookie.output(header="").strip())
