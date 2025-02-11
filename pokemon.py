import random, json, math
class Pokemon():
    coefficient = json.load(open('coefficient.json'))

    def __init__(self, name, hp, strength, defense, type, level, speed, stage):
        self.name = name
        self.__stage = stage
        self.__hp = hp
        self.__strength = strength
        self.__defense = defense
        self.__xp = 0
        self.__state = 'wild' # domesticated
        self.__effort_value = {
            "hp" : 0,
            "defense" : 0,
            "strength" : 0,
            "speed" : 0
        }
        self.__speed = speed
        self.__level = level
        self.type = type
        # self.image_path = 'images/pokemons/' + self.name + '.png'
        self.pet_name = 'Jean-Luc'

    def get_ev(self):
        return self.__effort_value
    
    def set_effort_value(self): 
        add_value = random.randrange(0, 255)
        self.__effort_value = self.get_ev() + add_value

    def get_hp(self):
        return self.__hp
    
    def set_damage_hp(self, damage):
        self.__hp = self.get_hp() - damage
    
    def get_strength(self):
        return self.__strength

    def get_defense(self):
        return self.__defense
    
    def get_xp(self):
        return self.__xp

    def get_level(self):
        return self.__level
    
    def get_speed(self):
        return self.__speed
    
    def get_state(self):
        return self.__state
    
    def set_state(self, new_state):
        if new_state in ['wild', 'domesticated']:
            self.__state = new_state
        
    
    def set_level_up(self, add_level):
        self.__level += add_level
        self.__strength += 3
        self.__defense += 3
        self.__speed += 3
        self.__hp += 3

        print(f"Vous avez gagné {add_level} niveau\
              \n{self.get_strength()}\
              \n{self.get_defense()}\
              \n{self.get_speed()}\
              \n{self.get_hp()}")

    
    def check_enemy_type(self, chose_attack_type, enemy):
        if len(enemy.type) > 1:
            list_coefficient = []
            
            for index in range(len(enemy.type)):
                a_coefficient = Pokemon.coefficient[chose_attack_type][enemy.type[index]]
                list_coefficient.append(a_coefficient)
        
            coefficient = list_coefficient[0] * list_coefficient[1]
        else:
            coefficient = Pokemon.coefficient[chose_attack_type][enemy.type[0]]

        return coefficient
    
    def attack(self, chose_attack_type, enemy):

        coefficient, efficency = self.attack_efficiency(chose_attack_type, enemy)
        
        damage = self.get_strength() * coefficient
        enemy_hp = enemy.get_hp()
        if enemy_hp - damage >= 0:
            enemy.set_damage_hp(damage)
        else:
            enemy.set_damage_hp(enemy_hp)
            print(f"le pokemon {enemy.name} n'a plus de PV !")
            self.update_xp(enemy)

        print(f"{self.name} a fait une attaque {chose_attack_type}, {efficency}\
              \n Le pokemon {enemy.name} de type {enemy.type} en face a reçu {damage}, il lui reste : {enemy.get_hp()}")
        
        self.level_up()

    def attack_efficiency(self, chose_attack_type, enemy):
        coefficient = self.check_enemy_type(chose_attack_type, enemy)

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
                    if enemy_level - self.__level in range(5):
                        xp_gained = enemy.get_level() * 2
                    elif enemy_level - self.__level in range(5, 20):
                        xp_gained = enemy.get_level() * 1
                    elif enemy_level - self.__level in range(20, 60):
                        xp_gained = math.floor(enemy.get_level() * 0.5)
                    else:
                        xp_gained = math.floor(enemy.get_level() * 0.4)
            else:
                if enemy_level - self.__level in range(5):
                    xp_gained = enemy.get_level() * 3
                elif enemy_level - self.__level in range(5, 20):
                    xp_gained = math.floor(enemy.get_level() * 1.5)
                elif enemy_level - self.__level in range(20, 60):
                    xp_gained = math.floor(enemy.get_level() * 0.7)
                else:
                    xp_gained = math.floor(enemy.get_level() * 0.5)

        elif enemy_level < self.__level:
            xp_gained = math.ceil(enemy.get_level() * 0.2)
        else:
            xp_gained = math.ceil(enemy.get_level() *  0.5)
            
        return xp_gained

    def update_ev(self):
        # update_stat = [self.__defense, self.__strength, self.__speed]
        # add_ev = []
        # for keys in self.get_ev():
        #     new_value = self.get_ev()[keys] + enemy.get_ev()[keys]
        #     self.get_ev()[keys] = new_value
        #     if bool(int((self.get_ev()[keys] + enemy.get_ev()[keys])/4)):
        #         add_ev.append((self.get_ev()[keys] + enemy.get_ev()[keys])/4)

        # if add_ev:
        #     for index in range(len(add_ev)):
        #         update_stat[index] += add_ev[index]
        ev_key_list = list(self.get_ev().keys())
        for index in range(len(ev_key_list)):
            if self.get_ev()[ev_key_list[index]] > 4:
                if index == 0:
                    self.__hp += self.get_ev()[ev_key_list[index]]//4
                    self.get_ev()[ev_key_list[index]] = self.get_ev()[ev_key_list[index]]%4
                elif index == 1:
                    self.__defense += self.get_ev()[ev_key_list[index]]//4
                    self.get_ev()[ev_key_list[index]] = self.get_ev()[ev_key_list[index]]%4
                elif index == 2:
                    self.__strength += self.get_ev()[ev_key_list[index]]//4
                    self.get_ev()[ev_key_list[index]] = self.get_ev()[ev_key_list[index]]%4
                elif index == 3:
                    self.__speed += self.get_ev()[ev_key_list[index]]//4
                    self.get_ev()[ev_key_list[index]] = self.get_ev()[ev_key_list[index]]%4
        # for keys in self.get_ev():
        #     if self.get_ev()[keys]%4 == 0:
        #         add_ev.append(self.get_ev()/4)
        
        print(f"Nouvelles valeurs de {self.name}:\
              \nHP : {self.get_hp()}\
              \nDEFENSE : {self.get_defense()}\
              \nSTRENGTH : {self.get_strength()}\
              \nSPEED : {self.get_speed()}")
        

    def update_xp(self, enemy):
        xp_gained = self.get_xp_gained(enemy)
        self.__xp += xp_gained
        self.set_ev(enemy)        
        print(f"Vous avez gagné {xp_gained}, votre total d'xp est de {self.get_xp()}")


    def set_ev(self, enemy):
        ev_dictionary = self.get_ev()

        rand_range_defense = int(enemy.get_defense() / 6)
        rand_range_strength = int((enemy.get_strength() / 6))
        rand_range_speed = int((enemy.get_speed() / 6))

        ev_dictionary["defense"] += math.floor(random.randrange(rand_range_defense, rand_range_defense*4))
        ev_dictionary["strength"] += math.floor(random.randrange(rand_range_strength, rand_range_strength*4))
        ev_dictionary["speed"] += math.floor(random.randrange(rand_range_speed, rand_range_speed*4))

        
        print(f"dictionnaire EV\n{self.get_ev()}")
        self.update_ev()

    def level_up(self):
        level =  self.get_level()
        if self.__xp >= level** 3:
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