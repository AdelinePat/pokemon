import pygame
from front_end.gameplay.entity import Entity
from .keylistener import KeyListener
from front_end.screen import Screen
from .switch import Switch
# from front_end.menu.name_input import NameInput
from front_end.gameplay.battlescreen import BattleScreen
from front_end.in_fight.in_fight import InFight
from front_end.menu.pause_menu import PauseMenu


class Player(Entity):
    def __init__(self, keylistener: KeyListener, screen: Screen, x: int, y: int, player_name: str, pokemon: object):
        super().__init__(keylistener, screen, x, y)
        self.switchs: list[Switch] | None = None  # List of switches the player can activate
        self.change_map = None  # Stores the switch that changes the map
        self.collisions = None  # List of collision objects
        self.spritesheet_bike = pygame.image.load("assets/sprite/hero_01_red_m_cycle_roll.png")  # Bike sprite
        self.player_name = player_name  # Stores the player's name
        self.name = player_name
        self.is_fleeing = False  # Indicates if the player is fleeing
        self.speed = 1  # Default walking speed
        self.active_pokemon = pokemon
        self.flee_steps = 0  # Number of steps taken while fleeing
        self.max_flee_steps = 100  # Maximum number of fleeing steps
        self.pause_menu = False

    def update(self) -> None:
        self.check_input()
        self.check_move()
        super().update()

    def check_move(self) -> None:
        if self.keyListener.key_pressed(pygame.K_ESCAPE):
            self.player_name, self.active_pokemon = PauseMenu(self.player_name, self.active_pokemon, self.screen).display()
            self.keyListener.remove_key(pygame.K_ESCAPE)      

        if self.animation_walk is False:
            temp_hitbox = self.hitbox.copy()
            if self.keyListener.key_pressed(pygame.K_q)or self.keyListener.key_pressed(pygame.K_LEFT):
                temp_hitbox.x -= 16
                if not self.check_collisions(temp_hitbox):
                    self.check_collisions_switchs(temp_hitbox)
                    self.move_left()
                else:
                    self.direction = "left"
            elif self.keyListener.key_pressed(pygame.K_d)or self.keyListener.key_pressed(pygame.K_RIGHT):
                temp_hitbox.x += 16
                if not self.check_collisions(temp_hitbox):
                    self.check_collisions_switchs(temp_hitbox)
                    self.move_right()
                else:
                    self.direction = "right"
            elif self.keyListener.key_pressed(pygame.K_z)or self.keyListener.key_pressed(pygame.K_UP):
                temp_hitbox.y -= 16
                if not self.check_collisions(temp_hitbox):
                    self.check_collisions_switchs(temp_hitbox)
                    self.move_up()
                else:
                    self.direction = "up"
            elif self.keyListener.key_pressed(pygame.K_s)or self.keyListener.key_pressed(pygame.K_DOWN):
                temp_hitbox.y += 16
                if not self.check_collisions(temp_hitbox):
                    self.check_collisions_switchs(temp_hitbox)
                    self.move_down()
                else:
                    self.direction = "down"

    def add_switchs(self, switchs: list[Switch]):
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
           

    def switch_bike(self, deactive=False):
        if self.speed == 1 and not deactive:
            self.speed = 2
            self.all_images = self.get_all_images(self.spritesheet_bike)
        else:
            self.speed = 1
            self.all_images = self.get_all_images(self.spritesheet)
        self.keyListener.remove_key(pygame.K_b)

    def start_battle(self, battle_zones):
        """Checks if the player enters a battle zone and starts a battle."""
        for battle_zone in battle_zones:
            if self.rect.colliderect(battle_zone):
                print("Pokémon battle starts! dans start battle de player")
                battle_screen = BattleScreen(self.screen, self)
                # battle_screen = InFight(self.screen, self.player_name).display()
                battle_screen.run()
                break

    def battle(self):
        """Starts a battle manually."""
        print("Pokémon battle starts! dans battle de player")
        # battle_screen = BattleScreen(self.screen, self)
        # battle_screen.run()
        battle_screen = InFight(self.screen, self.player_name).display()
        self.in_battle = False