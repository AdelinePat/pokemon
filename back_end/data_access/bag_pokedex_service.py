import json
from .util import instanciate_bag
from __settings__ import PLAYER_POKEDEX

def save_bag_to_pokedex(player, bag):
    with open(PLAYER_POKEDEX, "r") as file:
        player_pokedex = json.load(file)

    player_pokedex[player]["bag"].update(bag.get_dict())

    with open(PLAYER_POKEDEX, "w", encoding="UTF-8") as file:
        json.dump(player_pokedex, file, indent=4)

def get_bag_from_pokedex(player):
    with open(PLAYER_POKEDEX, "r") as file:
        player_bag = json.load(file)[player]["bag"]

    bag = instanciate_bag(player_bag)
    return bag