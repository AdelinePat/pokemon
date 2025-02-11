from create_pokemon import save_pokemon
import random

all_pokemons = save_pokemon()
print(all_pokemons)

first_pokemon = random.choice(all_pokemons)
second_pokemon = random.choice(all_pokemons)

while first_pokemon == second_pokemon:
    second_pokemon = random.choice(all_pokemons)

print(first_pokemon)
print(second_pokemon)

first_pokemon.attack(first_pokemon.type[0], second_pokemon)
print(second_pokemon)
second_pokemon.attack(second_pokemon.type[0], first_pokemon)
print(first_pokemon)
print("=== Fin du tour ===")
first_pokemon.attack(first_pokemon.type[0], second_pokemon)
print(second_pokemon)
second_pokemon.attack(second_pokemon.type[0], first_pokemon)
print(first_pokemon)