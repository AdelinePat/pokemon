import json
from __settings__ import WORLD_POKEMON_PATH, PLAYER_POKEDEX
import generate_pokemon.from_to_json as from_to

# back to front
def get_player_names():
    with open(PLAYER_POKEDEX, "r") as file:
        pokemons_dictionary = json.load(file)
    return pokemons_dictionary.keys()

def get_player_pokemons(player):
    with open(PLAYER_POKEDEX, "r") as file:
        pokemons_dictionary = json.load(file)
        player_pokemons = pokemons_dictionary[player].keys()
    return player_pokemons


# front to back
def create_player(player, pokemon):
    with open(PLAYER_POKEDEX, "r") as file:
        pokemons_dictionary = json.load(file)

    if player not in pokemons_dictionary.keys():
        pokemons_dictionary[player] = {pokemon.pet_name : pokemon.pokemon_dict()}
    
    with open(PLAYER_POKEDEX, "w") as file:
        json.dump(pokemons_dictionary, file, indent=4)
    # return player_pokemons

def get_starter_pokemon():
    pokemon = from_to.get_random_wild_pokemon()
    return pokemon