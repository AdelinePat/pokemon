from __settings__ import WORLD_POKEMON_PATH, PLAYER_POKEDEX, NAME_LIST_PATH, TYPES_PATH, EVOLUTION_STAGE_PATH
import json
from back_end.data_access.pokemon_pokedex_service import save_pokemon_to_pokedex
from back_end.data_access.util import instanciate_pokemon
from back_end.data_access.wild_pokemons import get_random_wild_pokemon
from back_end.generate_pokemon.create_pokemon import level_from_stage
import random
from back_end.models.pokemon import Pokemon

# def test():
#   final_type_list = [first_type]

    # get_second_type_dict = get_first_type_dict(first_type)
    
    # second_type_list = []

    # for type in get_second_type_dict:
    #     value = get_second_type_dict[type]["probability"]
    #     for index in range(value):
    #         second_type_list.append(type)
    
    # second_type_random = random.choice(second_type_list)
    # if second_type_random != "alone":
    #     final_type_list.append(second_type_random)

    # name, first_stage_name, stage = __get_pokemon_from_type(final_type_list)
    # level = level_from_stage(stage)

    # hp = random.randrange(10, 31) + level*3
    # strength = random.randrange(2,31) + level*3
    # speed = random.randrange(2,31) + level*3
    # defense_point = random.randrange(2,21) + level*3

    # my_pokemon = Pokemon(name, first_stage_name, hp, hp, strength, defense_point, final_type_list, level, speed, stage)
    
    # xp = random.randrange(my_pokemon.get_level()**3, (my_pokemon.get_level()+1)**3)
    # my_pokemon.set_xp(xp)

def create_low_level_world_pokemons():
    with open(EVOLUTION_STAGE_PATH, 'r') as file:
        pokemons_original_name = json.load(file)
        pokemons_original_name_list = list(pokemons_original_name.keys()) 

    all_pokemons = []
    for name in pokemons_original_name_list:
        if pokemons_original_name[name][name] == 1:

            type_list = []
            first_type, second_type, stage = get_type_low_level_pokemon(name)
            type_list.append(first_type)
            if second_type != "alone":
                type_list.append(second_type)

            level = level_from_stage(stage)

            hp = random.randrange(10, 31) + level*3
            strength = random.randrange(2,31) + level*3
            speed = random.randrange(2,31) + level*3
            defense_point = random.randrange(2,21) + level*3

            my_pokemon = Pokemon(name, name, hp, hp, strength, defense_point, type_list, level, speed, stage)
            
            xp = random.randrange(my_pokemon.get_level()**3, (my_pokemon.get_level()+1)**3)
            my_pokemon.set_xp(xp)
            all_pokemons.append(my_pokemon)
            print(my_pokemon)

def get_type_low_level_pokemon(original_name):
    with open(TYPES_PATH, 'r') as file:
        types = json.load(file)
        type_list = list(types.keys())

    for first_type in type_list:
        second_type_list = list(types[first_type].keys())

        for second_type in second_type_list:
            names_list = list(types[first_type][second_type]["names"].keys())

            for name in names_list:
                final_name_list = list(types[first_type][second_type]["names"][name].keys())
                final_name_dict = types[first_type][second_type]["names"][name]
                if 1 in list(final_name_dict.values()):
                    final_name = final_name_list[list(final_name_dict.values()).index(1)]

                    if final_name == original_name:
                        return first_type, second_type, 1
                                         
create_low_level_world_pokemons()
# first_type, second_type = get_type_low_level_pokemon("Bulbasaur")
# print(first_type, second_type)
# def does_player_exist(player):
#     with open(PLAYER_POKEDEX, "r", encoding="UTF-8") as file:
#         player_keys_dictionary = list(json.load(file).keys())
    
#     return player in player_keys_dictionary
    
# print(does_player_exist("Baba"))


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