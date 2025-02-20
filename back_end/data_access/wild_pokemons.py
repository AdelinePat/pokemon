import json, os, random
from ..generate_pokemon.create_pokemon import create_world_pokemons, create_low_level_world_pokemons
from .util import instanciate_pokemon
from __settings__ import WORLD_POKEMON_PATH, NAME_LIST_PATH

def generate_pokemons_dict():
    with open(NAME_LIST_PATH, 'r', encoding="UTF-8") as file:
        name_list = json.load(file)

    all_pokemons = create_low_level_world_pokemons()
    pokemons_dict_list = []
    
    # index = random.randrange(len(name_list))
    for index, each_pokemon in enumerate(all_pokemons):
        if index == len(name_list)-1:
            index = 0
        each_pokemon.set_pet_name("Jean-" + name_list[index])
        a_pokemon = each_pokemon.pokemon_dict()
        pokemons_dict_list.append(a_pokemon)
    
    return pokemons_dict_list

def save_world_pokemons(pokemons_dict_list):
    if not os.path.exists(WORLD_POKEMON_PATH):
        with open(WORLD_POKEMON_PATH, "w", encoding="UTF-8") as file:
            json.dump({}, file)
    with open(WORLD_POKEMON_PATH, "w", encoding="UTF-8") as file:
        json.dump(pokemons_dict_list, file, indent=4)

def save_wild_pokemon(my_pokemon):
    with open(WORLD_POKEMON_PATH, "r") as file:
        pokemons_dict_list = json.load(file)
    
    my_pokemon.set_state('wild')
    pokemons_dict_list.append(my_pokemon.pokemon_dict())

    with open(WORLD_POKEMON_PATH, "w", encoding="UTF-8") as file:
        json.dump(pokemons_dict_list, file, indent=4)

def get_random_wild_pokemon():
    if not os.path.exists(WORLD_POKEMON_PATH):
        with open(WORLD_POKEMON_PATH, "w", encoding="UTF-8") as file:
            json.dump([], file)

    with open(WORLD_POKEMON_PATH, "r") as file:
        pokemons = json.load(file)

    if not pokemons or len(pokemons) < 4 :
        pokemons = generate_pokemons_dict()

    a_pokemon = random.choice(pokemons)
    pokemons.pop(pokemons.index(a_pokemon))

    save_world_pokemons(pokemons)
    my_pokemon = instanciate_pokemon(a_pokemon)

    return my_pokemon