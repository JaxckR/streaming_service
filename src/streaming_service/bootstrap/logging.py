import logging.config

from typing import Literal

LoggingLevel = Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]

logger = logging.getLogger(__name__)


def setup_logging(level: LoggingLevel = "INFO") -> None:
    level_map: dict[LoggingLevel, int] = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR,
        "CRITICAL": logging.CRITICAL,
    }
    level = level_map[level]

    LOGGER_CONFIG = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "datefmt": "%Y-%m-%d %H:%M:%S",
                "format": "[%(asctime)s.%(msecs)03d] "
                "%(levelname)s - "
                "%(funcName)s "
                "%(module)s:%(lineno)d "
                "%(message)s",
            },
            "default2": {
                "datefmt": "%Y-%m-%d %H:%M:%S",
                "format": "[%(asctime)s.%(msecs)03d] %(levelname)s - %(message)s",
            },
            "uvicorn_access": {
                "()": "uvicorn.logging.AccessFormatter",
                "datefmt": "%Y-%m-%d %H:%M:%S",
                "format": "[%(asctime)s.%(msecs)03d] "
                "%(levelname)s - "
                "%(client_addr)s - "
                '"%(request_line)s"'
                " %(status_code)s",
            },
        },
        "handlers": {
            "default": {
                "class": "logging.StreamHandler",
                "formatter": "default",
                "level": level,
                # "use_colors": True,
            },
            "default2": {
                "class": "logging.StreamHandler",
                "formatter": "default2",
                "level": level,
            },
            "uvicorn_access": {
                "class": "logging.StreamHandler",
                "formatter": "uvicorn_access",
                "level": level,
            },
        },
        "loggers": {
            "": {
                "handlers": ["default"],
                "level": level,
            },
            "uvicorn": {"handlers": ["default2"], "level": level, "propagate": False},
            "uvicorn.access": {
                "handlers": ["uvicorn_access"],
                "level": level,
                "propagate": False,
            },
        },
    }

    logging.config.dictConfig(LOGGER_CONFIG)

    logger.debug("Logging initialized")
