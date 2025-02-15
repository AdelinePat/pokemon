import pygame
from game import Game
from menu import Menu
from screen import Screen
from sounds import Sounds

pygame.init()
sounds = Sounds()
sounds.play_background_music(volume=0.1)

if __name__ == "__main__":
    screen = Screen()
    menu = Menu(screen)
    
    menu.display()
    game = Game()
    game.run()
    
    