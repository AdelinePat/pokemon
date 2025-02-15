
import json, os
from __settings__ import PLAYER_POKEDEX
from .util import instanciate_pokemon

def to_player_pokedex(player, pokemon):
    if not os.path.exists(PLAYER_POKEDEX):
        with open(PLAYER_POKEDEX, "w", encoding="UTF-8") as file:
            json.dump({}, file)
    
    with open(PLAYER_POKEDEX, "r") as file:
        pokemons_dictionary = json.load(file)

    pokemon.set_state('domesticated')
    pokemons_dictionary[player].update({pokemon.pet_name : pokemon.pokemon_dict()})

    # pokemons_list.append(pokemon_dictionary)

    with open(PLAYER_POKEDEX, "w", encoding="UTF-8") as file:
        json.dump(pokemons_dictionary, file, indent=4)

def get_pokemon_from_pokedex(player_name, pokemon_pet_name):
    with open(PLAYER_POKEDEX, "r") as file:
        pokemons = json.load(file)[player_name]

    for pokemon in pokemons:
        if pokemon == pokemon_pet_name:
            my_pokemon = instanciate_pokemon(pokemons[pokemon])
            return my_pokemon

def get_petnames_from_pokedex():
    with open(PLAYER_POKEDEX, "r", encoding="UTF-8") as file:
        pokemons_dictionary = json.load(file)

    pokemons_names = list(pokemons_dictionary.keys())

    return pokemons_names