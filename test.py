from create_pokemon import save_pokemon
import random

all_pokemons = save_pokemon()
#print(all_pokemons)

first_pokemon = random.choice(all_pokemons)
second_pokemon = random.choice(all_pokemons)

while first_pokemon == second_pokemon:
    second_pokemon = random.choice(all_pokemons)

print(first_pokemon)
print(second_pokemon)
#print(first_pokemon.get_hp())

pv1 = first_pokemon.get_hp()
pv2 = second_pokemon.get_hp()
first = True

while pv1 >= 0 and pv2 >= 0:
    pv1 = first_pokemon.get_hp()
    pv2 = second_pokemon.get_hp()
    if first == True:
        choix = int(input("1-Attack 2-Fuite"))
        if choix == 1:
            first_pokemon.attack(first_pokemon.type[0], second_pokemon)
            print(second_pokemon)
            pv2 = second_pokemon.get_hp()
            first = False
        elif choix == 2:
            print("Vous prenez la fuite...")
            break
        if pv1 <= 0 or pv2 <= 0:
            break
    else : 
        second_pokemon.attack(second_pokemon.type[0], first_pokemon)
        print(first_pokemon)
        if pv1 <= 0 or pv2 <= 0:
            break
        else :
            print("=== Fin du tour ===")
            first = True
'''
first_pokemon.attack(first_pokemon.type[0], second_pokemon)
print(second_pokemon)
second_pokemon.attack(second_pokemon.type[0], first_pokemon)
print(first_pokemon)
print("=== Fin du tour ===")
first_pokemon.attack(first_pokemon.type[0], second_pokemon)
print(second_pokemon)
second_pokemon.attack(second_pokemon.type[0], first_pokemon)
print(first_pokemon)'''