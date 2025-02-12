import random, json, os
from models.pokemon import Pokemon
from __settings__ import TYPES_PATH, WORLD_POKEMON_PATH


def get_name(type_list):
    with open(TYPES_PATH, 'r') as file:
        type_name_dictionary = json.load(file)
        if len(type_list) == 2:
            get_name_list = type_name_dictionary[type_list[0]][type_list[1]]["names"]     
        else:
            get_name_list = type_name_dictionary[type_list[0]]["alone"]["names"]
    
    choice_list = list(get_name_list.keys())
    first_stage_name = random.choice(choice_list)
    # first_stage_name = random.choice(get_name_list)
    name = random.choice(list(get_name_list[first_stage_name].keys()))

    if get_name_list[first_stage_name][name] == 3:
        level = random.randrange(25, 36)
        stage = 3

    elif get_name_list[first_stage_name][name] == 4:
        level = random.randrange(40, 50)
        stage = 4

    elif get_name_list[first_stage_name][name] == 2:
        level = random.randrange(12, 20)
        stage = 2

    else:
        level = random.randrange(1, 10)
        stage = 1
    return name, first_stage_name, level, stage
    
def create_pokemon(first_type):
    final_type_list = [first_type]

    with open(TYPES_PATH, 'r') as file:
        second_type = json.load(file)
        get_second_type_dict = second_type[first_type]
    
    second_type_list = []
    for type in get_second_type_dict:
        value = get_second_type_dict[type]["probability"]
        for index in range(value):
            second_type_list.append(type)
    
    second_type_random = random.choice(second_type_list)
    if second_type_random != "alone":
        final_type_list.append(second_type_random)

    name, first_stage_name, level, stage = get_name(final_type_list)

    hp = random.randrange(10, 31) + level*3
    strength = random.randrange(2,31) + level*3
    speed = random.randrange(2,31) + level*3
    defense_point = random.randrange(2,31) + level*3

    my_pokemon = Pokemon(name, first_stage_name, hp, strength, defense_point, final_type_list, level, speed, stage)

    return my_pokemon

def create_world_pokemons():

    with open(TYPES_PATH, 'r') as file:
        types = json.load(file)
        type_list = list(types.keys())

    all_pokemons = []
    for type in type_list:
        a_pokemon = create_pokemon(type)
        all_pokemons.append(a_pokemon)
        # print(a_pokemon)
    
    return all_pokemons

def save_pokemon():

    all_pokemons = create_world_pokemons()
    pokemons_dict_list = []
    for each_pokemon in all_pokemons:
        a_pokemon = each_pokemon.pokemon_dict()
        pokemons_dict_list.append(a_pokemon)
            # "name" : each_pokemon.name,
            # "original_name" : each_pokemon.get_original_name(),
            # "hp" : each_pokemon.get_hp(),
            # "xp" : each_pokemon.get_xp(),
            # "strength" : each_pokemon.get_strength(),
            # "defense" : each_pokemon.get_defense(),
            # "type" : each_pokemon.type,
            # "level" : each_pokemon.get_level(),
            # "speed" : each_pokemon.get_speed(),
            # "stage" : each_pokemon.get_stage(),
            # "ev" : each_pokemon.get_effort_value().get_ev_dict()
            # "ev_hp" : each_pokemon.get_ev_hp(),
            # "ev_strength" : each_pokemon.get_ev_strength(),
            # "ev_defense" : each_pokemon.get_ev_defense(),
            # "ev_xp" : each_pokemon.get_ev_xp()
            # name, first_stage_name, hp, strength, defense_point, final_type_list, level, speed, stage
        #     self.__ev_hp = 0
        # self.__ev_strength = 0
        # self.__ev_defense = 0
        # self.__ev_speed = 0
        # self.__ev_xp = 0
        # }
        
    if not os.path.exists(WORLD_POKEMON_PATH):
        # Create an empty JSON file if it doesn't exist
        with open(WORLD_POKEMON_PATH, "w", encoding="UTF-8") as file:
            json.dump({}, file)
    with open(WORLD_POKEMON_PATH, "w") as file:
        # pokemons_data = json.load(file)
        json.dump(pokemons_dict_list, file, indent=4)

    # with open('pokemons.json', 'w', encoding="UTF-8") as pokemon_file:
    #     data = json.dump(all_pokemons, pokemon_file, indent=4)

save_pokemon()
