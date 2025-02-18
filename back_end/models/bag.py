class Bag:
    def __init__(self):
        self.potion = 10
        self.pokeball = 15

    def get_potion(self):
        return self.potion
    
    def get_pokeball(self):
        return self.pokeball
    
    def set_potion(self, new_value):
        self.potion = new_value

    def set_pokeball(self, new_value):
        self.pokeball = new_value

    def get_dict(self):
        return {
            "potions" : self.get_potion(),
            "pokeball" : self.get_pokeball()
        }