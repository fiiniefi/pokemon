from pytest import fixture, raises, mark

from src.poke.exceptions import NotFound
from src.poke.models import Pokemon
from src.poke.service import PokemonService


@fixture
def pokemon_750():
    return Pokemon(
        id=750,
        name="mudsdale",
        moves=[
            "attract",
            "bide",
            "bulldoze",
            "confide",
            "counter",
            "double-kick",
            "double-team",
            "earthquake",
            "facade",
            "focus-blast",
            "frustration",
            "giga-impact",
            "heavy-slam",
            "hidden-power",
            "high-horsepower",
            "iron-defense",
            "low-sweep",
            "mega-kick",
            "mud-slap",
            "mud-sport",
            "payback",
            "protect",
            "rest",
            "return",
            "roar",
            "rock-slide",
            "rock-tomb",
            "rototiller",
            "round",
            "sandstorm",
            "sleep-talk",
            "stomp",
            "substitute",
            "superpower",
            "swagger",
            "toxic",
        ],
    )


@fixture
def pokemon_service():
    return PokemonService()


def test_pokemon_service_returns_valid_pokemon_by_id(pokemon_service, pokemon_750):
    pokemon_id = 750

    pokemon = pokemon_service.pokemon_with_moves(pokemon_id)

    assert pokemon == pokemon_750


@mark.parametrize("pokemon_id", [100000, "asd", 0, -1])
def test_pokemon_service_raises_not_found_when_invalid_pokemon_number(
    pokemon_service, pokemon_id
):
    pokemon_id = "asd"

    with raises(NotFound):
        pokemon_service.pokemon_with_moves(pokemon_id)
