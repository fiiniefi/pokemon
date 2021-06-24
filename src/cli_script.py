from src.poke.exceptions import NotFound
from src.poke.interface.cli import pokemon_with_moves

print("Insert number of a pokemon according to the PokeAPI")
try:
    pokemon_id = int(input())
except ValueError:
    print("Invalid input (must be a number)")
else:
    try:
        print(pokemon_with_moves(pokemon_id))
    except NotFound:
        print(f"Invalid pokemon id ({pokemon_id})")
