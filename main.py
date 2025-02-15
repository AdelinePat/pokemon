import pygame
from codes.game import Game
from codes.menu import Menu
from codes.screen import Screen
from codes.sounds import Sounds

pygame.init()
sounds = Sounds()
sounds.play_background_music(volume=0.1)

if __name__ == "__main__":
    screen = Screen()
    menu = Menu(screen)
    
    menu.display()
    game = Game()
    game.run()
    
    