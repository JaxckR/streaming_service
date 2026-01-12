from dataclasses import dataclass


@dataclass(frozen=True)
class ApplicationError(Exception):
    msg: str = "Application error occurred"

    @property
    def message(self) -> str:
        return self.msg


class NotFoundError(ApplicationError): ...
