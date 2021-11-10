from typing import Union

import requests

POKEAPI_URL = "https://pokeapi.co/api/v2/pokemon/$pokemon_id"


def get_pokemon(pokemon: Union[int, str]) -> requests.Response:
    uri = POKEAPI_URL.replace("$pokemon_id", str(pokemon))
    response = requests.get(uri, headers=None, timeout=30)
    return response
