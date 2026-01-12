from prometheus_client import (
    CollectorRegistry,
    Counter,
    Histogram,
    ProcessCollector,
    PlatformCollector,
    GCCollector,
)

registry = CollectorRegistry()

ProcessCollector(registry=registry)
PlatformCollector(registry=registry)
GCCollector(registry=registry)


http_requests_total = Counter(
    "http_requests_total",
    "Total number of HTTP requests",
    ["method", "endpoint", "status_code"],
    registry=registry,
)

http_request_duration_seconds = Histogram(
    "http_request_duration_seconds",
    "HTTP request duration in seconds",
    ["method", "endpoint"],
    registry=registry,
)

http_errors_4xx_total = Counter(
    "http_errors_4xx_total",
    "Total number of 4xx HTTP errors",
    ["method", "endpoint", "status_code"],
    registry=registry,
)

http_errors_5xx_total = Counter(
    "http_errors_5xx_total",
    "Total number of 5xx HTTP errors",
    ["method", "endpoint", "status_code"],
    registry=registry,
)
