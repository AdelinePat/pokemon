import random, json
from __settings__ import TYPES_PATH, EVOLUTION_STAGE_PATH

class Evolution():
    def __init__(self, name, stage, original_name, type, level):
        self.name = name
        self.__stage = stage
        self.__original_name = original_name
        self._level = level
        self.type = type
        # self.image_path = self.set_image()
        self.__names_list, self.__evolution_number = self.get_evolution_name_list()
        self.image = self.set_image()

    def set_stage(self, new_stage):
        self.__stage = new_stage
    
    def get_stage(self):
        return self.__stage

    def set_image(self):
        image = "./images/pokemons/" + self.name + ".png"
        return image


    def get_name(self):
        pass

    def get_evolution_stage_json(self):
        with open(EVOLUTION_STAGE_PATH, 'r') as evolution_stage:
            data = json.load(evolution_stage)
            name_list = list(data.keys())
        return name_list, data
   
    def get_evolution_name_list(self):
        name_list, evolution_stage = self.get_evolution_stage_json()
        
        find = False
        for pokemon in name_list:
            if self.__original_name == pokemon and not find:
                my_pokemon_names = list(evolution_stage[pokemon].keys())
                if self.__original_name != 'Eevee':
                    evolution_number = len(my_pokemon_names)
                else:
                    evolution_number = 2
                find = True
        
        
        return my_pokemon_names, evolution_number
    
    def update_name(self, new_name):
        self.name = new_name

    def update_evolution_meowth(self):
        if self.type[0] != 'normal':
            self.__type = ['dark']

    def update_evolution_eevee(self):
        types = ['water', 'electric', 'fire']
        new_type = random.choice(types) #Doesn't change type
        self.type.append(new_type)
        self.type.pop(self.type.index('normal'))
        # self.__type = [new_type]
        match new_type:
            case 'water':
                new_name = 'Vaporeon'
            case 'electric':
                new_name = 'Jolteon'
            case 'fire':
                new_name = 'Flareon'
        self.update_name(new_name)
        #TODO update name

    def update_evolution_slowpoke(self):
        if self.__type[0] == 'psychic':
            self.__type = ['poison', 'psychic']

    #TODO Check geodude vers graveler et golemn !!

    def update_evolution_stage(self):
        name_list, evolution_stage = self.get_evolution_stage_json()

        if self.__original_name != 'Eevee':
            evolution_stage_value = list(evolution_stage[self.__original_name].values())
            new_name = list(evolution_stage[self.__original_name].keys())[evolution_stage_value.index(self.__stage)]
            self.update_name(new_name)
        self.update_type()
        self.set_image()

    def update_type(self):

        if len(self.type) == 1 and self.__original_name not in ['Eevee', 'Meowth', 'Slowpoke']:
            with open(TYPES_PATH, 'r') as file:
                data = json.load(file)
                my_pokemon_data = data[self.type[0]]

            data_list = list(my_pokemon_data.keys())
            
            # For all type except normal type and Eevee
            for sub_type in data_list:
                # first_type_list = list(my_pokemon_data[sub_type].keys())
                if sub_type != "alone":
                    sub_type_dict = my_pokemon_data[sub_type]
                    if self.__original_name in sub_type_dict["names"]: 
                        if self.name in sub_type_dict["names"][self.__original_name]: # .keys()
                            self.type.append(sub_type)
        
        if self.__original_name == "Eevee":
            self.update_evolution_eevee()

        if self.__original_name == "Meowth":
            self.update_evolution_meowth()
        
        if self.__original_name == "Slowpoke":
            self.update_evolution_slowpoke()

    def level_up(self, pokemon):
        level =  self.get_level()
        xp_value = pokemon.get_xp()
        add_level = 0
        while xp_value >= level**3: #TODO balance level up ?
            add_level += 1
            xp_value -= level**3
            level += 1
            
        if add_level != 0:
            self.set_level_up(pokemon, add_level)

    def evolve(self):
        level = self.get_level()
        if self.__stage < self.__evolution_number:
            if self.__evolution_number == 3:
                match self.__stage:
                    case 1:
                        if level in range(10, 20):
                            luck = random.randrange(100)
                            if luck > 60:
                                self.__stage += 1
                                self.update_evolution_stage()
                                return True
                        elif level == 20:
                            self.__stage += 1
                            self.update_evolution_stage()
                            return True
                    case 2:
                        if level in range(22, 32):
                            luck = random.randrange(100)
                            if luck > 60:
                                self.__stage += 1
                                self.update_evolution_stage()
                                return True
                        elif level == 32:
                            self.__stage += 1
                            self.update_evolution_stage()
                            return True
            if self.__evolution_number == 2: 
                match self.__stage:
                    case 1:
                        if level in range(17, 25):
                            luck = random.randrange(100)
                            if luck > 60:
                                self.__stage += 1
                                self.update_evolution_stage()
                                return True
                        elif level == 25:
                            self.__stage += 1
                            self.update_evolution_stage()
                            return True
            
        # if level in range(5,10):
        #     luck = random.randrange(100)
        #     if luck > 0:
        #         self.__stage += 1
        #         self.update_evolution_stage()
                
                
    def set_level_up(self, pokemon, add_level):
        self._level += add_level
        pokemon.set_strength(pokemon.get_strength() + random.randrange(add_level*5, add_level*15))
        pokemon.set_defense(pokemon.get_defense() + random.randrange(add_level*5, add_level*15))
        pokemon.set_speed(pokemon.get_speed() + random.randrange(add_level*5, add_level*15))
        pokemon.set_hp_max(pokemon.get_hp_max() + random.randrange(add_level*5, add_level*15))
        # self.__strength += add_level*3
        # self.__defense += add_level*3
        # self.__speed += add_level*3
        # self.__hp += add_level*3

        print(f"Vous avez gagné {add_level} niveau\
              \n{self.get_strength()}\
              \n{self.get_defense()}\
              \n{self.get_speed()}\
              \n{self.get_hp()}\n\n")
        
    def get_level(self):
        return self._level
    
    def get_original_name(self):
        return self.__original_name