import json, os, random
from generate_pokemon.create_pokemon import create_world_pokemons
from __settings__ import WORLD_POKEMON_PATH

def save_pokemon():

    all_pokemons = create_world_pokemons()
    pokemons_dict_list = []
    for each_pokemon in all_pokemons:
        a_pokemon = each_pokemon.pokemon_dict()
        pokemons_dict_list.append(a_pokemon)
        
    if not os.path.exists(WORLD_POKEMON_PATH):
        with open(WORLD_POKEMON_PATH, "w", encoding="UTF-8") as file:
            json.dump({}, file)
    with open(WORLD_POKEMON_PATH, "w") as file:
        json.dump(pokemons_dict_list, file, indent=4)

save_pokemon()

def from_json():
    with open(WORLD_POKEMON_PATH, "w") as file:
        pokemons = json.load(file)
    
    a_pokemon = random.choice(pokemons)
    pokemons.pop(pokemons.index(a_pokemon))

    with open(WORLD_POKEMON_PATH, "w") as file:
        json.dump(pokemons, file, indent=4)
    
    return a_pokemon
