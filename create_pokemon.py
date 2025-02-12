import random, json
from pokemon import Pokemon
from __settings__ import COEFFICIENT_PATH, TYPES_PATH, EVOLUTION_STAGE_PATH

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

def save_pokemon():

    with open(TYPES_PATH, 'r') as file:
        types = json.load(file)
        type_list = list(types.keys())

    all_pokemons = []
    for type in type_list:
        a_pokemon = create_pokemon(type)
        all_pokemons.append(a_pokemon)
        # print(a_pokemon)
    
    return all_pokemons
    # with open('pokemons.json', 'w', encoding="UTF-8") as pokemon_file:
    #     data = json.dump(all_pokemons, pokemon_file, indent=4)

# save_pokemon()
