from fastapi import APIRouter, Depends

from src.poke.models import Pokemon
from src.poke.root import pokemon_service
from src.poke.service import PokemonService

router = APIRouter()


@router.get("/pokemon/{pokemon_id}/moves")
def pokemon_moves(
    pokemon_id: int, poke_service: PokemonService = Depends(pokemon_service)
) -> Pokemon:
    return poke_service.pokemon_with_moves(pokemon_id)
