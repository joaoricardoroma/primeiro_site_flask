from storage import Pokemon
import requests
r = requests.get("https://pokeapi.co/api/v2/pokemon?limit=1118")
result_api = r.json()

for pokemon_api in result_api["results"]:
    r = requests.get(pokemon_api['url'])
    detail = r.json()

    types_api = detail["types"]
    list_types = []

    for type_api in types_api:
        list_types.append(type_api["type"]['name'])

    pokemon = Pokemon(pokemon_api['name'], list_types)
    print(pokemon)
