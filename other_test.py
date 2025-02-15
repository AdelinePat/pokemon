from __settings__ import WORLD_POKEMON_PATH, PLAYER_POKEDEX, NAME_LIST_PATH
import json

#TODO POKEMON NOT FOUND
# MOLTRES

# with open(WORLD_POKEMON_PATH, "r", encoding="UTF-8") as file:
#     my_list = json.load(file)

# print(my_list[5]["pet_name"])

# with open(PLAYER_POKEDEX, "r", encoding="UTF-8") as file:
#     name_list = list(json.load(file).keys())

# print(name_list[-1])

with open(NAME_LIST_PATH, "r", encoding="UTF-8") as file:
    name_list = json.load(file)

print(name_list)

# name_list = [
# "Baptiste",
# "Michel",
# "Pierre",
# "Paul",
# "Louis",
# "François",
# "Claude",
# "Christophe",
# "Charles",
# "Luc",
# "Marie",
# "Sébastien",
# "Daniel",
# "Eric",
# "Robert",
# "Joseph",
# "Thibault",
# "Adeline",
# "Florence",
# "Eltigani",
# "Jolyne",
# "Mehdi",
# "Vanessa",
# "Noa",
# "Armelle",
# "Morgan",
# "Alicia",
# "Ryan",
# "Ryhad",
# "Emilie",
# "Hubert",
# "Vincent",
# "Roger",
# "David",
# "Thierry",
# "Sarah",
# "Hélène"
# ]

# with open(NAME_LIST_PATH, "w", encoding="UTF-8") as file:
#     json.dump(name_list, file, indent=4)