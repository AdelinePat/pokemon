from create_pokemon import save_pokemon
import random
#print(first_pokemon.get_hp())

class Fight:
    def __init__(self):
        self.all_pokemons = save_pokemon()
        self.first_pokemon = random.choice(self.all_pokemons)
        self.second_pokemon = random.choice(self.all_pokemons)
        while self.first_pokemon == self.second_pokemon:
            self.second_pokemon = random.choice(self.all_pokemons)

    def battle(self):
        pv1 = self.first_pokemon.get_hp()
        pv2 = self.second_pokemon.get_hp()
        print("================")
        print(self.first_pokemon)
        print(self.second_pokemon)

        while pv1 >= 0 and pv2 >= 0:
            pv1 = self.first_pokemon.get_hp()
            pv2 = self.second_pokemon.get_hp()
            choice= int(input("1-Attack 2-Fuite : "))
            if self.first_pokemon.get_speed() > self.second_pokemon.get_speed():
                first = True
            else :
                first = False 

            if choice == 1:
                if first == True:
                    self.first_pokemon.attack(self.first_pokemon.type[0], self.second_pokemon)
                    pv2 = self.second_pokemon.get_hp()
                    if pv1 <= 0 or pv2 <= 0:
                        break
                    self.second_pokemon.attack(self.second_pokemon.type[0], self.first_pokemon)
                    print(self.first_pokemon)
                    print(self.second_pokemon)
                    pv1 = self.first_pokemon.get_hp()
                    if pv1 <= 0 or pv2 <= 0:
                        break
                    print("=== Fin du tour ===")
                    first = True
                else : 
                    self.second_pokemon.attack(self.second_pokemon.type[0], self.first_pokemon)
                    pv1 = self.first_pokemon.get_hp()
                    if pv1 <= 0 or pv2 <= 0:
                        break
                    self.first_pokemon.attack(self.first_pokemon.type[0], self.second_pokemon)
                    print(self.first_pokemon)
                    print(self.second_pokemon)
                    pv2 = self.second_pokemon.get_hp()
                    if pv1 <= 0 or pv2 <= 0:
                        break
                    print("=== Fin du tour ===")
                    first = True
            elif choice == 2:
                print("Vous prenez la fuite...")
                break

test = Fight()
test.battle()
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