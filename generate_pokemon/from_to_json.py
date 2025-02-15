import json, os, random
from models.pokemon import Pokemon
from generate_pokemon.create_pokemon import create_world_pokemons
from __settings__ import WORLD_POKEMON_PATH, PLAYER_POKEDEX

def generate_pokemons_dict():
    name_list = ["Baptiste", "Michel", "Pierre", "Paul", "Louis", "François", "Claude", "Christophe", "Charles", "Luc", "Marie", "Sébastien", "Daniel", "Eric", "Robert", "Joseph", "Thibault", "Adeline", "Florence", "Eltigani", "Jolyne", "Mehdi", "Vanessa", "Noa", "Armelle", "Morgan", "Alicia", "Ryan", "Ryhad", "Emilie", "Hubert", "Vincent", "Roger", "David", "Thierry", "Sarah", "Hélène"]
    all_pokemons = create_world_pokemons()
    pokemons_dict_list = []
    for index, each_pokemon in enumerate(all_pokemons):
        each_pokemon.set_pet_name("Jean-" + name_list[index])
        a_pokemon = each_pokemon.pokemon_dict()
        pokemons_dict_list.append(a_pokemon)
    
    return pokemons_dict_list

def save_world_pokemons(pokemons_dict_list):
    if not os.path.exists(WORLD_POKEMON_PATH):
        with open(WORLD_POKEMON_PATH, "w", encoding="UTF-8") as file:
            json.dump({}, file)
    with open(WORLD_POKEMON_PATH, "w") as file:
        json.dump(pokemons_dict_list, file, indent=4)

def save_wild_pokemon(my_pokemon):
    with open(WORLD_POKEMON_PATH, "r") as file:
        pokemons_dict_list = json.load(file)
    
    my_pokemon.set_state('wild')
    pokemons_dict_list.append(my_pokemon.pokemon_dict())

    with open(WORLD_POKEMON_PATH, "w") as file:
        json.dump(pokemons_dict_list, file, indent=4)

def get_random_wild_pokemon():
    with open(WORLD_POKEMON_PATH, "r") as file:
        pokemons = json.load(file)

    if not pokemons:
        pokemons = generate_pokemons_dict()

    a_pokemon = random.choice(pokemons)
    pokemons.pop(pokemons.index(a_pokemon))

    save_world_pokemons(pokemons)

    # with open(WORLD_POKEMON_PATH, "w") as file:
    #     json.dump(pokemons, file, indent=4)

# name, original_name, hp, strength, defense, type, level, speed, stage
    my_pokemon = instanciate_pokemon(a_pokemon)

    return my_pokemon

def instanciate_pokemon(pokemon):
    my_pokemon = Pokemon(pokemon['name'], pokemon['original_name'], pokemon['hp'],\
                        pokemon['strength'], pokemon['defense'], pokemon['type'],\
                        pokemon['level'], pokemon['speed'], pokemon['stage'])
    
    my_pokemon.set_xp(pokemon['xp'])
    my_pokemon.set_state(pokemon['state'])
    my_pokemon.get_effort_value().set_ev_hp(pokemon['ev']['hp'])
    my_pokemon.get_effort_value().set_ev_strength(pokemon['ev']['strength'])
    my_pokemon.get_effort_value().set_ev_defense(pokemon['ev']['defense'])
    my_pokemon.get_effort_value().set_ev_speed(pokemon['ev']['speed'])
    my_pokemon.get_effort_value().set_ev_xp(pokemon['ev']['xp'])

    my_pokemon.set_pet_name(pokemon['pet_name'])

    return my_pokemon


def to_player_pokedex(player, pokemon):
    if not os.path.exists(PLAYER_POKEDEX):
        with open(PLAYER_POKEDEX, "w", encoding="UTF-8") as file:
            json.dump({}, file)
    
    with open(PLAYER_POKEDEX, "r") as file:
        pokemons_dictionary = json.load(file)

    pokemon.set_state('domesticated')
    pokemons_dictionary[player].update({pokemon.pet_name : pokemon.pokemon_dict()})

    # pokemons_list.append(pokemon_dictionary)

    with open(PLAYER_POKEDEX, "w") as file:
        json.dump(pokemons_dictionary, file, indent=4)

def get_pokemon_from_pokedex(pokemon_pet_name):
    with open(PLAYER_POKEDEX, "r") as file:
        pokemons = json.load(file)

    for pokemon in pokemons:
        if pokemon == pokemon_pet_name:
            my_pokemon = instanciate_pokemon(pokemons[pokemon])
            return my_pokemon

def get_petnames_from_pokedex():
    with open(PLAYER_POKEDEX, "r") as file:
        pokemons_dictionary = json.load(file)

    pokemons_names = list(pokemons_dictionary.keys())

    return pokemons_names