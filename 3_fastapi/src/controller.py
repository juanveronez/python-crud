import requests

from db import SessionLocal, engine, Base
from models import Pokemon
from schemas import PokemonSchema

Base.metadata.create_all(bind=engine)

def fetch_pokemon_data(pokemon_id: int):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}'
    response = requests.get(url)
    
    if response.status_code != 200:
        return None
    
    data = response.json()

    data_types = data['types']
    data_name = data['name']

    types_list = [data_type['type']['name'] for data_type in data_types]
    types = ', '.join(types_list)

    return PokemonSchema(name=data_name, types=types)

def add_pokemon_to_db(pokemon: PokemonSchema) -> Pokemon:
    with SessionLocal() as session:
        db_pokemon = Pokemon(name=pokemon.name, types=pokemon.types)
        session.add(db_pokemon)
        session.commit()
        session.refresh(db_pokemon)
        return db_pokemon
    
