# from .bag import Bag
from ..data_access.pokemon_pokedex_service import save_pokemon_to_pokedex
import random
from .fight_info import FightInfo
import math

class Fight:
    def __init__(self, pokemon1, pokemon2):
        self.first_pokemon = pokemon1
        self.second_pokemon = pokemon2
        self.fightinfo = FightInfo()
    
    def set_first_pokemon(self, new_pokemon):
        self.first_pokemon = new_pokemon

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
                    if critical < critical_rate:
                        efficency =  "Critical hit !!"
                        final_damage = damage * 2
                    else:
                        final_damage = damage
                else:
                    if enemy.get_hp() - damage < 0:
                        final_damage = enemy.get_hp()
                    else:
                        final_damage = 0
                    pokemon.update_xp(enemy)
            else:
                if critical < critical_rate:
                    efficency = "Critical hit !!"

                    final_damage = 20
                else:
                    final_damage = 1
                    if enemy.get_hp() - final_damage < 0:
                        final_damage = 0
                        
            final_damage = math.ceil(final_damage)
            enemy.set_damage_hp(final_damage)
        
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
            
            self.fightinfo.set_fail_flee_message()
            return False
        if miss == 1:
            self.fightinfo.set_fail_flee_message()

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

            if capture >= pokemon_enemy.get_hp():
                return "Success"
            else :

                self.bot_attack()

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