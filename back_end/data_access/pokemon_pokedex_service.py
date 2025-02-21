
import json
from __settings__ import PLAYER_POKEDEX
from .util import instanciate_pokemon

def save_pokemon_to_pokedex(player, pokemon):   
    with open(PLAYER_POKEDEX, "r") as file:
        player_pokedex = json.load(file)

    pokemon.set_state('domesticated')
    player_pokedex[player]["pokemons"].update({pokemon.pet_name : pokemon.pokemon_dict()})

    with open(PLAYER_POKEDEX, "w", encoding="UTF-8") as file:
        json.dump(player_pokedex, file, indent=4)

def get_pokemon_from_pokedex(player_name, pokemon_pet_name):
    with open(PLAYER_POKEDEX, "r") as file:
        pokemons = json.load(file)[player_name]["pokemons"]

    for pokemon in pokemons:
        if pokemon == pokemon_pet_name:
            my_pokemon = instanciate_pokemon(pokemons[pokemon])
            return my_pokemon
        
def get_all_pokemons_from_pokedex(player_name):
    with open(PLAYER_POKEDEX, "r") as file:
        pokemons = json.load(file)[player_name]["pokemons"]

    pokemon_list = []
    for pokemon in pokemons:
        my_pokemon = instanciate_pokemon(pokemons[pokemon])
        pokemon_list.append(my_pokemon)

    return pokemon_list

def get_first_pokemon(player_name):
    with open(PLAYER_POKEDEX, "r") as file:
        pokemons = json.load(file)[player_name]["pokemons"]
        pokemon_keys = list(pokemons.keys())

    my_pokemon = instanciate_pokemon(pokemons[pokemon_keys[0]])
    return my_pokemon

def get_player_pokemons(player):
    with open(PLAYER_POKEDEX, "r", encoding="UTF-8") as file:
        pokemons_dictionary = json.load(file)
        player_pokemons = pokemons_dictionary[player]["pokemons"].keys()
    return player_pokemons