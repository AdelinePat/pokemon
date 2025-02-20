import pygame
import sys
from front_end.menu.util_tool import UtilTool
from __settings__ import BATTLE_BACKGROUND, BATTLE_FLOOR, REGULAR_FONT, LIGHT_GREEN, DARK_GREEN
import math


class AttackMenu:
    def __init__(self, screen, pokemon, pokemon_enemy):
        """
        Initialize the menu with the screen, font, options, and selected index.
        """
        self.screen = screen
        self.pokemon = pokemon
        self.font = pygame.font.Font(None, 50)  # Set the font for menu text
        self.options = self.pokemon.type + ["Back"] # Menu options
        self.selected_index = 0  # Index of the currently selected option
        self.running = True  # Controls the menu loop
        self.util = UtilTool()
        
        self.pokemon_enemy = pokemon_enemy

    def display(self):
        """
        Main menu loop that displays options and handles user input.
        """
        battle_floor = self.util.load_image(BATTLE_FLOOR)
        battle_floor2 = pygame.transform.flip(battle_floor, True, False)
        pokemon = self.util.load_image(self.pokemon.get_back_image())
        pokemon_enemy = self.util.load_image(self.pokemon_enemy.get_image())
        time_count = 0
        var_x = 5
        var_y = 5
        speed = 1.5
        win = False
        
        while self.running:
            self.screen.update()
            if not win:
                time_count += speed
                x_movement = int(var_y * math.sin(time_count * 0.1))
                y_movement = int(var_x * math.sin(time_count * 0.08))
            self.util.display_assets_and_background_in_fight(self.screen, x_movement, y_movement, battle_floor, battle_floor2, pokemon_enemy, pokemon)

            self.util.draw_option_screen(self.screen)

            # Draw menu options
            for i, option in enumerate(self.options):
                color = LIGHT_GREEN if i == self.selected_index else DARK_GREEN  # Highlight selected option
                # self.draw_text(option, self.screen.width//2 + i * 200, self.screen.height//8*7  , color)
                self.util.draw_text(option, REGULAR_FONT, self.screen.width //30, self.screen,\
                                    (self.screen.width//2 + i * 200, self.screen.height//8*7), color)

            pygame.display.flip()  # Refresh the screen

            # Handle user input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # If user closes the window
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN or event.key == pygame.K_RIGHT:  # Navigate down
                        self.selected_index = (self.selected_index + 1) % len(self.options)
                    elif event.key == pygame.K_UP or event.key == pygame.K_LEFT:  # Navigate up
                        self.selected_index = (self.selected_index - 1) % len(self.options)
                    elif event.key == pygame.K_RETURN:  # Select an option
                        return self.options[self.selected_index]

   