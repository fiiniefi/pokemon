from src.poke.models import Pokemon
from src.poke.root import pokemon_service
from src.poke.service import PokemonService


def pokemon_with_moves(
    pokemon_id: int, poke_service: PokemonService = pokemon_service()
) -> Pokemon:
    return poke_service.pokemon_with_moves(pokemon_id)
