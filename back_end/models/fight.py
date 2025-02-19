# from .bag import Bag
from ..data_access.pokemon_pokedex_service import save_pokemon_to_pokedex
import random
from .fight_info import FightInfo

class Fight:
    def __init__(self, pokemon1, pokemon2):
        self.first_pokemon = pokemon1
        self.second_pokemon = pokemon2
        self.fightinfo = FightInfo()
        # self.bag = Bag()

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
        

        damage = ((pokemon.get_strength() * coefficient) - enemy.get_defense())
        critical_rate = pokemon.get_speed() / 2
        critical = random.randint(1, 255)

        if miss ==1:
            efficency = "Missed attack..."
            final_damage = 0
        else:
            if damage > 0:
                if enemy.get_hp() - damage >= 0:
                    # if critical:
                    if critical < critical_rate:
                        efficency =  "Critical hit !!"
                        print("Coup critique !")
                        final_damage = damage * 2
                    else:
                        final_damage = damage
                else:
                    if enemy.get_hp() - damage < 0:
                        final_damage = enemy.get_hp()
                    else:
                        final_damage = 0
                    pokemon.update_xp(enemy)
                    # print(f"le pokemon {enemy.name} n'a plus de PV ! Vous avez gagné {pokemon.get_xp()} XP")
            else:
                # if critical:
                if critical < critical_rate:
                    efficency = "Critical hit !!"
                    print("Coup critique !")
                    final_damage = 20
                else:
                    final_damage = 1
                    if enemy.get_hp() - final_damage < 0:
                        final_damage = 0

            enemy.set_damage_hp(final_damage)
            print(f"DEGATS FINAUX : {final_damage}")            
            # print(f"{pokemon.name} a fait une attaque {attack_type}, {efficency}\
            #     \n Le pokemon {enemy.name} de type {enemy.type} en face a reçu {final_damage}, il lui reste : {enemy.get_hp()}")
        
        self.fightinfo.set_all_values(efficency, attack_type, final_damage)

    def is_player_first(self):
        if self.first_pokemon.get_speed() > self.second_pokemon.get_speed():
            return True
        else:
            return False
        
    def player_attack(self, attack_type):
        self.attack(self.first_pokemon, self.second_pokemon, attack_type)

    def bot_attack(self):
        if len(self.second_pokemon.type) == 2:
            attack_type = random.choice(self.second_pokemon.type)
        else:
            attack_type = self.second_pokemon.type[0]

        self.attack(self.second_pokemon, self.first_pokemon, attack_type)

    def run_away(self):
        miss = random.randint(1,7) #1-7
        if self.second_pokemon.get_state() == "domesticated":
            # print("Impossible de fuire dans un combat de dresseur")
            self.fightinfo.set_fail_flee_message()
            return False
        if miss == 1:
            self.fightinfo.set_fail_flee_message()
            # print("Vous n'avez pas reussi à prendre la fuite...")
            self.bot_attack()
            self.first_pokemon.get_hp()
            return False
        else :
            self.fightinfo.set_success_flee_message()
            return True

    def use_potion(self, pokemon, bag):
        if bag.get_potion() > 0:
            pokemon.heal(20)
            bag.set_potion(bag.get_potion() - 1)
            return None
        else:
            return "Back"

    def use_pokeball(self, player, bag, pokemon, pokemon_enemy):
        if bag.get_pokeball() > 0:
            capture = random.randint(1, 255)
            bag.set_pokeball(bag.get_pokeball() - 1)
            print("On utilise une pokeball")
            if capture <= pokemon_enemy.get_hp():
                return "Success"
            else :
                print("Le pokemon à reussi à s'échapper")
                self.bot_attack()
                print("=== Fin du tour ===")
            return "Fail"
        else:
            return "Back"

    def use(self, player, bag, bag_option, pokemon, pokemon_enemy):
        if bag_option == "Potions":
            pokemon.heal(20)
        else:
            if bag.get_pokeball() > 0:
                bag_option == "Pokeball"
                capture = random.randint(1, pokemon_enemy.get_hp())
                bag.set_pokeball(bag.get_pokeball() - 1)

                if capture <= 10:
                    save_pokemon_to_pokedex(player, pokemon)
                else :
                    self.bot_attack()
                    first = True

        # while flag2:
        #         try :
        #             take = int(input(f"1-potion = {self.bag.get_potion()} 2-pokeball = {self.bag.get_pokeball()} 3-rBack : "))
        #             if choice >= 1 and choice <= 3:
        #                 flag2 = False
        #             else : 
        #                 print("Valeur non correct")
        #         except ValueError:
        #             print("Choix invalide")
        #     if take == 1:
        #         if self.bag.get_potion() >= 1:
        #             if first == True:
        #                 self.first_pokemon.heal(20)
        #                 print("Vous avez soigné votre pokemon")
        #                 self.bag.potion -= 1
        #                 self.attack(self.second_pokemon, self.first_pokemon, self.second_pokemon.type[0])
        #                 hp1 = self.first_pokemon.get_hp()
        #                 print(self.first_pokemon)
        #                 print(self.second_pokemon)
        #                 if hp1 <= 0 or hp2 <= 0:
        #                     break
        #                 print("=== Fin du tour ===")
        #                 first = True
        #             elif first == False:
        #                 self.attack(self.second_pokemon, self.first_pokemon, self.second_pokemon.type[0])
        #                 hp1 = self.first_pokemon.get_hp()
        #                 if hp1 <= 0 or hp2 <= 0:
        #                     break
        #                 self.first_pokemon.heal(20)
        #                 print("Vous avez soigné votre pokemon")
        #                 self.bag.potion -= 1
        #                 print(self.first_pokemon)
        #                 print(self.second_pokemon)
        #                 print("=== Fin du tour ===")
        #                 first = True
        #     if take == 2:
        #         if self.second_pokemon.get_state() == "domesticated":
        #             print("Vous pouvez pas captuter le pokemon d'un autres dresseur")
        #         else:
        #             capture = random.randint(1, hp2)
        #             if capture <= 5:
        #                 print("1... 2... 3... Hop ! Le pokemon a était capturé !")
        #                 save_pokemon_to_pokedex("test", self.second_pokemon)
        #                 break
        #             else :
        #                 print("Le pokemon à reussi à s'échapper")
        #                 self.attack(self.second_pokemon, self.first_pokemon, self.second_pokemon.type[0])
        #                 hp1 = self.first_pokemon.get_hp()
        #                 if hp1 <= 0 or hp2 <= 0:
        #                     break
        #                 print(self.first_pokemon)
        #                 print(self.second_pokemon)
        #                 print("=== Fin du tour ===")
        #                 first = True
        #             self.bag.pokeball -= 1

    # def battle(self):
    #     hp1 = self.first_pokemon.get_hp()
    #     hp2 = self.second_pokemon.get_hp()
    #     print("================")
    #     print(self.first_pokemon)
    #     print(self.second_pokemon)

    #     while hp1 >= 0 and hp2 >= 0:
    #         hp1 = self.first_pokemon.get_hp()
    #         hp2 = self.second_pokemon.get_hp()
    #         miss = 0
    #         flag = True
    #         flag2 = True
    #         while flag:
    #             try:
    #                 choice= int(input("1-Attack 2-Fuite 3-Sac : "))
    #                 if choice >= 1 and choice <= 3:
    #                     flag = False
    #                 else : 
    #                     print("Valeur non correct")
    #             except ValueError:
    #                 print("Choix invalide")

    #         if self.first_pokemon.get_speed() > self.second_pokemon.get_speed():
    #             first = True
    #         else :
    #             first = False

    #         if choice == 1:
    #             if first == True:
    #                 #pokemon, enemy, attack_type
    #                 self.attack(self.first_pokemon, self.second_pokemon, self.first_pokemon.type[0])
    #                 # self.first_pokemon.attack(self.first_pokemon.type[0], self.second_pokemon)
    #                 hp2 = self.second_pokemon.get_hp()
    #                 if hp1 <= 0 or hp2 <= 0:
    #                     break
    #                 # self.second_pokemon.attack(self.second_pokemon.type[0], self.first_pokemon)
    #                 self.attack(self.second_pokemon, self.first_pokemon, self.second_pokemon.type[0])
    #                 print(self.first_pokemon)
    #                 print(self.second_pokemon)
    #                 hp1 = self.first_pokemon.get_hp()
    #                 if hp1 <= 0 or hp2 <= 0:
    #                     break
    #                 print("=== Fin du tour ===")
    #                 first = True
    #             else :
    #                 self.attack(self.second_pokemon, self.first_pokemon, self.second_pokemon.type[0])
    #                 # self.second_pokemon.attack(self.second_pokemon.type[0], self.first_pokemon)
    #                 hp1 = self.first_pokemon.get_hp()
    #                 if hp1 <= 0 or hp2 <= 0:
    #                     break
    #                 # self.first_pokemon.attack(self.first_pokemon.type[0], self.second_pokemon)
    #                 self.attack(self.first_pokemon, self.second_pokemon, self.first_pokemon.type[0])
    #                 print(self.first_pokemon)
    #                 print(self.second_pokemon)
    #                 hp2 = self.second_pokemon.get_hp()
    #                 if hp1 <= 0 or hp2 <= 0:
    #                     break
    #                 print("=== Fin du tour ===")
    #                 first = True
    #         elif choice == 2:
                # miss = random.randint(1, 7)
                # if self.second_pokemon.get_state() == "domesticated":
                #     print("Impossible de fuire dans un combat de dresseur")
                # if miss == 1:
                #     print("Vous n'avez pas reussi à prendre la fuite...")
                #     self.attack(self.second_pokemon, self.first_pokemon, self.second_pokemon.type[0])
                #     hp1 = self.first_pokemon.get_hp()
                #     if hp1 <= 0 or hp2 <= 0:
                #         break
                #     print(self.first_pokemon)
                #     print(self.second_pokemon)
                #     print("=== Fin du tour ===")
                #     first = True
                # else :
                #     print("Vous prenez la fuite...")
            #         break
            # elif choice == 3:
                # while flag2:
                #     try :
                #         take = int(input(f"1-potion = {self.bag.get_potion()} 2-pokeball = {self.bag.get_pokeball()} 3Back : "))
                #         if choice >= 1 and choice <= 3:
                #             flag2 = False
                #         else : 
                #             print("Valeur non correct")
                #     except ValueError:
                #         print("Choix invalide")
                # if take == 1:
                #     if self.bag.get_potion() >= 1:
                #         if first == True:
                #             self.first_pokemon.heal(20)
                #             print("Vous avez soigné votre pokemon")
                #             self.bag.potion -= 1
                #             self.attack(self.second_pokemon, self.first_pokemon, self.second_pokemon.type[0])
                #             hp1 = self.first_pokemon.get_hp()
                #             print(self.first_pokemon)
                #             print(self.second_pokemon)
                #             if hp1 <= 0 or hp2 <= 0:
                #                 break
                #             print("=== Fin du tour ===")
                #             first = True
                #         elif first == False:
                #             self.attack(self.second_pokemon, self.first_pokemon, self.second_pokemon.type[0])
                #             hp1 = self.first_pokemon.get_hp()
                #             if hp1 <= 0 or hp2 <= 0:
                #                 break
                #             self.first_pokemon.heal(20)
                #             print("Vous avez soigné votre pokemon")
                #             self.bag.potion -= 1
                #             print(self.first_pokemon)
                #             print(self.second_pokemon)
                #             print("=== Fin du tour ===")
                #             first = True
                # if take == 2:
                #     if self.second_pokemon.get_state() == "domesticated":
                #         print("Vous pouvez pas captuter le pokemon d'un autres dresseur")
                #     else:
                #         capture = random.randint(1, hp2)
                #         if capture <= 5:
                #             print("1... 2... 3... Hop ! Le pokemon a était capturé !")
                #             save_pokemon_to_pokedex("test", self.second_pokemon)
                #             break
                #         else :
                #             print("Le pokemon à reussi à s'échapper")
                #             self.attack(self.second_pokemon, self.first_pokemon, self.second_pokemon.type[0])
                #             hp1 = self.first_pokemon.get_hp()
                #             if hp1 <= 0 or hp2 <= 0:
                #                 break
                #             print(self.first_pokemon)
                #             print(self.second_pokemon)
                #             print("=== Fin du tour ===")
                #             first = True
                #         self.bag.pokeball -= 1
        # print(self.first_pokemon,"\n")
        # print(self.second_pokemon,"\n")
