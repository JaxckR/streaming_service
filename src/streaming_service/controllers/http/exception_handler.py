import logging
from functools import partial
from typing import Final

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from starlette import status
from starlette.requests import Request

from streaming_service.application.exceptions import ApplicationError, NotFoundError
from streaming_service.controllers.http.schemas import ErrorResponse

logger = logging.getLogger(__name__)

EXCEPTIONS: Final[dict[Exception:status]] = {
    ApplicationError: status.HTTP_400_BAD_REQUEST,
    NotFoundError: status.HTTP_404_NOT_FOUND,
}


async def validate(_: Request, exception: Exception, code: int) -> ORJSONResponse:
    if info := str(exception):
        content = ErrorResponse(detail=info)
    else:
        content = None

    return ORJSONResponse(status_code=code, content=content)


async def internal_error(_: Request, exception: Exception) -> ORJSONResponse:
    logger.exception("ERROR", exc_info=exception)
    return ORJSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=ErrorResponse(detail="Internal server error").model_dump(),
    )


def setup_exceptions(app: FastAPI) -> None:
    for exc, code in EXCEPTIONS.items():
        app.add_exception_handler(exc, partial(validate, code=code))

    app.add_exception_handler(Exception, internal_error)

    logger.debug("Exception handlers setup")
