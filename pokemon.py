import random, json, math
from models.effortValue import EffortValue


class Evolution():
    def __init__(self, stage):
        self.stage = stage
    
    def get_image(self):
        pass

    def get_name(self):
        pass

class Pokemon(Evolution):
    coefficient = json.load(open('coefficient.json'))

    def __init__(self, name, original_name, hp, strength, defense, type, level, speed, stage):
        super().__init__()
        self.name = name
        self.__stage = Evolution(stage)
        self.__hp = hp
        self.__hp_max = hp
        self.__strength = strength
        self.__defense = defense
        self.__xp = 1
        self.__state = 'wild' # or domesticated
        self.__ev = EffortValue()

        # self.__effort_value = {
        #     "hp" : 0,
        #     "defense" : 0,
        #     "strength" : 0,
        #     "speed" : 0
        # }
        self.__speed = speed
        self.__level = level
        self.type = type
        # self.image_path = 'images/pokemons/' + self.name + '.png'
        self.pet_name = 'Jean-Luc'

    def get_hp(self):
        return self.__hp
    
    def set_damage_hp(self, damage):
        self.__hp = self.get_hp() - damage

    def get_hp_max(self):
        return self.__hp_max
    
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

    def get_level(self):
        return self.__level
    
    def get_speed(self):
        return self.__speed
    
    def set_speed(self, new_value):
        self.__speed = new_value
    
    def get_state(self):
        return self.__state
    
    def set_state(self, new_state):
        if new_state in ['wild', 'domesticated']:
            self.__state = new_state
        
    
    def set_level_up(self, add_level):
        self.__level += add_level
        self.__strength += add_level*3
        self.__defense += add_level*3
        self.__speed += add_level*3
        self.__hp += add_level*3

        print(f"Vous avez gagné {add_level} niveau\
              \n{self.get_strength()}\
              \n{self.get_defense()}\
              \n{self.get_speed()}\
              \n{self.get_hp()}\n\n")

    
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
    
    def attack(self, chose_attack_type, enemy):

        coefficient, efficency = self.attack_efficiency(chose_attack_type, enemy)
        
        damage = self.get_strength() * coefficient
        enemy_hp = enemy.get_hp()
        if enemy_hp - damage >= 0:
            enemy.set_damage_hp(damage)
        else:
            enemy.set_damage_hp(enemy_hp)
            
            # self.update_xp(enemy)

        print(f"{self.name} a fait une attaque {chose_attack_type}, {efficency}\
              \n Le pokemon {enemy.name} de type {enemy.type} en face a reçu {damage}, il lui reste : {enemy.get_hp()}")
        
        if enemy.get_hp() == 0:
            print(f"le pokemon {enemy.name} n'a plus de PV !")
            self.update_xp(enemy)
        
        self.level_up()

    def attack_efficiency(self, chose_attack_type, enemy):
        coefficient = self.get_attack_coefficient(chose_attack_type, enemy)

        match coefficient:
            case 4:
                efficency = "attaque ultra efficace"
                # self.__xp = self.get_xp() + 20
            case 2:
                efficency = "attaque très efficace"
                # self.__xp = self.get_xp() + 10
            case 1:
                efficency = "attaque efficace"
                # self.__xp = self.get_xp() + 5
            case 0.5:
                efficency = "attaque peu efficace"
                # self.__xp = self.get_xp() + 2
            case 0:
                efficency = "impossible d'attaquer"

        self.evolve()

        return coefficient, efficency
    
    def get_xp_gained(self, enemy):
        enemy_level = enemy.get_level()
        if enemy_level > self.__level:
            if enemy.get_state() == 'wild':
                    if enemy_level in range(5):
                        xp_gained = enemy.get_level() * 2
                    elif enemy_level in range(5, 20):
                        xp_gained = enemy.get_level() * 1
                    elif enemy_level in range(20, 60):
                        xp_gained = math.floor(enemy.get_level() * 0.5)
                    else:
                        xp_gained = math.floor(enemy.get_level() * 0.4)
            else:
                if enemy_level in range(5):
                    xp_gained = enemy.get_level() * 3
                elif enemy_level in range(5, 20):
                    xp_gained = math.floor(enemy.get_level() * 1.5)
                elif enemy_level in range(20, 60):
                    xp_gained = math.floor(enemy.get_level() * 0.7)
                else:
                    xp_gained = math.floor(enemy.get_level() * 0.5)

        elif enemy_level < self.__level:
            xp_gained = math.ceil(enemy.get_level() * 0.2)
        else:
            xp_gained = math.ceil(enemy.get_level() *  0.5)
            
        return xp_gained

    
    def update_xp(self, enemy):
        xp_gained = self.get_xp_gained(enemy)
        self.set_xp(self.get_xp() + xp_gained)
        self.__ev.update_ev(enemy, self)
        # self.set_ev(enemy)        
        print(f"\nVous avez gagné {xp_gained}, votre total d'xp est de {self.get_xp()}\n")


    # def set_ev(self, enemy):
    #     ev_dictionary = self.get_ev()

    #     rand_range_defense = int(enemy.get_defense() / 6)
    #     rand_range_strength = int((enemy.get_strength() / 6))
    #     rand_range_speed = int((enemy.get_speed() / 6))

    #     ev_dictionary["defense"] += math.floor(random.randrange(rand_range_defense * 2, rand_range_defense * 4))
    #     ev_dictionary["strength"] += math.floor(random.randrange(rand_range_strength * 2, rand_range_strength * 4))
    #     ev_dictionary["speed"] += math.floor(random.randrange(rand_range_speed * 2, rand_range_speed * 4))

        
        # print(f"dictionnaire EV\n{self.get_ev()}\n")
        # self.update_ev()

    def level_up(self):
        level =  self.get_level()
        if self.__xp >= level**3 +3:
            self.set_level_up(1)

    def evolve(self):
        level = self.get_level()
        if level in range(15, 40):
            luck = random.randrange(100)
            if luck > 60:
                self.__stage += 1
        

        # if self.get_xp() >= Pokemon.evolving_stage[self.get_level()]:
        #     self.set_level_up(1)

        # if self.__level == 4:
        #     self.name = "bidule"

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
                \nPV : {self.get_hp()}\
                \nType : {self.type[0]}\
                \nForce : {self.get_strength()}\n"
        return string + "\n"




# first_pokemon = create_pokemon('Toto')
# print(first_pokemon)
# my_enemy = create_pokemon('Hehe')

# my_pokemon = Pokemon('Thibault', 50, 20, 0, ['water', 'electric'])
# my_enemy = Pokemon('Joseph', 60, 10, 0, ['fire', 'dragon'] )

# print(my_pokemon, my_enemy)

# first_pokemon.attack(first_pokemon.type[0], my_enemy)
# first_pokemon.attack(first_pokemon.type[0], my_enemy)
# first_pokemon.attack(first_pokemon.type[0], my_enemy)
# first_pokemon.attack(first_pokemon.type[0], my_enemy)
# first_pokemon.attack(first_pokemon.type[0], my_enemy)
# first_pokemon.attack(first_pokemon.type[0], my_enemy)
# first_pokemon.attack(first_pokemon.type[0], my_enemy)
# print(first_pokemon, my_enemy)
# my_enemy.attack(my_enemy.type[0] ,first_pokemon)
# print(first_pokemon, my_enemy)