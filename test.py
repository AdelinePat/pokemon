from create_pokemon import save_pokemon
import random
from pokemon import Pokemon

# all_pokemons = save_pokemon()
# # print(all_pokemons)

# first_pokemon = random.choice(all_pokemons)
# second_pokemon = random.choice(all_pokemons)

# while first_pokemon == second_pokemon:
#     second_pokemon = random.choice(all_pokemons)

# print(first_pokemon)
# print(second_pokemon)
# print("=== TOUR 1 ===")
# first_pokemon.attack(first_pokemon.type[0], second_pokemon)
# second_pokemon.attack(second_pokemon.type[0], first_pokemon)
# print(first_pokemon)
# print(second_pokemon)
# print("\n=== TOUR 2 ===")
# first_pokemon.attack(first_pokemon.type[0], second_pokemon)
# second_pokemon.attack(second_pokemon.type[0], first_pokemon)
# print(first_pokemon)
# print(second_pokemon)
# print("\n=== TOUR 3 ===")
# print(first_pokemon)
# print(second_pokemon)
# first_pokemon.attack(first_pokemon.type[0], second_pokemon)
# print(first_pokemon)
# print(second_pokemon)
# second_pokemon.attack(second_pokemon.type[0], first_pokemon)
# print(first_pokemon)
# print(second_pokemon)

# print(first_pokemon)
# print("\n=== TOUR 4 ===")
# first_pokemon.attack(first_pokemon.type[0], second_pokemon)
# print(second_pokemon)
# second_pokemon.attack(second_pokemon.type[0], first_pokemon)
# print(first_pokemon)
# print("\n=== TOUR 5 ===")
# first_pokemon.attack(first_pokemon.type[0], second_pokemon)
# print(second_pokemon)
# second_pokemon.attack(second_pokemon.type[0], first_pokemon)
# print(first_pokemon)

# magikarp = Pokemon('MAGIKARP', 'magikarp', 18, 12, 10, ['water'], 1, 29, 1)
# print(magikarp)
# voltorb = Pokemon('VOLTORB','voltorb', 20, 24, 14, ['electric', 'grass'], 1, 16, 1)
# print(voltorb)

# print("=== PREMIER TOUR ===\n")
# magikarp.attack(magikarp.type[0],  voltorb)
# print(voltorb)

# voltorb.attack(voltorb.type[0], magikarp)
# print(voltorb)

# autre test
# meowth = Pokemon('meowth', 14, 10, 15, ['steel'], 1, 20)
# print(meowth)
# mew = Pokemon('mew', 18, 20, 22, ['psychic'], 1, 18)
# print(mew)


# print("=== PREMIER TOUR ===\n")
# meowth.attack(meowth.type[0],  mew)
# print(mew)

# mew.attack(mew.type[0], meowth)
# print(meowth)

# print("=== SECOND TOUR ===\n")
# meowth.attack(meowth.type[0],  mew)
# print(mew)

# print("\n", meowth)
# self, name, original_name, hp, strength, defense, type, level, speed, stage
tauros = Pokemon('tauros', 'tauros', 78, 73, 52, ['normal'], 16, 10, 2)
seaking = Pokemon('seaking', 'goldeen', 73, 62, 62, ['water'], 17, 10, 2)

print(seaking)
print(tauros)
print("TOUR 1")
seaking.attack(seaking.type[0], tauros)
tauros.attack(tauros.type[0], seaking)
print(seaking)
print(tauros)
print("TOUR 2")
seaking.attack(seaking.type[0], tauros)
tauros.attack(tauros.type[0], seaking)
print(seaking)
print(tauros)