from fastapi import APIRouter
from prometheus_client import CONTENT_TYPE_LATEST
from prometheus_client.openmetrics.exposition import generate_latest
from starlette.responses import PlainTextResponse

from streaming_service.controllers.prometheus.metrics import registry

index_router = APIRouter()


@index_router.get("/metrics")
async def get_metrics():
    return PlainTextResponse(
        generate_latest(registry),
        media_type=CONTENT_TYPE_LATEST,
    )
