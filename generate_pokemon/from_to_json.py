import json, os, random
from models.pokemon import Pokemon
from generate_pokemon.create_pokemon import create_world_pokemons
from __settings__ import WORLD_POKEMON_PATH

def save_pokemon():

    all_pokemons = create_world_pokemons()
    pokemons_dict_list = []
    for each_pokemon in all_pokemons:
        a_pokemon = each_pokemon.pokemon_dict()
        pokemons_dict_list.append(a_pokemon)
        
    if not os.path.exists(WORLD_POKEMON_PATH):
        with open(WORLD_POKEMON_PATH, "w", encoding="UTF-8") as file:
            json.dump({}, file)
    with open(WORLD_POKEMON_PATH, "w") as file:
        json.dump(pokemons_dict_list, file, indent=4)

def to_json(my_pokemon):
   
    # pokemons_dict_list = []
    # for each_pokemon in all_pokemons:
    #     a_pokemon = each_pokemon.pokemon_dict()
    #     pokemons_dict_list.append(a_pokemon)

    with open(WORLD_POKEMON_PATH, "r") as file:
        pokemons_dict_list = json.load(file)

    pokemons_dict_list.append(my_pokemon)

    with open(WORLD_POKEMON_PATH, "w") as file:
        json.dump(pokemons_dict_list, file, indent=4)

def from_json_random_pick():
    with open(WORLD_POKEMON_PATH, "r") as file:
        pokemons = json.load(file)
    
    a_pokemon = random.choice(pokemons)
    pokemons.pop(pokemons.index(a_pokemon))

    with open(WORLD_POKEMON_PATH, "w") as file:
        json.dump(pokemons, file, indent=4)

# name, original_name, hp, strength, defense, type, level, speed, stage
    my_pokemon = Pokemon(a_pokemon['name'], a_pokemon['original_name'], a_pokemon['hp'],\
                        a_pokemon['strength'], a_pokemon['defense'], a_pokemon['type'],\
                        a_pokemon['level'], a_pokemon['speed'], a_pokemon['stage'])
    
    my_pokemon.get_effort_value().set_ev_hp(a_pokemon['ev']['hp'])
    my_pokemon.get_effort_value().set_ev_strength(a_pokemon['ev']['strength'])
    my_pokemon.get_effort_value().set_ev_defense(a_pokemon['ev']['defense'])
    my_pokemon.get_effort_value().set_ev_speed(a_pokemon['ev']['speed'])
    my_pokemon.get_effort_value().set_ev_xp(a_pokemon['ev']['xp'])
    my_pokemon.set_pet_name(a_pokemon['pet_name'])

    return my_pokemon


# ev = {
#             "hp" : self.get_ev_hp(),
#             "strength" : self.get_ev_strength(),
#             "defense" : self.get_ev_defense(),
#             "speed" : self.get_ev_speed(),
#             "xp" : self.get_ev_xp()
#         }
