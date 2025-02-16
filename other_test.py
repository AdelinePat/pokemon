from __settings__ import WORLD_POKEMON_PATH, PLAYER_POKEDEX, NAME_LIST_PATH
import json
from back_end.data_access.pokemon_pokedex_service import save_pokemon_to_pokedex
from back_end.data_access.util import instanciate_pokemon
from back_end.data_access.wild_pokemons import get_random_wild_pokemon


def does_player_exist(player):
    with open(PLAYER_POKEDEX, "r", encoding="UTF-8") as file:
        player_keys_dictionary = list(json.load(file).keys())
    
    return player in player_keys_dictionary
    
print(does_player_exist("Baba"))


# instanciate_pokemon()
# pokemon = get_random_wild_pokemon()

# ======
#  pokemon = {
#             "name": "Tauros",
#             "original_name": "Tauros",
#             "pet_name": "Jean-Louis",
#             "hp": 86,
#             "xp": 6941,
#             "strength": 84,
#             "defense": 73,
#             "type": [
#                 "normal"
#             ],
#             "level": 19,
#             "speed": 87,
#             "stage": 2,
#             "ev": {
#                 "hp": 0,
#                 "strength": 0,
#                 "defense": 0,
#                 "speed": 0,
#                 "xp": 0
#             },
#             "state": "domesticated"
#             }

# pokemon_final = instanciate_pokemon(pokemon)
# pokemon_final.set_hp(250)


# save_pokemon_to_pokedex("Adeline", pokemon_final)

#TODO POKEMON NOT FOUND
# MOLTRES

# with open(WORLD_POKEMON_PATH, "r", encoding="UTF-8") as file:
#     my_list = json.load(file)

# print(my_list[5]["pet_name"])

# with open(PLAYER_POKEDEX, "r", encoding="UTF-8") as file:
#     name_list = list(json.load(file).keys())

# print(name_list[-1])

# with open(NAME_LIST_PATH, "r", encoding="UTF-8") as file:
#     name_list = json.load(file)

# print(name_list)

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