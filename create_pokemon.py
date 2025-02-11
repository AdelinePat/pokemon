import random, json
from pokemon import Pokemon

def get_name(type_list):
    with open('multiple_type.json', 'r') as file:
        type_name_dictionary = json.load(file)
        if len(type_list) == 2:
            get_name_list = type_name_dictionary[type_list[0]][type_list[1]]["names"]     
        else:
            get_name_list = type_name_dictionary[type_list[0]]["alone"]["names"]
            
    name = random.choice(get_name_list)
    return name
    
def create_pokemon(first_type):
    final_type_list = [first_type]
    hp = random.randrange(30,50)
    strength = random.randrange(5, 15)
    defense_point = 0

    with open('multiple_type.json', 'r') as file:
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

    name = get_name(final_type_list)

    my_pokemon = Pokemon(name, hp, strength, defense_point, final_type_list)

    return my_pokemon

def save_pokemon():

    with open('multiple_type.json', 'r') as file:
        types = json.load(file)
        type_list = list(types.keys())

    all_pokemons = []
    for type in type_list:
        a_pokemon = create_pokemon(type)
        all_pokemons.append(a_pokemon)
        print(a_pokemon)
    
    return all_pokemons
    # with open('pokemons.json', 'w', encoding="UTF-8") as pokemon_file:
    #     data = json.dump(all_pokemons, pokemon_file, indent=4)

# save_pokemon()
