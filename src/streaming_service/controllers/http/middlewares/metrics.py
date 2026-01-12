import time

from fastapi import FastAPI
from starlette.types import Receive, Scope, Send

from streaming_service.controllers.prometheus.metrics import (
    http_requests_total,
    http_request_duration_seconds,
    http_errors_4xx_total,
    http_errors_5xx_total,
)


class MetricsMiddleware:
    def __init__(self, app: FastAPI):
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        start_time = time.time()
        status_code: int | None = None

        async def send_wrapper(message):
            nonlocal status_code

            if message["type"] == "http.response.start":
                status_code = message["status"]

            await send(message)

        await self.app(scope, receive, send_wrapper)

        duration = time.time() - start_time

        method = scope.get("method")
        endpoint = "unknown"

        if "route" in scope:
            endpoint = scope["route"].path

        http_requests_total.labels(
            method=method, endpoint=endpoint, status_code=status_code
        ).inc()

        http_request_duration_seconds.labels(
            method=method,
            endpoint=endpoint,
        ).observe(duration)

        if status_code >= 500:
            http_errors_5xx_total.labels(
                method=method, endpoint=endpoint, status_code=status_code
            ).inc()
        elif status_code >= 400:
            http_errors_4xx_total.labels(
                method=method, endpoint=endpoint, status_code=status_code
            ).inc()
