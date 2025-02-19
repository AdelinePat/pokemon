import pygame
from front_end.gameplay.entity import Entity
from .keylistener import KeyListener
from front_end.screen import Screen
from .switch import Switch
# from front_end.menu.name_input import NameInput
# from front_end.gameplay.battlescreen import BattleScreen
from front_end.in_fight.in_fight import InFight
# from front_end.menu.menu import Menu
import front_end.menu.menu as menu

class Player(Entity):
    def __init__(self, keylistener: KeyListener, screen: Screen, x: int, y: int, player_name: str):
        super().__init__(keylistener, screen, x, y)
        self.switchs: list[Switch] | None = None  # List of switches the player can activate
        self.change_map = None  # Stores the switch that changes the map
        self.collisions = None  # List of collision objects
        self.spritesheet_bike = pygame.image.load("assets/sprite/hero_01_red_m_cycle_roll.png")  # Bike sprite
        self.player_name = player_name  # Stores the player's name
        self.name = player_name
        self.is_fleeing = False  # Indicates if the player is fleeing
        # self.speed = 1  # Default walking speed
        self.flee_steps = 0  # Number of steps taken while fleeing
        self.max_flee_steps = 100  # Maximum number of fleeing steps

    def update(self) -> None:
        """Update player state, checking inputs and movement."""
        self.check_input()  # Calls check_input() only once per update
        if self.is_fleeing:
            move_speed = 10
            self.flee_steps += 1
        else:
            move_speed = self.speed
            self.flee_steps = self.max_flee_steps
        # move_speed = 8 if self.is_fleeing else 10
        self.check_move(move_speed)
        
        # if self.is_fleeing:
        #     while self.flee_steps < self.max_flee_steps:
        #         self.flee_steps += 1
        # else:
        #     self.flee_steps = self.max_flee_steps

        if not any(self.keyListener.key_pressed(key) for key in [pygame.K_q, pygame.K_d, pygame.K_z, pygame.K_s, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN] ) :
            self.is_fleeing = False
            self.flee_steps = 0
            self.speed = 1
        super().update()

    def check_move(self, move_speed) -> None:
        """Check player movement based on key input and handle collisions."""
        if self.animation_walk is False:
            temp_hitbox = self.hitbox.copy()
            # move_speed = 8 if self.is_fleeing else 10  # Adjusted speed
            
            # Map size (to be adjusted according to your game)
            map_width = self.screen.width  # Map width
            map_height = self.screen.height  # Map height

            if self.keyListener.key_pressed(pygame.K_q) or self.keyListener.key_pressed(pygame.K_LEFT):  # Left
                self.flee_steps += 1
                if temp_hitbox.x - move_speed >= 0:  # Prevents going out of bounds on the left
                    temp_hitbox.x -= move_speed
                    # self.flee_steps += 1
                    if not self.check_collisions(temp_hitbox):
                        self.check_collisions_switchs(temp_hitbox)
                        self.move_left()
                    #     if self.is_fleeing:
                    #         self.flee_steps += 1
                    # else:
                    #     self.direction = "left"

            elif self.keyListener.key_pressed(pygame.K_d) or self.keyListener.key_pressed(pygame.K_RIGHT):  # Right
                self.flee_steps += 1
                if temp_hitbox.x + temp_hitbox.width + move_speed <= map_width:  # Prevents going out of bounds on the right
                    temp_hitbox.x += move_speed
                    
                    if not self.check_collisions(temp_hitbox):
                        self.check_collisions_switchs(temp_hitbox)
                        self.move_right()
                    #     if self.is_fleeing:
                    #         self.flee_steps += 1
                    # else:
                    #     self.direction = "right"

            elif self.keyListener.key_pressed(pygame.K_z) or self.keyListener.key_pressed(pygame.K_UP):  # Up
                self.flee_steps += 1
                if temp_hitbox.y - move_speed >= 0:  # Prevents going out of bounds at the top
                    temp_hitbox.y -= move_speed
                    if not self.check_collisions(temp_hitbox):
                        self.check_collisions_switchs(temp_hitbox)
                        self.move_up()
                    #     if self.is_fleeing:
                    #         self.flee_steps += 1
                    # else:
                    #     self.direction = "up"

            elif self.keyListener.key_pressed(pygame.K_s) or self.keyListener.key_pressed(pygame.K_DOWN):  # Down
                self.flee_steps += 1
                if temp_hitbox.y + temp_hitbox.height + move_speed <= map_height:  # Prevents going out of bounds at the bottom
                    temp_hitbox.y += move_speed
                    if not self.check_collisions(temp_hitbox):
                        self.check_collisions_switchs(temp_hitbox)
                        self.move_down()
                    #     if self.is_fleeing:
                    #         self.flee_steps += 1
                    # else:
                    #     self.direction = "down"

    def add_switchs(self, switchs: list[Switch]):
        """Assigns a list of switches to the player."""
        self.switchs = switchs

    def check_collisions_switchs(self, temp_hitbox):
        """Check if the player collides with a switch and updates the map change if necessary."""
        if self.switchs:
            for switch in self.switchs:
                if switch.check_collision(temp_hitbox):
                    self.change_map = switch

    def add_collisions(self, collisions):
        """Assigns collision objects to the player."""
        self.collisions = collisions

    def check_collisions(self, temp_hitbox: pygame.Rect):
        """Checks if the player collides with an object."""
        for collision in self.collisions:
            if temp_hitbox.colliderect(collision):
                return True
        return False

    def check_input(self):
        """Checks player input for bike switch and fleeing mode."""
        if self.keyListener.key_pressed(pygame.K_b):  # Toggle bike mode
            self.switch_bike()

        # Enable/disable fleeing mode
        if self.keyListener.key_pressed(pygame.K_f):  # Press F to flee
            # self.flee_steps = 0
            self.is_fleeing = True
            self.speed = 2
        
        elif self.keyListener.key_pressed(pygame.K_SPACE):  # Release space to stop fleeing
            self.is_fleeing = False
            # self.flee_steps = 0
            self.speed = 1

        if self.keyListener.key_pressed(pygame.K_ESCAPE):  # Release space to stop fleeing
            blabla = menu.Menu(self.screen).display()
        
        

    def switch_bike(self, deactive=False):
        """Toggles bike mode on/off."""
        if self.speed == 1 and not deactive:  # Activate bike mode
            self.speed = 2
            self.all_images = self.get_all_images(self.spritesheet_bike)
        else:  # Deactivate bike mode
            self.speed = 1
            self.all_images = self.get_all_images(self.spritesheet)

        self.keyListener.remove_key(pygame.K_b)  # Prevents continuous key press

    def start_battle(self, battle_zones):
        """Checks if the player enters a battle zone and starts a battle."""
        for battle_zone in battle_zones:
            if self.rect.colliderect(battle_zone):
                print("Pokémon battle starts! in start_battle of player")
                battle_screen = BattleScreen(self.screen, self)
                # battle_screen = InFight(self.screen, self.player_name).display()
                battle_screen.run()
                break

    def battle(self):
        """Starts a battle manually."""
        print("Pokémon battle starts! in battle of player")
        battle_screen = InFight(self.screen, self.player_name).display()
        self.in_battle = False


    


