import pygame
import sys

from front_end.gameplay import game
# from front_end.menu.name_input import NameInput  

from .select_player import SelectPlayer
from .change_pokemon import ChangePokemon
from __settings__ import MAIN_MENU_BACKGROUND1, LIGHT_GREEN, REGULAR_FONT
from front_end.sounds import Sounds
from front_end.menu.util_tool import UtilTool
from back_end.data_access.pokemon_pokedex_service import get_all_pokemons_from_pokedex
from back_end.data_access.pokemon_pokedex_service import get_first_pokemon

sounds = Sounds()

class PauseMenu:
    def __init__(self, player, pokemon, screen, pokemon_list=[]):
        """
        Initialize the menu with the screen, font, options, and selected index.
        """
        self.screen = screen
        self.font = pygame.font.Font(None, 50)  # Set the font for menu text
        self.options = ["Change pokemon", "Change player", "Continue", "Exit"]  # Menu options
        self.selected_index = 0  # Index of the currently selected option
        self.running = True  # Controls the menu loop
        self.player = player
        self.pokemon = pokemon
        self.util = UtilTool()
        if not pokemon_list:
            self.pokemons = get_all_pokemons_from_pokedex(self.player)
        else:
            self.pokemons = pokemon_list


    # def draw_text(self, text, x, y, color=(255, 255, 255)):
    #     """
    #     Renders text and displays it at the given (x, y) position.
    #     """
    #     surface = self.font.render(text, True, color)
    #     rect = surface.get_rect(center=(x, y))
    #     self.screen.get_display().blit(surface, rect)

    def display(self):
        """
        Main menu loop that displays options and handles user input.
        """
        while self.running:
            self.screen.update()
            self.screen.get_display().fill((0, 0, 0))

            self.screen.set_background_display(MAIN_MENU_BACKGROUND1)
            
            font_size = self.screen.height // 10
            self.util.draw_text("Pause Menu", REGULAR_FONT, font_size, self.screen,\
                                (self.screen.width//2, self.screen.height // 10*2), LIGHT_GREEN)  # Draw the title

            # Draw menu options
            for i, option in enumerate(self.options):
                color = LIGHT_GREEN if i == self.selected_index else (255, 255, 255)  # Highlight selected option
                # self.draw_text(option, 600, 300 + i * 60, color)
                self.util.draw_text(option, REGULAR_FONT, font_size - 14, self.screen,\
                                (self.screen.width//2, self.screen.height // 10*3.5 + i*100), color)

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
                                self.pokemon = ChangePokemon(self.player, self.screen).display()
                                # player_name, pokemon = name_input.get_name()
                                # print(player_name, pokemon)
                                import front_end.gameplay.game as gameplay
                                game = gameplay.Game(self.screen, self.player, self.pokemon)
                                
                                # Stop the opening music and start the map music
                                sounds.stop_background_music()  # Correct the method name here
                                sounds.play_map_music()  # Play map music
                                # return self.player, self.pokemon
                                # return self.player, self.pokemon
                                # game.run()
                            case 1:
                                self.player = SelectPlayer(self.screen).display()
                                self.pokemons = get_all_pokemons_from_pokedex(self.player)
                                self.pokemon = get_first_pokemon(self.player)
                            case 2:
                                # select_player = SelectPlayer(self.screen).display()
                                # game = Game(self.screen, select_player)
                                
                                # print(select_player)

                                # Stop the opening music and start the map music
                                sounds.stop_background_music()  # Correct the method name here
                                sounds.play_map_music()  # Play map music
                                # game.run()
                                return self.player, self.pokemon
                            case 3:
                                pygame.quit()
                                sys.exit()
