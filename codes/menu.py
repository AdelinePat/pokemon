import pygame
import sys

from codes.name_input import NameInput  
from codes.game import Game
from codes.select_player import SelectPlayer



class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 50)
        self.options = ["Start Game", "Resume Game", "Exit"]
        self.selected_index = 0
        self.running = True

    def draw_text(self, text, x, y, color=(255, 255, 255)):
        surface = self.font.render(text, True, color)
        rect = surface.get_rect(center=(x, y))
        self.screen.get_display().blit(surface, rect)

    def display(self):
        while self.running:
            self.screen.update()
            self.screen.get_display().fill((0, 0, 0))

            self.draw_text("Menu Principal", 600, 150, (255, 255, 0))

            for i, option in enumerate(self.options):
                color = (255, 255, 0) if i == self.selected_index else (255, 255, 255)
                self.draw_text(option, 600, 300 + i * 60, color)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.selected_index = (self.selected_index + 1) % len(self.options)
                    elif event.key == pygame.K_UP:
                        self.selected_index = (self.selected_index - 1) % len(self.options)
                    elif event.key == pygame.K_RETURN:
                        match self.selected_index:
                            case 0:
                                name_input = NameInput(self.screen)
                                player_name, pokemon = name_input.get_name()
                                print(player_name, pokemon)
                                game = Game(self.screen, player_name)
                                game.run()
                            case 1:
                                select_player = SelectPlayer(self.screen).display()
                                game = Game(self.screen, select_player)
                                print(select_player)
                                game.run()
                                # game = Game(self.screen, "test")
                                # game.run()
                                # print("Reprendre la partie (à faire)")
                            case 2:
                                pygame.quit()
                                sys.exit()