from beckett.exceptions import InvalidStatusCodeError, MissingUidException
from pokepy import V2Client

from src.poke.exceptions import NotFound
from src.poke.models import Pokemon


class PokemonService:
    def __init__(self):
        self.poke_client = V2Client()

    def pokemon_with_moves(self, pokemon_id: int) -> Pokemon:
        try:
            pokemon = self.poke_client.get_pokemon(pokemon_id)
        except (InvalidStatusCodeError, MissingUidException):
            raise NotFound(f"Invalid pokemon id ({pokemon_id})")
        return Pokemon(
            id=pokemon_id,
            name=pokemon.name,
            moves=sorted(move.move.name for move in pokemon.moves),
        )
