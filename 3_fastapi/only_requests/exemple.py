import requests

def print_pokemon(id: int):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{id}')
    data = response.json()

    data_types = data['types']
    data_name = data['name']

    types_list = [data_type['type']['name'] for data_type in data_types]

    types = ', '.join(types_list)
    print(data_name, '->', types)

if __name__ == '__main__':
    print_pokemon(15)
    print_pokemon(24)
    print_pokemon(19)