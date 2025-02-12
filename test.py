from create_pokemon import save_pokemon
from pokemon import Sac
import random
#print(first_pokemon.get_hp())

class Fight:
    def __init__(self):
        self.all_pokemons = save_pokemon()
        self.first_pokemon = random.choice(self.all_pokemons)
        self.second_pokemon = random.choice(self.all_pokemons)
        while self.first_pokemon == self.second_pokemon:
            self.second_pokemon = random.choice(self.all_pokemons)
        self.sac = Sac()

    def battle(self):
        pv1 = self.first_pokemon.get_hp()
        pv2 = self.second_pokemon.get_hp()
        print("================")
        print(self.first_pokemon)
        print(self.second_pokemon)

        while pv1 >= 0 and pv2 >= 0:
            pv1 = self.first_pokemon.get_hp()
            pv2 = self.second_pokemon.get_hp()
            choice= int(input("1-Attack 2-Fuite 3-Sac : "))
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
            elif choice == 3:
                take = int(input(f"1-potion = {self.sac.get_potion()} 2-pokeball = {self.sac.get_pokeball()} 3-retour : "))
                if take == 1:
                    if self.sac.get_potion() >= 1:
                        if first == True:
                            self.first_pokemon.heal(20)
                            print("Vous avez soigné votre pokemon")
                            self.sac.potion -= 1
                            self.second_pokemon.attack(self.second_pokemon.type[0], self.first_pokemon)
                            pv1 = self.first_pokemon.get_hp()
                            print(self.first_pokemon)
                            print(self.second_pokemon)
                            if pv1 <= 0 or pv2 <= 0:
                                break
                            print("=== Fin du tour ===")
                            first = True
                        elif first == False:
                            self.second_pokemon.attack(self.second_pokemon.type[0], self.first_pokemon)
                            pv1 = self.first_pokemon.get_hp()
                            if pv1 <= 0 or pv2 <= 0:
                                break
                            self.first_pokemon.heal(20)
                            print("Vous avez soigné votre pokemon")
                            self.sac.potion -= 1
                            print(self.first_pokemon)
                            print(self.second_pokemon)
                            print("=== Fin du tour ===")
                            first = True
                if take == 2:
                    print("en cours")
                    self.sac.pokeball -= 1

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