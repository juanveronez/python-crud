import requests
from pydantic import BaseModel

class PokemonSchema(BaseModel):
    name: str
    types: list[str]

    class Config:
        orm_mode = True # Define que será usado em um ORM

def get_pokemon(id: int):
    url = f'https://pokeapi.co/api/v2/pokemon/{id}'
    response = requests.get(url)
    data = response.json()

    data_types = data['types']
    data_name = data['name']

    types_list = [data_type['type']['name'] for data_type in data_types]
    types = ', '.join(types_list)

    return PokemonSchema(name=data_name, types=types)


if __name__ == '__main__':
    print(get_pokemon(15))
    print(get_pokemon(3))
    print(get_pokemon(25))
    print(get_pokemon(135))