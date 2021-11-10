from typing import Union

from fastapi import APIRouter, HTTPException, status
from requests import HTTPError

from pykemon.pokeapi import pokemon
from pykemon.models.pokemon_schemas import PokemonBasicInfo

router = APIRouter()


@router.get("/{req_pokemon}", response_model=PokemonBasicInfo)
def get_pokemon(req_pokemon: Union[int, str]):
    """
    Obtains the Pokedex information from the requested Pokemon
    :param req_pokemon
    :return: PokemonBasicInfo
    """
    response = pokemon.get_pokemon(req_pokemon)

    if response.ok is False:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail=response.text)

    return response.json()
