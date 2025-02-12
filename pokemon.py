import random, json
class Pokemon():
    coefficient = json.load(open('coefficient.json'))

    evolving_stage = {
        1 : 50,
        2 : 100,
        3 : 200, 
        4 : 400,
        5 : 800,
        6 : 1600,
        7 : 3200,
        8 : 6400,
        9 : 12800,
        10 : 25600
    }

    def __init__(self, name, hp, strength, defense, type, level=1):
        self.name = name
        self.__hp = hp
        self.__strength = strength
        self.__defense = defense
        self.__xp = 0
        self.__level = level
        self.type = type
        # self.image_path = 'images/pokemons/' + self.name + '.png'
        self.pet_name = 'Jean-Luc'

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
    
    def set_level_up(self, add_level):
        self.__level = self.get_level + add_level
    
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

        coefficient, efficency = self.update_xp(chose_attack_type, enemy)
        
        damage = self.get_strength() * coefficient
        enemy_hp = enemy.get_hp()
        critical = random.randint(1, 20)
        if enemy_hp - (damage - enemy.get_defense()) >= 0:
            if critical == 20:
                print("Coup critique !")
                damage = damage * 2
                enemy.set_damage_hp(damage)
            else:
                damage = damage - enemy.get_defense()
                enemy.set_damage_hp(damage)
        else:
            enemy.set_damage_hp(enemy_hp)
            print(f"le pokemon {enemy.name} n'a plus de PV !")

        print(f"{self.name} a fait une attaque {chose_attack_type}, {efficency}\
              \n Le pokemon {enemy.name} de type {enemy.type} en face a reçu {damage}, il lui reste : {enemy.get_hp()}")

    def update_xp(self, chose_attack_type, enemy):
        coefficient = self.check_enemy_type(chose_attack_type, enemy)

        match coefficient:
            case 4:
                efficency = "attaque ultra efficace"
                self.__xp = self.get_xp() + 20
            case 2:
                efficency = "attaque très efficace"
                self.__xp = self.get_xp() + 10
            case 1:
                efficency = "attaque efficace"
                self.__xp = self.get_xp() + 5
            case 0.5:
                efficency = "attaque peu efficace"
                self.__xp = self.get_xp() + 2
            case 0:
                efficency = "impossible d'attaquer"

        self.evolve()
        return coefficient, efficency
    
    def evolve(self):
        if self.get_xp() >= Pokemon.evolving_stage[self.get_level()]:
            self.set_level_up(1)

        # if self.__level == 4:
        #     self.name = "bidule"

    def __str__(self):
        if len(self.type) > 1:
            string = f"Pokemon : {self.name}\
                \nNiveau : {self.get_level()}\
                \nXP : {self.get_xp()}\
                \nPV : {self.get_hp()}\
                \nType principal : {self.type[0]}\
                \nType secondaire : {self.type[1]}\
                \nForce : {self.get_strength()}\n"
        else:
            string = f"Pokemon : {self.name}\
                \nNiveau : {self.get_level()}\
                \nXP : {self.get_xp()}\
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