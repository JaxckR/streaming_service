from uuid_extensions import uuid7

from streaming_service.application.ports.id_generator import IdGenerator
from streaming_service.entities.film import FilmId


class IdGeneratorImpl(IdGenerator):
    def film_id(self) -> FilmId:
        return FilmId(uuid7())
