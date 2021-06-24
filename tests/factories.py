from src.poke.models import Pokemon


def create_pokemon(id=1, name="name", moves=None):
    return Pokemon(id=id, name=name, moves=moves or [])
