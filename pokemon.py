class Pokemon():
    # physical_type = ['normal', 'fighting', 'ground', 'flying', 'bug', 'rock']
    # element_type = ['fire', 'water', 'electric', 'grass', 'ice', 'poison', 'psychic'] # inefficient against themselves
    # special_type = ['ghost', 'dragon'] # efficient against themselves

    coeficient = {
        'normal': {
            'normal': 1,
            'fire' : 1,
            'water': 1,
            'electric': 1,
            'grass': 1,
            'ice': 1,
            'fighting': 1,
            'poison': 1,
            'ground': 1,
            'flying': 1,
            'psychic': 1,
            'bug': 1,
            'rock': 0.5,
            'ghost': 0,
            'dragon' : 1
        },
        'fire': {
            'normal': 1,
            'fire' : 0.5,
            'water': 0.5,
            'electric': 1,
            'grass': 2,
            'ice': 2,
            'fighting': 1,
            'poison': 1,
            'ground': 1,
            'flying': 1,
            'psychic': 1,
            'bug': 2,
            'rock': 0.5,
            'ghost': 1,
            'dragon' : 0.5
        },
        'water': {
            'normal': 1,
            'fire' : 2,
            'water': 0.5,
            'electric': 1,
            'grass': 0.5,
            'ice': 1,
            'fighting': 1,
            'poison': 1,
            'ground': 2,
            'flying': 1,
            'psychic': 1,
            'bug': 1,
            'rock': 2,
            'ghost': 0,
            'dragon' : 0.5
        },
        'electric': {
            'normal': 1,
            'fire' : 1,
            'water': 2,
            'electric': 1,
            'grass': 0.5,
            'ice': 1,
            'fighting': 1,
            'poison': 1,
            'ground': 0,
            'flying': 2,
            'psychic': 1,
            'bug': 1,
            'rock': 1,
            'ghost': 1,
            'dragon' : 0.5
        },
        'grass': {
            'normal': 1,
            'fire' : 0.5,
            'water': 2,
            'electric': 1,
            'grass': 0.5,
            'ice': 1,
            'fighting': 1,
            'poison': 0.5,
            'ground': 2,
            'flying': 0.5,
            'psychic': 1,
            'bug': 0.5,
            'rock': 2,
            'ghost': 1,
            'dragon' : 0.5
        },
        'ice': {
            'normal': 1,
            'fire' : 1,
            'water': 0.5,
            'electric': 1,
            'grass': 2,
            'ice': 0.5,
            'fighting': 1,
            'poison': 1,
            'ground': 1,
            'flying': 2,
            'psychic': 1,
            'bug': 1,
            'rock': 1,
            'ghost': 1,
            'dragon' : 2
        },
        'fighting': {
            'normal': 2,
            'fire' : 1,
            'water': 1,
            'electric': 1,
            'grass': 1,
            'ice': 1,
            'fighting': 1,
            'poison': 0.5,
            'ground': 1,
            'flying': 0.5,
            'psychic': 0.5,
            'bug': 0.5,
            'rock': 2,
            'ghost': 0,
            'dragon' : 1
        },
        'poison': {
            'normal': 1,
            'fire' : 1,
            'water': 1,
            'electric': 1,
            'grass': 2,
            'ice': 1,
            'fighting': 1,
            'poison': 0.5,
            'ground': 0.5,
            'flying': 1,
            'psychic': 1,
            'bug': 2,
            'rock': 0.5,
            'ghost': 0.5,
            'dragon' : 1
        },
        'ground': {
            'normal': 1,
            'fire' : 2,
            'water': 1,
            'electric': 2,
            'grass': 0.5,
            'ice': 1,
            'fighting': 1,
            'poison': 2,
            'ground': 1,
            'flying': 0,
            'psychic': 1,
            'bug': 0.5,
            'rock': 2,
            'ghost': 1,
            'dragon' : 1
        },
        'flying': {
            'normal': 1,
            'fire' : 1,
            'water': 1,
            'electric': 0.5,
            'grass': 2,
            'ice': 1,
            'fighting': 2,
            'poison': 1,
            'ground': 1,
            'flying': 1,
            'psychic': 1,
            'bug': 2,
            'rock': 0.5,
            'ghost': 1,
            'dragon' : 1
        },
        'psychic': {
            'normal': 1,
            'fire' : 1,
            'water': 1,
            'electric': 1,
            'grass': 1,
            'ice': 1,
            'fighting': 2,
            'poison': 2,
            'ground': 1,
            'flying': 1,
            'psychic': 0.5,
            'bug': 1,
            'rock': 1,
            'ghost': 1,
            'dragon' : 1
        },
        'bug': {
            'normal': 1,
            'fire' : 0.5,
            'water': 1,
            'electric': 1,
            'grass': 2,
            'ice': 1,
            'fighting': 0.5,
            'poison': 2,
            'ground': 1,
            'flying': 0.5,
            'psychic': 2,
            'bug': 1,
            'rock': 1,
            'ghost': 0.5,
            'dragon' : 1
        },
        'rock': {
            'normal': 1,
            'fire' : 2,
            'water': 1,
            'electric': 1,
            'grass': 1,
            'ice': 2,
            'fighting': 0.5,
            'poison': 1,
            'ground': 0.5,
            'flying': 2,
            'psychic': 1,
            'bug': 2,
            'rock': 1,
            'ghost': 1,
            'dragon' : 1
        },
        'ghost': {
            'normal': 1,
            'fire' : 1,
            'water': 1,
            'electric': 1,
            'grass': 1,
            'ice': 1,
            'fighting': 1,
            'poison': 1,
            'ground': 1,
            'flying': 1,
            'psychic': 1,
            'bug': 1,
            'rock': 1,
            'ghost': 2,
            'dragon' : 1
        },
        'dragon': {
            'normal': 1,
            'fire' : 1,
            'water': 1,
            'electric': 1,
            'grass': 1,
            'ice': 1,
            'fighting': 1,
            'poison': 1,
            'ground': 1,
            'flying': 1,
            'psychic': 1,
            'bug': 1,
            'rock': 1,
            'ghost': 1,
            'dragon' : 2
        }
    }

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
        self.hp = hp
        self.strength = strength
        self.defense = defense
        self.xp = 0
        self.level = level
        self.type = self.check_type(type)
    
    def check_type(self, type):
        if len(type) > 2:
            type = input("Vous n'avez pas entré le bon nombre de type, vous ne pouvez en choisir que 2 maximum\n").split()
            if len(type) > 2:
                return self.check_type(type)
            
            if type[0] == type[1]:
                type = input("Vous ne pouvez pas entrer deux fois le même type\n").split()
                if type[0] == type[1]:
                    return self.check_type(type)
            
        return type

    def check_enemy_type(self, chose_attack_type, enemy):
        if len(enemy.type) > 1:
            list_coefficient = []
            
            for index in range(len(enemy.type)):
                a_coefficient = Pokemon.coeficient[chose_attack_type][enemy.type[index]]
                list_coefficient.append(a_coefficient)
        
            # for another_index in range(len(list_coefficient)):
            if list_coefficient[0] == 2 and list_coefficient[1] == 2:
                coefficient = 4
            else:
                coefficient = max(list_coefficient)
        else:
            coefficient = Pokemon.coeficient[chose_attack_type][enemy.type[0]]

        return coefficient
    
    def attack(self, chose_attack_type, enemy):

        coefficient, efficency = self.update_xp(chose_attack_type, enemy)
        
        damage = self.strength * coefficient
        if enemy.hp - damage >= 0:
            enemy.hp -= damage
        else:
            print(f"le pokemon {enemy.name} n'a plus de PV !")

        print(f"{self.name} a fait une attaque {chose_attack_type}, {efficency}\
              \n Le pokemon {enemy.name} de type {enemy.type} en face a reçu {damage}, il lui reste : {enemy.hp}")

    def update_xp(self, chose_attack_type, enemy):
        coefficient = self.check_enemy_type(chose_attack_type, enemy)

        match coefficient:
            case 4:
                efficency = "attaque ultra efficace"
                self.xp += 20
            case 2:
                efficency = "attaque très efficace"
                self.xp += 10
            case 1:
                efficency = "attaque efficace"
                self.xp += 5
            case 0.5:
                efficency = "attaque peu efficace"
                self.xp += 2
            case 0:
                efficency = "impossible d'attaquer"
        self.level = self.evolve()
        return coefficient, efficency
    
    def evolve(self):
        if self.xp >= Pokemon.evolving_stage[self.level]:
            self.level += 1

        return self.level 

    def __str__(self):
        if len(self.type) > 1:
            string = f"Pokemon : {self.name}\
                \nNiveau : {self.level}\
                \nXP : {self.xp}\
                \nPV : {self.hp}\
                \nType principal : {self.type[0]}\
                \nType secondaire : {self.type[1]}\
                \nForce : {self.strength}\n"
        else:
            string = f"Pokemon : {self.name}\
                \nNiveau : {self.level}\
                \nXP : {self.xp}\
                \nPV : {self.hp}\
                \nType : {self.type[0]}\
                \nForce : {self.strength}\n"
        return string + "\n"

my_pokemon = Pokemon('Thibault', 50, 20, 0, ['water', 'electric'])
my_enemy = Pokemon('Joseph', 60, 10, 0, ['fire', 'dragon'] )

print(my_pokemon, my_enemy)

my_pokemon.attack(my_pokemon.type[0], my_enemy)
my_pokemon.attack(my_pokemon.type[0], my_enemy)
my_pokemon.attack(my_pokemon.type[0], my_enemy)
my_pokemon.attack(my_pokemon.type[0], my_enemy)
my_pokemon.attack(my_pokemon.type[1], my_enemy)
my_pokemon.attack(my_pokemon.type[1], my_enemy)
my_pokemon.attack(my_pokemon.type[1], my_enemy)
print(my_pokemon, my_enemy)
my_enemy.attack(my_enemy.type[0] ,my_pokemon)
print(my_pokemon, my_enemy)