import random, json, math
from models.effortValue import EffortValue
from __settings__ import COEFFICIENT_PATH
from models.evolution import Evolution

class Pokemon(Evolution):
    coefficient = json.load(open(COEFFICIENT_PATH))
    def __init__(self, name, original_name, hp, strength, defense, type, level, speed, stage):
        super().__init__(name, stage, original_name, type, level)
        # self.__stage = Evolution(stage)
        self.__hp = hp
        self.__hp_max = hp
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
            "hp" : self.get_hp(),
            "xp" : self.get_xp(),
            "strength" : self.get_strength(),
            "defense" : self.get_defense(),
            "type" : self.type,
            "level" : self.get_level(),
            "speed" : self.get_speed(),
            "stage" : self.get_stage(),
            "ev" : self.get_effort_value().get_ev_dict()
        }

    def get_effort_value(self):
        return self.__ev

    def get_hp(self):
        return self.__hp
    
    def set_damage_hp(self, damage):
        self.__hp = self.get_hp() - damage

    def get_hp_max(self):
        return self.__hp_max
    
    def heal(self, heal):
        self.__hp = self.__hp + heal
        if self.__hp > self.__hp_max:
            cap = self.__hp - self.__hp_max
            self.__hp = self.__hp - cap
    
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
    
    def attack(self, attack_type, enemy):
        coefficient, efficency = self.attack_efficiency(attack_type, enemy)
        # coefficient, efficency = self.update_xp(enemy)
        
        damage = (self.get_strength() * coefficient) - enemy.get_defense()
        enemy_hp = enemy.get_hp()
        T = self.get_speed() / 2
        critical = random.randint(1, 255)

        # damage_defense = damage - enemy.get_defense()
        if damage > 0:
            if enemy.get_hp() - damage >= 0:
                if critical < T:
                    print("Coup critique !")
                    final_damage = damage * 2

                    # if enemy.get_hp() - final_damage >= 0:
                    #     enemy.set_damage_hp(final_damage)
                    # else:
                    #     enemy.set_damage_hp(enemy.get_hp())
                else:
                    final_damage = damage
                # enemy.set_damage_hp(final_damage)
            else:
                # enemy.set_damage_hp(enemy_hp)
                final_damage = enemy.get_hp()
                print(f"le pokemon {enemy.name} n'a plus de PV !")
        else:
            final_damage = 1
            if enemy.get_hp() - final_damage < 0:
                final_damage = 0
        enemy.set_damage_hp(final_damage)

        print(f"{self.name} a fait une attaque {attack_type}, {efficency}\
              \n Le pokemon {enemy.name} de type {enemy.type} en face a reçu {final_damage}, il lui reste : {enemy.get_hp()}")

        # coefficient, efficency = self.attack_efficiency(chose_attack_type, enemy)
        
        # damage = self.get_strength() * coefficient
        # enemy_hp = enemy.get_hp()
        # if enemy_hp - damage >= 0:
        #     enemy.set_damage_hp(damage)
        # else:
        #     enemy.set_damage_hp(enemy_hp)
            
        # print(f"{self.name} a fait une attaque {chose_attack_type}, {efficency}\
        #       \n Le pokemon {enemy.name} de type {enemy.type} en face a reçu {damage}, il lui reste : {enemy.get_hp()}")
        
        # if enemy.get_hp() == 0:
        #     print(f"le pokemon {enemy.name} n'a plus de PV !")
        #     self.update_xp(enemy)
        #     self.check_evolution()
        
        self.level_up(self)

    def attack_efficiency(self, chose_attack_type, enemy):
        coefficient = self.get_attack_coefficient(chose_attack_type, enemy)

        match coefficient:
            case 4:
                efficency = "attaque ultra efficace"
            case 2:
                efficency = "attaque très efficace"
            case 1:
                efficency = "attaque efficace"
            case 0.5:
                efficency = "attaque peu efficace"
            case 0:
                efficency = "impossible d'attaquer"
        
        return coefficient, efficency

    def check_evolution(self):
        is_evolving = self.evolve()
        if is_evolving:
            print(f"{self.get_original_name().upper()} évolue en : {self.name.upper()}")
            self.set_hp_max(self.get_hp_max() + random.randrange(20, 35))
            self.set_defense(self.get_defense() + random.randrange(20, 35))
            self.set_strength(self.get_strength() + random.randrange(20, 35))
            self.set_speed(self.get_speed() + random.randrange(20, 35))

    
    def get_xp_gained(self, enemy):
        enemy_level = enemy.get_level()

        if enemy_level > self._level:
            if enemy.get_state() == 'wild':
                xp_gained = int(math.floor(100 * enemy.get_level() / 6))
            else:
                xp_gained = int(math.floor(100 * enemy.get_level() / 5))
        elif enemy_level < self._level:
            xp_gained = 100 * enemy.get_level() / 9
        else:
            xp_gained = 100 * enemy.get_level() / 7
        return xp_gained

    
    def update_xp(self, enemy):
        xp_gained = self.get_xp_gained(enemy)
        self.set_xp(self.get_xp() + xp_gained)
        self.__ev.update_ev(enemy, self)
        # self.set_ev(enemy)        
        print(f"\nVous avez gagné {xp_gained}, votre total d'xp est de {self.get_xp()}\n")

    def __str__(self):
        if len(self.type) > 1:
            string = f"Pokemon : {self.name}\
                \nNiveau : {self.get_level()}\
                \nXP : {self.get_xp()}\
                \nDéfense : {self.get_defense()}\
                \nRapidité : {self.get_speed()}\
                \nPV : {self.get_hp()}\
                \nType principal : {self.type[0]}\
                \nType secondaire : {self.type[1]}\
                \nForce : {self.get_strength()}\n"
        else:
            string = f"Pokemon : {self.name}\
                \nNiveau : {self.get_level()}\
                \nXP : {self.get_xp()}\
                \nDéfense : {self.get_defense()}\
                \nRapidité : {self.get_speed()}\
                \nPV max : {self.get_hp_max()}\
                \nPV actuel : {self.get_hp()}\
                \nType : {self.type[0]}\
                \nForce : {self.get_strength()}\n"
        return string + "\n"