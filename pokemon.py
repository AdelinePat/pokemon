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

    def __init__(self, hp, strength, defense, type, level=1):
        self.hp = hp
        self.strength = strength
        self.defense = defense
        self.xp = 0
        self.level = level
        self.type = type # is a list

    def attack(self, enemy):
        coefficient = Pokemon.coeficient[self.type][enemy.type]

        match coefficient:
            case 2:
                print("attaque très efficace")
            case 1:
                print("attaque efficace")
            case 0.5:
                print("attaque peu efficace")
            case 0:
                print("impossible d'attaquer")
        damage = self.strength * coefficient
        enemy.hp -= damage
        print(f"Le pokemon en face a reçu {damage}, il lui reste : {enemy.hp}")

    def defense_action(self):
        pass
    
    def evolve(self):
        pass

my_pokemon = Pokemon(50, 20, 0, 'water')
my_enemy = Pokemon(60, 10, 0, 'fire' )

my_pokemon.attack(my_enemy)
my_enemy.attack(my_pokemon)