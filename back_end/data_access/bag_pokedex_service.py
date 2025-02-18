import json, os
from __settings__ import PLAYER_POKEDEX

def save_bag_to_pokedex(player, bag):
    with open(PLAYER_POKEDEX, "r") as file:
        player_pokedex = json.load(file)

    player_pokedex[player]["bag"].update(bag.get_dict())

    # pokemons_list.append(pokemon_dictionary)

    with open(PLAYER_POKEDEX, "w", encoding="UTF-8") as file:
        json.dump(player_pokedex, file, indent=4)