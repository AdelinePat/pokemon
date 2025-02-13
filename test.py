from models.fight import Fight
import random
from generate_pokemon.create_pokemon import create_world_pokemons
from generate_pokemon.from_to_json import save_pokemon, from_json_random_pick, to_json
from models.pokemon import Pokemon
#print(first_pokemon.get_hp())

# ONE SHOT TEST
first_pokemon = Pokemon('Clefable', 'Clefairy', 49, 60, 57, ['fairy'], 13, 46, 2)
second_pokemon = Pokemon('Raichu', 'Pikachu', 80, 59, 75, ['electric'], 17, 57, 2)
# LEVEL UP  TEST

# second_pokemon = Pokemon('Clefable', 'Clefairy', 49, 60, 57, ['fairy'], 1, 46, 2)
# first_pokemon = Pokemon('Raichu', 'Pikachu', 80, 80, 75, ['electric'], 1, 57, 2)

test = Fight(first_pokemon, second_pokemon)
# test.battle()

def check_alive(first_pokemon, second_pokemon):
    if first_pokemon.get_hp() == 0 or second_pokemon.get_hp() == 0:
        print("fin du combat")
        alive = False
    else:
        alive = True
    return alive

def get_pokemons():
    all_pokemons = create_world_pokemons()
    # print(all_pokemons)

    first_pokemon = random.choice(all_pokemons)
    second_pokemon = random.choice(all_pokemons)

    while first_pokemon == second_pokemon:
        second_pokemon = random.choice(all_pokemons)

    return first_pokemon, second_pokemon

def test_evolution():
    # geodude = Pokemon('Geodude', 'Geodude', 10, 11, 9, ["rock", 'electric'], 25, 10, 1)
    # print(geodude)
    # geodude.pet_name = "geo"
    # # geodude.set_stage(1)
    # geodude.evolve()
    # print(geodude)
    # geodude.set_xp(50000)
    # geodude.set_level_up(geodude, 11)
    # geodude.evolve()
    # print(geodude)

    eevee = Pokemon('Eevee', 'Eevee', 10, 11, 9, ["normal"], 25, 10, 1)
    print(eevee)
    eevee.pet_name = "geo"
    # eevee.set_stage(1)
    eevee.evolve()
    print(eevee)

# test_evolution()
    # if Bulbasaur.get_hp() == 0 or Charmander.get_hp() == 0:
    #     print("fin du combat")
    #     alive = False

# Charmander.attack(Charmander.type[0], Bulbasaur)
# print(Bulbasaur)
# print(Charmander)

# print("\n")
# Charmander.set_stage(2)
# Charmander.evolve()
# print(Charmander)



# self, name, original_name, hp, strength, defense, type, level, speed, stage
# Pokemon : Clefable
# Niveau : 13
# XP : 1
# Défense : 57
# Rapidité : 46
# PV max : 49
# PV actuel : 49
# Type : fairy
# Force : 60


# Pokemon : Raichu
# Niveau : 17
# XP : 1
# Défense : 75
# Rapidité : 57
# PV max : 80
# PV actuel : 80
# Type : electric
# Force : 59

# save_pokemon()

poke = from_json_random_pick()
print(poke)
print(poke.get_xp())
poke.set_xp(poke.get_xp() + 100)
print(poke)

to_json(poke)