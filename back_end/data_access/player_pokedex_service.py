import json, os
from __settings__ import PLAYER_POKEDEX
from .wild_pokemons import get_random_wild_pokemon
from ..models.bag import Bag
from .pokemon_pokedex_service import save_pokemon_to_pokedex
from .bag_pokedex_service import save_bag_to_pokedex

# back to front
def get_player_names():
    with open(PLAYER_POKEDEX, "r", encoding="UTF-8") as file:
        player_keys_dictionary = json.load(file)
    return player_keys_dictionary.keys()

def does_player_exist(player):
    if not os.path.exists(PLAYER_POKEDEX):
        with open(PLAYER_POKEDEX, "w", encoding="UTF-8") as file:
            json.dump({}, file)

    with open(PLAYER_POKEDEX, "r", encoding="UTF-8") as file:
        player_keys_dictionary = list(json.load(file).keys())

    return player in player_keys_dictionary


# front to back
def create_player(player, pokemon):
    # if not os.path.exists(PLAYER_POKEDEX):
    #     with open(PLAYER_POKEDEX, "w", encoding="UTF-8") as file:
    #         json.dump({}, file)

    with open(PLAYER_POKEDEX, "r", encoding="UTF-8") as file:
        players_dictionary = json.load(file)

    if player not in players_dictionary.keys():
        player_bag = Bag()
        players_dictionary[player] = {
            "bag" : {},
            "pokemons" : {}
            }
    else:
        return
            
    with open(PLAYER_POKEDEX, "w", encoding="UTF-8") as file:
        json.dump(players_dictionary, file, indent=4)
    
    save_pokemon_to_pokedex(player, pokemon)
    save_bag_to_pokedex(player, player_bag)
    # return player_pokemons

def get_starter_pokemon():
    pokemon = get_random_wild_pokemon()
    return pokemon