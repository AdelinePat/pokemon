import pygame
import sys

from .name_input import NameInput  
from front_end.gameplay.game import Game
from .select_player import SelectPlayer
from __settings__ import MAIN_MENU_BACKGROUND1


class Menu:
    def __init__(self, screen):
        """
        Initialize the menu with the screen, font, options, and selected index.
        """
        self.screen = screen
        self.font = pygame.font.Font(None, 50)  # Set the font for menu text
        self.options = ["Start Game", "Resume Game", "Exit"]  # Menu options
        self.selected_index = 0  # Index of the currently selected option
        self.running = True  # Controls the menu loop

    def draw_text(self, text, x, y, color=(255, 255, 255)):
        """
        Renders text and displays it at the given (x, y) position.
        """
        surface = self.font.render(text, True, color)
        rect = surface.get_rect(center=(x, y))
        self.screen.get_display().blit(surface, rect)

    

    def display(self):
        """
        Main menu loop that displays options and handles user input.
        """
        while self.running:
            self.screen.update()
            self.screen.get_display().fill((0, 0, 0))

            self.screen.set_background_display(MAIN_MENU_BACKGROUND1)

            self.draw_text("Menu Principal", 600, 150, (255, 255, 0))  # Draw the title

            # Draw menu options
            for i, option in enumerate(self.options):
                color = (255, 255, 0) if i == self.selected_index else (255, 255, 255)  # Highlight selected option
                self.draw_text(option, 600, 300 + i * 60, color)

            pygame.display.flip()  # Refresh the screen

            # Handle user input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # If user closes the window
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  # Navigate down
                        self.selected_index = (self.selected_index + 1) % len(self.options)
                    elif event.key == pygame.K_UP:  # Navigate up
                        self.selected_index = (self.selected_index - 1) % len(self.options)
                    elif event.key == pygame.K_RETURN:  # Select an option
                        match self.selected_index:
                            case 0:  # Start a new game
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
