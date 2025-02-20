class FightInfo():
    def __init__(self,):
        self.efficiency = ""
        self.attack_type = ""
        self.total_damage = 0
        self.actual_hp = 0
        self.flee_message = ""

    def set_all_values(self, efficiency, attack_type, damage):
        self.efficiency = efficiency
        self.attack_type = attack_type
        self.total_damage = damage

    def set_who_attack_message(self, pokemon):
        return f"Attak type {self.attack_type} from {pokemon.name} "
    
    def get_damage_message(self):
        if self.total_damage > 1:
            return f"{self.efficiency} : {self.total_damage} damages"
        else:
            return f"{self.efficiency} : {self.total_damage} damage"

    def set_flee_trainer_message(self):
        self.flee_message = "You can't escape a fight against another pokemon trainer"
    
    def set_fail_flee_message(self):
        self.flee_message = "You failed to flee..."

    def set_success_flee_message(self):
        self.flee_message = "You escaped successfully"