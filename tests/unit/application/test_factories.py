from datetime import datetime

import pytest
from dishka import AsyncContainer

from streaming_service.application.exceptions import FieldError
from streaming_service.application.factories import UserFactory, FilmFactory
from streaming_service.entities.genre import Genre


@pytest.mark.parametrize(
    ("username", "password", "email", "exc"),
    [
        ("username", "password", "correctEmail@business.com", None),
        ("username", "len", "correctEmail@business.com", FieldError),
        ("incorrectSym#!`=", "len", "correctEmail@business.com", FieldError),
        ("username", "len", "incorrectMailmail.ru", FieldError),
        ("username", "len", "incorrect@gmail@com", FieldError),
        ("username", "len", "incorrectMail@mail", FieldError),
    ],
)
async def test_user_factory(
    username: str,
    password: str,
    email: str,
    exc: type[Exception] | None,
    container: AsyncContainer,
) -> None:
    factory = await container.get(UserFactory)

    if exc is not None:
        with pytest.raises(exc):
            _ = factory.create(
                username=username,
                password=password,
                email=email,
            )
    else:
        user = factory.create(
            username=username,
            password=password,
            email=email,
        )
        assert user.id is not None
        assert user.username == username
        assert user.password != password
        assert user.email == email


@pytest.mark.parametrize(
    ("title", "description", "genres", "country", "release_date", "rating", "exc"),
    [
        (
            "Garry Potter",
            "A young wizard’s journey",
            ["Fantasy", "Adventure"],
            "UK",
            "2001",
            89,
            None,
        )
    ],
)
async def test_film_factory(
    title: str,
    description: str,
    genres: list[str],
    country: str,
    release_date: datetime,
    rating: int | None,
    exc: type[Exception] | None,
    container: AsyncContainer,
) -> None:
    factory = await container.get(FilmFactory)

    if exc is not None:
        with pytest.raises(exc):
            _ = factory.create(
                title=title,
                description=description,
                genres=[
                    Genre(
                        id=index,
                        name=name,
                        created_at=datetime.now(),
                        updated_at=None,
                    )
                    for index, name in enumerate(genres)
                ],
                country=country,
                release_date=release_date,
                rating=rating,
            )
    else:
        film = factory.create(
            title=title,
            description=description,
            genres=[
                Genre(
                    id=index,
                    name=name,
                    created_at=datetime.now(),
                    updated_at=None,
                )
                for index, name in enumerate(genres)
            ],
            country=country,
            release_date=release_date,
            rating=rating,
        )
        assert film.id is not None
        assert film.title == title
        assert film.description == description
        assert film.country == country
        assert film.release_date == release_date
        assert film.rating == rating
