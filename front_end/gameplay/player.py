import pygame
from front_end.gameplay.entity import Entity
from .keylistener import KeyListener
from front_end.screen import Screen
from .switch import Switch
from front_end.menu.name_input import NameInput
from front_end.gameplay.battlescreen import BattleScreen


class Player(Entity):
    def __init__(self, keylistener: KeyListener, screen: Screen, x: int, y: int, player_name: str):
        super().__init__(keylistener, screen, x, y)
        #  
        self.switchs : list[Switch] | None = None
        self.change_map = None
        self.collisions = None
        self.spritesheet_bike = pygame.image.load("assets/sprite/hero_01_red_m_cycle_roll.png")
        self.player_name = player_name
        self.name = player_name
        self.is_fleeing = False
        

    def update(self) -> None:
        self.check_input()
        self.check_move()
        super().update()

    def check_move(self) -> None:
        if self.animation_walk is False:
            temp_hitbox = self.hitbox.copy()
            if self.keyListener.key_pressed(pygame.K_q):
                temp_hitbox.x -= 16
                if not self.check_collisions(temp_hitbox):
                    self.check_collisions_switchs(temp_hitbox)
                    self.move_left()
                else:
                    self.direction = "left"
            elif self.keyListener.key_pressed(pygame.K_d):
                temp_hitbox.x += 16
                if not self.check_collisions(temp_hitbox):
                    self.check_collisions_switchs(temp_hitbox)
                    self.move_right()
                else:
                    self.direction = "right"
            elif self.keyListener.key_pressed(pygame.K_z):
                temp_hitbox.y -= 16
                if not self.check_collisions(temp_hitbox):
                    self.check_collisions_switchs(temp_hitbox)
                    self.move_up()
                else:
                    self.direction = "up"
            elif self.keyListener.key_pressed(pygame.K_s):
                temp_hitbox.y += 16
                if not self.check_collisions(temp_hitbox):
                    self.check_collisions_switchs(temp_hitbox)
                    self.move_down()
                else:
                    self.direction = "down"
         
            

    def add_switchs(self, switchs: list[Switch]) :
        """
        Add the switchs to the player
        :param switchs:
        :return:
        """
        self.switchs = switchs

    def check_collisions_switchs(self, temp_hitbox):
        if self.switchs:
            for switch in self.switchs:
                if switch.check_collision(temp_hitbox):
                     self.change_map = switch
                 
                   
                   
            return None
        
    def add_collisions(self, collisions):
        self.collisions = collisions

    def check_collisions(self, temp_hitbox: pygame.Rect):
        for collision in self.collisions:
            if temp_hitbox.colliderect(collision):
                return True
        return False
    
    def check_input(self):
        if self.keyListener.key_pressed(pygame.K_b):
            self.switch_bike()

    def switch_bike(self, deactive = False):
        if self.speed == 1 and not deactive:
            self.speed = 2
            self.all_images = self.get_all_images(self.spritesheet_bike)
        else:
            self.speed = 1
            self.all_images = self.get_all_images(self.spritesheet)
        self.keyListener.remove_key(pygame.K_b)


    def start_battle(self, battle_zones):
        for battle_zone in battle_zones:
            if self.rect.colliderect(battle_zone):
                
                print("Début du combat Pokémon !")
                battle_screen = BattleScreen(self.screen, self)
                battle_screen.run()
                break
    
    def battle(self):
        print("Début du combat Pokémon !")
        battle_screen = BattleScreen(self.screen, self)
        battle_screen.run()
        self.in_battle = False


    def check_input(self):
        if self.keyListener.key_pressed(pygame.K_b):
            self.switch_bike()

        # Ajouter la condition pour activer/désactiver le mode fuite
        if self.keyListener.key_pressed(pygame.K_f):  # Touche F pour fuir
            self.is_fleeing = True
        else:
            self.is_fleeing = False




        




    

    # def check_move(self) -> None:
    #     if self.animation_walk is False:
    #         if self.keylistener.key_pressed(pygame.K_q):
    #             self.move_left()
    #         elif self.keylistener.key_pressed(pygame.K_d):
    #             self.move_right()
    #         elif self.keylistener.key_pressed(pygame.K_z):
    #             self.move_up()
    #         elif self.keylistener.key_pressed(pygame.K_s):
    #             self.move_down()
