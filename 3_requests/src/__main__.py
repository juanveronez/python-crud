import time
import random

from controller import fetch_pokemon_data, add_pokemon_to_db

def main():
    while True:
        pokemon_id = random.randint(1, 350)
        pokemon = fetch_pokemon_data(pokemon_id)
        
        if pokemon:
            print(f'Adding {pokemon.name} to database.')
            add_pokemon_to_db(pokemon)
        else:
            print(f'Data not fount to pokemon with ID: {pokemon_id}')
        time.sleep(10)

if __name__ == '__main__':
    main()