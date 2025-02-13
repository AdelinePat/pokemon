from models.bag import Bag
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
        # self.sac = Bag()

    def battle(self):
        pv1 = self.first_pokemon.get_hp()
        pv2 = self.second_pokemon.get_hp()
        print("================")
        print(self.first_pokemon)
        print(self.second_pokemon)

        while pv1 >= 0 and pv2 >= 0:
            pv1 = self.first_pokemon.get_hp()
            pv2 = self.second_pokemon.get_hp()
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
                while flag2:
                    try :
                        take = int(input(f"1-potion = {self.sac.get_potion()} 2-pokeball = {self.sac.get_pokeball()} 3-retour : "))
                        if choice >= 1 and choice <= 3:
                            flag2 = False
                        else : 
                            print("Valeur non correct")
                    except ValueError:
                        print("Choix invalide")
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
        print(self.first_pokemon,"\n")
        print(self.second_pokemon,"\n")
