import pygame
from display.models.sounds import Sounds
from display.models.menu import Menu

pygame.init()
sounds = Sounds()
sounds.play_background_music(volume=0.1)

if __name__ == "__main__":
    menu = Menu()
    menu.display()

