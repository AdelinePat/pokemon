from __settings__ import WORLD_POKEMON_PATH, PLAYER_POKEDEX
import json

with open(WORLD_POKEMON_PATH, "r", encoding="UTF-8") as file:
    my_list = json.load(file)

print(my_list[5]["pet_name"])

with open(PLAYER_POKEDEX, "r", encoding="UTF-8") as file:
    name_list = list(json.load(file).keys())

print(name_list[-1])