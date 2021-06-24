from unittest.mock import Mock

from pytest import fixture
from starlette.status import HTTP_200_OK, HTTP_422_UNPROCESSABLE_ENTITY

from src.poke.root import pokemon_service
from tests.factories import create_pokemon
from tests.requests import get_pokemon_moves


@fixture
def sample_pokemon():
    return create_pokemon()


@fixture
def pokemon_service_patch(app, sample_pokemon):
    app.dependency_overrides[pokemon_service] = lambda: Mock(
        pokemon_with_moves=Mock(return_value=sample_pokemon)
    )


def test_pokemon_moves_getter_passes_correctly(
    api_client, pokemon_service_patch, sample_pokemon
):
    response = get_pokemon_moves(api_client, 222)

    assert response.status_code == HTTP_200_OK
    assert response.json() == sample_pokemon


def test_pokemon_moves_getter_fails_with_422_when_invalid_pokemon_id_type(
    app, api_client, pokemon_service_patch
):
    response = get_pokemon_moves(api_client, "unexisting")

    assert response.status_code == HTTP_422_UNPROCESSABLE_ENTITY
