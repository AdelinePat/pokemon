from models.bag import Bag
import random

class Fight:
    def __init__(self, pokemon1, pokemon2):
        self.first_pokemon = pokemon1
        self.second_pokemon = pokemon2
        self.bag = Bag()
        # self.all_pokemons = create_world_pokemons() #TODO edit this function
        # self.first_pokemon = random.choice(self.all_pokemons)
        # self.second_pokemon = random.choice(self.all_pokemons)

        # ONE SHOT TEST
        # self.first_pokemon = Pokemon('Clefable', 'Clefairy', 49, 60, 57, ['fairy'], 13, 46, 2)
        # self.second_pokemon = Pokemon('Raichu', 'Pikachu', 80, 59, 75, ['electric'], 17, 57, 2)
        # LEVEL UP  TEST

        # self.second_pokemon = Pokemon('Clefable', 'Clefairy', 49, 60, 57, ['fairy'], 1, 46, 2)
        # self.first_pokemon = Pokemon('Raichu', 'Pikachu', 80, 80, 75, ['electric'], 1, 57, 2)

        # while self.first_pokemon == self.second_pokemon:
        #     self.second_pokemon = random.choice(self.all_pokemons)
        # self.bag = Bag()

    def attack(self, pokemon, enemy, attack_type):
        coefficient, efficency = pokemon.attack_efficiency(attack_type, enemy)
        miss = random.randint(1, 8)
        
        damage = (pokemon.get_strength() * coefficient) - enemy.get_defense()
        T = pokemon.get_speed() / 2
        critical = random.randint(1, 255)

        if miss == 1:
            print("l'attaque à était raté...")
        else:
            if damage > 0:
                if enemy.get_hp() - damage >= 0:
                    if critical < T:
                        print("Coup critique !")
                        final_damage = damage * 2
                    else:
                        final_damage = damage
                else:
                    final_damage = enemy.get_hp()
                    pokemon.update_xp(enemy)
                    print(f"le pokemon {enemy.name} n'a plus de PV ! Vous avez gagné {pokemon.get_xp()} XP")
            else:
                final_damage = 1
                if enemy.get_hp() - final_damage < 0:
                    final_damage = 0

            enemy.set_damage_hp(final_damage)

            print(f"{pokemon.name} a fait une attaque {attack_type}, {efficency}\
                \n Le pokemon {enemy.name} de type {enemy.type} en face a reçu {final_damage}, il lui reste : {enemy.get_hp()}")


    def battle(self):
        hp1 = self.first_pokemon.get_hp()
        hp2 = self.second_pokemon.get_hp()
        print("================")
        print(self.first_pokemon)
        print(self.second_pokemon)

        while hp1 >= 0 and hp2 >= 0:
            hp1 = self.first_pokemon.get_hp()
            hp2 = self.second_pokemon.get_hp()
            miss = 0
            flag = True
            flag2 = True
            while flag:
                try:
                    choice= int(input("1-Attack 2-Fuite 3-Sac : "))
                    if choice >= 1 and choice <= 3:
                        flag = False
                    else : 
                        print("Valeur non correct")
                except ValueError:
                    print("Choix invalide")

            if self.first_pokemon.get_speed() > self.second_pokemon.get_speed():
                first = True
            else :
                first = False 

            if choice == 1:
                if first == True:
                    #pokemon, enemy, attack_type
                    self.attack(self.first_pokemon, self.second_pokemon, self.first_pokemon.type[0])
                    # self.first_pokemon.attack(self.first_pokemon.type[0], self.second_pokemon)
                    hp2 = self.second_pokemon.get_hp()
                    if hp1 <= 0 or hp2 <= 0:
                        break
                    # self.second_pokemon.attack(self.second_pokemon.type[0], self.first_pokemon)
                    self.attack(self.second_pokemon, self.first_pokemon, self.second_pokemon.type[0])
                    print(self.first_pokemon)
                    print(self.second_pokemon)
                    hp1 = self.first_pokemon.get_hp()
                    if hp1 <= 0 or hp2 <= 0:
                        break
                    print("=== Fin du tour ===")
                    first = True
                else :
                    self.attack(self.second_pokemon, self.first_pokemon, self.second_pokemon.type[0])
                    # self.second_pokemon.attack(self.second_pokemon.type[0], self.first_pokemon)
                    hp1 = self.first_pokemon.get_hp()
                    if hp1 <= 0 or hp2 <= 0:
                        break
                    # self.first_pokemon.attack(self.first_pokemon.type[0], self.second_pokemon)
                    self.attack(self.first_pokemon, self.second_pokemon, self.first_pokemon.type[0])
                    print(self.first_pokemon)
                    print(self.second_pokemon)
                    hp2 = self.second_pokemon.get_hp()
                    if hp1 <= 0 or hp2 <= 0:
                        break
                    print("=== Fin du tour ===")
                    first = True
            elif choice == 2:
                miss = random.randint(1, 7)
                if self.second_pokemon.get_state() == "domesticated":
                    print("Impossible de fuire dans un combat de dresseur")
                if miss == 1:
                    print("Vous n'avez pas reussi à prendre la fuite...")
                    self.second_pokemon.attack(self.second_pokemon.type[0], self.first_pokemon)
                    hp1 = self.first_pokemon.get_hp()
                    if hp1 <= 0 or hp2 <= 0:
                        break
                    print(self.first_pokemon)
                    print(self.second_pokemon)
                    print("=== Fin du tour ===")
                    first = True
                else :
                    print("Vous prenez la fuite...")
                    break
            elif choice == 3:
                while flag2:
                    try :
                        take = int(input(f"1-potion = {self.bag.get_potion()} 2-pokeball = {self.bag.get_pokeball()} 3-retour : "))
                        if choice >= 1 and choice <= 3:
                            flag2 = False
                        else : 
                            print("Valeur non correct")
                    except ValueError:
                        print("Choix invalide")
                if take == 1:
                    if self.bag.get_potion() >= 1:
                        if first == True:
                            self.first_pokemon.heal(20)
                            print("Vous avez soigné votre pokemon")
                            self.bag.potion -= 1
                            self.second_pokemon.attack(self.second_pokemon.type[0], self.first_pokemon)
                            hp1 = self.first_pokemon.get_hp()
                            print(self.first_pokemon)
                            print(self.second_pokemon)
                            if hp1 <= 0 or hp2 <= 0:
                                break
                            print("=== Fin du tour ===")
                            first = True
                        elif first == False:
                            self.second_pokemon.attack(self.second_pokemon.type[0], self.first_pokemon)
                            hp1 = self.first_pokemon.get_hp()
                            if hp1 <= 0 or hp2 <= 0:
                                break
                            self.first_pokemon.heal(20)
                            print("Vous avez soigné votre pokemon")
                            self.bag.potion -= 1
                            print(self.first_pokemon)
                            print(self.second_pokemon)
                            print("=== Fin du tour ===")
                            first = True
                if take == 2:
                    print("en cours")
                    self.bag.pokeball -= 1
        print(self.first_pokemon,"\n")
        print(self.second_pokemon,"\n")
