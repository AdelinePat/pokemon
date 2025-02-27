import random, json, math
from .effortValue import EffortValue
from __settings__ import COEFFICIENT_PATH
from .evolution import Evolution

class Pokemon(Evolution):
    coefficient = json.load(open(COEFFICIENT_PATH))
    
    def __init__(self, name, original_name, hp, hp_max, strength, defense, type, level, speed, stage):
        super().__init__(name, stage, original_name, type, level)
        # self.__stage = Evolution(stage)
        self.__hp = hp
        self.__hp_max = hp_max
        self.__strength = strength
        self.__defense = defense
        self.__xp = 1
        self.__state = 'wild' # or domesticated
        self.__ev = EffortValue()
        self.__speed = speed
        # self.image_path = 'images/pokemons/' + self.name + '.png'
        self.pet_name = 'Jean-Luc'
    
    def pokemon_dict(self):
        return {
            "name" : self.name,
            "original_name" : self.get_original_name(),
            "pet_name" : self.pet_name,
            "hp_max" : self.get_hp_max(),
            "hp" : self.get_hp(),
            "xp" : self.get_xp(),
            "strength" : self.get_strength(),
            "defense" : self.get_defense(),
            "type" : self.type,
            "level" : self.get_level(),
            "speed" : self.get_speed(),
            "stage" : self.get_stage(),
            "ev" : self.get_effort_value().get_ev_dict(),
            "state" : self.get_state()
        }
    
    def set_pet_name(self, new_name):
        self.pet_name = new_name

    def get_effort_value(self):
        return self.__ev

    def get_hp(self):
        return self.__hp
    
    def set_hp(self, new_hp):
        self.__hp = new_hp
    
    def set_damage_hp(self, damage):
        self.__hp = self.get_hp() - damage

    def get_hp_max(self):
        return self.__hp_max
    
    def heal(self, heal):
        if self.get_hp() + heal <= self.get_hp_max():
            self.set_hp(self.get_hp() + heal)
        else:
            self.set_hp(self.get_hp_max())
    
    def set_hp_max(self, new_value):
        self.__hp_max = new_value
    
    def get_strength(self):
        return self.__strength
    
    def set_strength(self, new_value):
        self.__strength = new_value

    def get_defense(self):
        return self.__defense

    def set_defense(self, new_value):
        self.__defense = new_value
    
    def get_xp(self):
        return self.__xp
    
    def set_xp(self, new_value):
        self.__xp = new_value
    
    def get_speed(self):
        return self.__speed
    
    def set_speed(self, new_value):
        self.__speed = new_value
    
    def get_state(self):
        return self.__state
    
    def set_state(self, new_state):
        if new_state in ['wild', 'domesticated']:
            self.__state = new_state
    
    def get_state(self):
        return self.__state
        
    def get_attack_coefficient(self, attack_type, enemy):
        if len(enemy.type) == 2:
            list_coefficient = []
            
            for index in range(len(enemy.type)):
                a_coefficient = Pokemon.coefficient[attack_type][enemy.type[index]]
                list_coefficient.append(a_coefficient)
        
            coefficient = list_coefficient[0] * list_coefficient[1]
        else:
            coefficient = Pokemon.coefficient[attack_type][enemy.type[0]]

        return coefficient
    
    def attack_efficiency(self, chose_attack_type, enemy):
        coefficient = self.get_attack_coefficient(chose_attack_type, enemy)

        match coefficient:
            case 4:
                efficiency = "Super effective attack"

            case 2:
                efficiency = "Very effective attack"

            case 1:
                efficiency = "Effective attack"
            case 0.25 | 0.5:
                efficiency = "Not so effective attack"

            case 0:
                efficiency = "Impossible to attack"

        return coefficient, efficiency

    def check_evolution(self):
        is_evolving = self.evolve()
        # if is_evolving:
        #     print(f"{self.get_original_name().upper()} evolve into : {self.name.upper()}")
        #     self.set_hp_max(self.get_hp_max() + random.randrange(20, 35))
        #     self.set_defense(self.get_defense() + random.randrange(20, 35))
        #     self.set_strength(self.get_strength() + random.randrange(20, 35))
        #     self.set_speed(self.get_speed() + random.randrange(20, 35))

    
    def get_xp_gained(self, enemy):
        enemy_level = enemy.get_level()

        if enemy_level > self._level:
            if enemy.get_state() == 'wild':
                xp_gained = int(math.floor(100 * enemy.get_level() / 6))
            else:
                xp_gained = int(math.floor(100 * enemy.get_level() / 5))
        elif enemy_level < self._level:
            xp_gained = int(math.floor(100 * enemy.get_level() / 9))
        else:
            xp_gained = int(math.floor(100 * enemy.get_level() / 7))
        return xp_gained

    
    def update_xp(self, enemy):
        xp_gained = self.get_xp_gained(enemy)
        self.set_xp(self.get_xp() + xp_gained)
        self.__ev.update_ev(enemy, self)
        self.level_up(self)
        self.evolve()

    def __str__(self):
        if len(self.type) > 1:
            string = f"Pokemon : {self.name}\
                \Level : {self.get_level()}\
                \nXP : {self.get_xp()}\
                \nDefense : {self.get_defense()}\
                \nSpeed : {self.get_speed()}\
                \nHP max : {self.get_hp_max()}\
                \nHP: {self.get_hp()}\
                \nFirst type: {self.type[0]}\
                \nSecond type : {self.type[1]}\
                \nStrength : {self.get_strength()}\n"
        else:
            string = f"Pokemon : {self.name}\
                \nLevel : {self.get_level()}\
                \nXP : {self.get_xp()}\
                \nDefense : {self.get_defense()}\
                \nSpeed : {self.get_speed()}\
                \nHP max : {self.get_hp_max()}\
                \nHP: {self.get_hp()}\
                \nType : {self.type[0]}\
                \nStrength : {self.get_strength()}\n"
        return string + "\n"