import pygame
import sys
from button import Button
from screen import Screen

# Initialisation de Pygame
pygame.init()

# Définition des états du jeu
STATE_MAIN_MENU = "main_menu"
STATE_OPTIONS_MENU = "options_menu"
STATE_PLAYING = "playing"

class Game(Screen):
    def __init__(self):
        super().__init__()
        self.state = STATE_MAIN_MENU
        self.main_menu = MainMenu(self)
        self.options_menu = OptionsMenu(self)
        self.playing = Playing(self)

    def run(self):
        while True:
            if self.state == STATE_MAIN_MENU:
                self.main_menu.run()
            elif self.state == STATE_OPTIONS_MENU:
                self.options_menu.run()
            elif self.state == STATE_PLAYING:
                self.playing.run()
