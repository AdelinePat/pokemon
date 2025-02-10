import random, json
from pokemon import Pokemon
def get_name(type_list):
    
    with open('multiple_type.json', 'r') as file:
        second_type = json.load(file)
        if len(type_list) == 2:
            get_second_type_names = second_type[type_list[0]][type_list[1]]["names"]     
        else:
            get_second_type_names = second_type[type_list[0]]["alone"]["names"]
            
    
    name = random.choice(get_second_type_names)
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

    # total_probability = 0

    # keys_range = []

    # for each_key_value in get_second_type_dict:
    #     total_probability += get_second_type_dict[each_key_value]
    #     keys_range.append(total_probability)

    # final_type_list = [first_type]

    # second_type_index = random.randrange(total_probability)
    # create_second_type = True

    # for keys in range(1, len(get_second_type_dict)) :
    #     if second_type_index >= keys_range[keys-1] and create_second_type:
    #         index = keys_range.index(keys_range[keys])
    #         final_type_list.append(second_types_key[index]) #TODO ghost can't be alone
    #         create_second_type = False
    
    name = get_name(final_type_list)
    # name = 'toto'
    
    my_pokemon = Pokemon(name, hp, strength, defense_point, final_type_list)

    return my_pokemon

def save_pokemon():

    with open('multiple_type.json', 'r') as file:
        types = json.load(file)
        type_list = list(types.keys())

    for type in type_list:
        a_pokemon = create_pokemon(type)
        print(a_pokemon)

save_pokemon()
