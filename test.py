from generate_pokemon.create_pokemon import create_world_pokemons
import random
from models.pokemon import Pokemon


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

# self, name, original_name, hp, strength, defense, type, level, speed, stage

# first_pokemon = Pokemon('Tauros', 'Tauros', 78, 73, 52, ['normal'], 16, 10, 2)
# second_pokemon = Pokemon('Seaking', 'Goldeen', 73, 62, 62, ['water'], 17, 10, 2)

#  name, original_name, hp, strength, defense, type, level, speed, stage

# Bulbasaur = Pokemon("Bulbasaur", "Bulbasaur", 89, 79, 100, ['grass', 'poison'], 17, 14, 1)
# Charmander = Pokemon("Charmander", "Charmander", 56, 15, 15, ['fire'], 8, 13, 1)
# print(Charmander)
# Bulbasaur.set_xp(1000)
# Charmander.set_xp(514)

def fight_loop_test():
    first_pokemon, second_pokemon = get_pokemons()
    alive = True
    i = 1
    while alive:
        print(f"=== Tour n°{i}")
        if first_pokemon.get_speed() > second_pokemon.get_speed():
            first_pokemon.attack(first_pokemon.type[0], second_pokemon)
            alive = check_alive(first_pokemon, second_pokemon)
            if alive:
                second_pokemon.attack(second_pokemon.type[0], first_pokemon)
                alive = check_alive(first_pokemon, second_pokemon)

        if first_pokemon.get_speed() < second_pokemon.get_speed():
            second_pokemon.attack(second_pokemon.type[0], first_pokemon)
            alive = check_alive(first_pokemon, second_pokemon)
            if alive:
                first_pokemon.attack(first_pokemon.type[0], second_pokemon)
                alive = (first_pokemon, second_pokemon)

        if first_pokemon.get_speed() == second_pokemon.get_speed():
            pokemons = [first_pokemon, second_pokemon]
            first = random.choice(pokemons)
            pokemons.pop(pokemons.index(first))
            first.attack(first.type[0], pokemons[0])
            alive = (first_pokemon, second_pokemon)
            if alive:
                pokemons[0].attack(pokemons[0].type[0], first)
                alive = (first_pokemon, second_pokemon)
                
        print(first_pokemon, "\n")
        print(second_pokemon, "\n\n")
        i +=1

# fight_loop_test()

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


    

test_evolution()
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