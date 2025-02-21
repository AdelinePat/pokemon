import pygame
from front_end.menu.menu import Menu
from front_end.screen import Screen
from front_end.sounds import Sounds

pygame.init()
sounds = Sounds()
sounds.play_background_music(volume=0.1)

if __name__ == "__main__":
    screen = Screen()
    menu = Menu(screen)
    
    menu.display()
    
    