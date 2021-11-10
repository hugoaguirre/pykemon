from pydantic import BaseModel

class PokemonBasicInfo(BaseModel):
    id: int
    name: str
    height: int
    weight: int