from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter

from streaming_service.application.handlers.auth import (
    LoginRequest,
    LoginHandler,
    LogoutHandler,
    SignUpRequest,
    SignUpHandler,
)

auth_router = APIRouter(prefix="/auth", tags=["auth"], route_class=DishkaRoute)


@auth_router.post("/login")
async def login(request: LoginRequest, handler: FromDishka[LoginHandler]):
    await handler.handle(request)


@auth_router.delete("/logout")
async def logout(handler: FromDishka[LogoutHandler]):
    await handler.handle()


@auth_router.post("/sign-up")
async def sign_up(request: SignUpRequest, handler: FromDishka[SignUpHandler]):
    await handler.handle(request)
