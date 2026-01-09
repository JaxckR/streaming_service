from fastapi import APIRouter

healthcheck_router = APIRouter(prefix="/healthcheck", tags=["healthcheck"])


@healthcheck_router.get("/")
async def healthcheck():
    return {"status": "OK"}
