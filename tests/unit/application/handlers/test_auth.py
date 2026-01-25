import pytest
from dishka import AsyncContainer

from streaming_service.application.exceptions import UnauthorizedError, FieldError
from streaming_service.application.handlers.auth import (
    LoginHandler,
    LoginRequest,
    SignUpHandler,
    SignUpRequest,
    LogoutHandler,
)


@pytest.mark.parametrize(
    ("username", "password", "exc"),
    [
        ("testUsername", "qwerty12345", None),
        ("testUsername", "incorrectPassword", UnauthorizedError),
        ("notFoundUsername", "12345678", UnauthorizedError),
    ],
)
async def test_login(
    username: str, password: str, exc: type[Exception] | None, container: AsyncContainer
) -> None:
    handler = await container.get(LoginHandler)
    request_manager = handler._request_manager
    user_repository = handler._user_repository

    if exc is not None:
        with pytest.raises(exc):
            await handler.handle(LoginRequest(username=username, password=password))
        user_repository.get_by_username.assert_called()
    else:
        await handler.handle(LoginRequest(username=username, password=password))
        request_manager.set_access.assert_called()
        request_manager.set_refresh.assert_called()


@pytest.mark.parametrize(
    ("username", "password", "email", "exc"),
    [
        ("testUsername", "qwerty12345", "test@mail.ru", None),
        ("testUsername", "qwerty12345", "incorrect1gmail.com", FieldError),
        ("testUsername", "qwerty12345", "incorrect2@gmailcom", FieldError),
        ("testUsername", "qwerty12345", "@gmail.ru", FieldError),
        ("testUsername", "12", "test@gmail.com", FieldError),
        ("1", "qwerty12345", "mail@yahoo.com", FieldError),
    ],
)
async def test_sign_up(
    username: str,
    password: str,
    email: str,
    exc: type[Exception] | None,
    container: AsyncContainer,
) -> None:
    handler = await container.get(SignUpHandler)
    user_repository = handler._user_repository
    transaction_manager = handler._transaction_manager

    if exc is not None:
        with pytest.raises(exc):
            await handler.handle(
                SignUpRequest(username=username, password=password, email=email)
            )
    else:
        await handler.handle(
            SignUpRequest(username=username, password=password, email=email)
        )
        user_repository.add.assert_called()
        transaction_manager.commit.assert_called()


async def test_logout(container: AsyncContainer) -> None:
    handler = await container.get(LogoutHandler)
    await handler.handle()
