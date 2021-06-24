def get_pokemon_moves(api_client, pokemon_id):
    return api_client.get(f"pokemon/{pokemon_id}/moves")
