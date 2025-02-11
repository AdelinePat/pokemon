import math

class EffortValue():
    def __init__(self):
        self.__ev_hp = 0
        self.__ev_strength = 0
        self.__ev_defense = 0
        self.__ev_speed = 0
        self.__ev_xp = 0

    def get_ev_hp(self):
            return self.__ev_hp
    
    def get_ev_strength(self):
            return self.__ev_strength
    
    def get_ev_defense(self):
            return self.__ev_defense
    
    def get_ev_speed(self):
            return self.__ev_speed
    
    def get_ev_xp(self):
            return self.__ev_xp
    
    def set_ev_hp(self, new_value):
        self.__ev_hp = new_value
    
    def set_ev_strength(self, new_value):
        self.__ev_strength = new_value
    
    def set_ev_defense(self, new_value):
        self.__ev_defense = new_value

    def set_ev_speed(self, new_value):
        self.__ev_speed = new_value
    
    def set_ev_xp(self, new_value):
        self.__ev_xp = new_value
    
    def update_ev(self, enemy, pokemon):
        rand_range_hp = math.ceil(enemy.get_hp_max()/6)
        rand_range_strength = math.ceil((enemy.get_strength() / 6))
        rand_range_defense = math.ceil(enemy.get_defense() / 6)
        rand_range_speed = math.ceil((enemy.get_speed() / 6))
        rand_range_xp = math.ceil((enemy.get_xp()/6))
        # print(f"rand hp {rand_range_hp}")
        # print(f"rand strength {rand_range_strength}")
        # print(f"rand defense {rand_range_defense}")
        # print(f"rand speed {rand_range_speed}")
        # print(f"rand xp {rand_range_xp}")

        self.set_ev_hp(self.get_ev_hp() + math.floor(random.randrange(rand_range_hp * 2, rand_range_hp * 4)))
        self.set_ev_strength(self.get_ev_strength() + math.floor(random.randrange(rand_range_strength * 2, rand_range_strength * 4)))
        self.set_ev_defense(self.get_ev_defense() + math.floor(random.randrange(rand_range_defense * 2, rand_range_defense * 4)))
        self.set_ev_speed(self.get_ev_speed() + math.floor(random.randrange(rand_range_speed * 2, rand_range_speed * 4)))
        self.set_ev_xp(self.get_ev_xp() + math.floor(random.randrange(rand_range_xp * 2, rand_range_xp * 4)))

        print(f"Nouvelles valeurs EV de {pokemon.name}:\
              \nHP : {self.get_ev_hp()}\
              \nDEFENSE : {self.get_ev_defense()}\
              \nSTRENGTH : {self.get_ev_strength()}\
              \nSPEED : {self.get_ev_speed()}\n")


        self.__update_stats(pokemon)

    def __update_stats(self, pokemon): #TODO à mettre dans pokemon
        if self.get_ev_hp() > 4:
            hp = pokemon.get_hp_max() + self.get_ev_hp()//4
            self.set_ev_hp(self.get_ev_hp()%4)
            pokemon.set_hp_max(hp)

        if self.get_ev_strength() > 4:
            strength = pokemon.get_strength() + self.get_ev_strength()//4
            self.set_ev_strength(self.get_ev_strength()%4)
            pokemon.set_strength(strength)
        
        if self.get_ev_defense() > 4:
            defense = pokemon.get_defense() + self.get_ev_defense()//4
            self.set_ev_defense(self.get_ev_defense()%4)
            pokemon.set_defense(defense)
        
        if self.get_ev_speed() > 4:
            speed = pokemon.get_speed() + self.get_ev_speed()//4
            self.set_ev_speed(self.get_ev_speed()%4)
            pokemon.set_speed(speed)
        
        if self.get_ev_xp() > 4:
            xp = pokemon.get_xp() + self.get_ev_xp()//4
            self.set_ev_xp(self.get_ev_xp()%4)
            pokemon.set_xp(xp)

        # print(f"Nouvelles valeurs EV de {pokemon.name}:\
        #       \nHP : {self.get_ev_hp()}\
        #       \nDEFENSE : {self.get_ev_defense()}\
        #       \nSTRENGTH : {self.get_ev_strength()}\
        #       \nSPEED : {self.get_ev_speed()}\n")
