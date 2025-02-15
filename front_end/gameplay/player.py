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
        self.switchs: list[Switch] | None = None  # List of switches the player can activate
        self.change_map = None  # Stores the switch that changes the map
        self.collisions = None  # List of collision objects
        self.spritesheet_bike = pygame.image.load("assets/sprite/hero_01_red_m_cycle_roll.png")  # Bike sprite
        self.player_name = player_name  # Stores the player's name
        self.name = player_name
        self.is_fleeing = False  # Indicates if the player is fleeing
        self.speed = 1  # Default walking speed

    def update(self) -> None:
        """Update player state, checking inputs and movement."""
        self.check_input()  # Calls check_input() only once per update
        self.check_move()
        super().update()

    def check_move(self) -> None:
        """Check player movement based on key input and handle collisions."""
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
            self.is_fleeing = True
            self.speed = self.speed if self.speed == 2 else 1
        elif not self.keyListener.key_pressed(pygame.K_f):  # Release F key
            self.is_fleeing = False

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
                print("Pokémon battle starts!")
                battle_screen = BattleScreen(self.screen, self)
                battle_screen.run()
                break

    def battle(self):
        """Starts a battle manually."""
        print("Pokémon battle starts!")
        battle_screen = BattleScreen(self.screen, self)
        battle_screen.run()
        self.in_battle = False
