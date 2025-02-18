import pygame
import sys
from front_end.menu.util_tool import UtilTool
from __settings__ import BATTLE_BACKGROUND, BATTLE_FLOOR, REGULAR_FONT, LIGHT_GREEN, DARK_GREEN
import math


class InfoMenu:
    def __init__(self, screen, pokemon, pokemon_enemy):
        """
        Initialize the menu with the screen, font, options, and selected index.
        """
        self.screen = screen
        self.pokemon = pokemon
        self.pokemon_enemy = pokemon_enemy
        self.font = pygame.font.Font(None, 50)  # Set the font for menu text
        self.options = [f"{self.pokemon.name}", f"{self.pokemon_enemy.name}", "Back"]  # Menu options
        self.selected_index = 0  # Index of the currently selected option
        self.running = True  # Controls the menu loop
        self.util = UtilTool()
        
    def draw_text(self, text, x, y, color=(255, 255, 255)):
        """
        Renders text and displays it at the given (x, y) position.
        """
        surface = self.font.render(text, True, color)
        rect = surface.get_rect(center=(x, y))
        self.screen.get_display().blit(surface, rect)

    def load_image(self, image):
        return pygame.image.load(image)
    
    def display_asset_battle(self, image, scale_x, scale_y, x, y):
        image.set_colorkey((255, 255, 255))
        battle_floor = pygame.transform.scale(image, (scale_x, scale_y))
        battle_floor_rect = battle_floor.get_rect(center = (x, y))
        self.screen.display.blit(battle_floor, battle_floor_rect)

    # def display_pokemon_battle(self, image, scale_x, scale_y, x, y):
    #     image.set_colorkey((255, 255, 255))
    #     battle_floor = pygame.transform.scale(image, (scale_x, scale_y))
    #     battle_floor_rect = battle_floor.get_rect(midbottom = (x, y))
    #     self.screen.display.blit(battle_floor, battle_floor_rect)

    def display_assets_and_background(self,x_movement, y_movement, battle_floor, battle_floor2, pokemon_enemy, pokemon):
        
        
        self.screen.set_background_without_black(BATTLE_BACKGROUND)
        floor1 = self.display_asset_battle(battle_floor, self.screen.width // 5, self.screen.height // 7, self.screen.width // 10 * 7.5, self.screen.height // 7 * 3.2)
        floor = self.display_asset_battle(battle_floor2, self.screen.width // 3, self.screen.height // 5, self.screen.width // 10 * 2.5, self.screen.height // 7 * 6.6)

        enemy = self.display_asset_battle(pokemon_enemy, self.screen.width //6, self.screen.width //6, self.screen.width // 10 * 7.5 + x_movement, self.screen.height // 7 * 3)
        my_pokemon = self.display_asset_battle(pokemon, self.screen.width // 3, self.screen.width // 3, self.screen.width // 10 * 2.5, self.screen.height // 7 * 6.4 + y_movement)


    

    def display(self):
        """
        Main menu loop that displays options and handles user input.
        """
        battle_floor = self.load_image(BATTLE_FLOOR)
        battle_floor2 = pygame.transform.flip(battle_floor, True, False)
        pokemon = pygame.transform.flip(self.load_image(self.pokemon.image), True, False)
        pokemon_enemy = self.load_image(self.pokemon_enemy.image)
        time_count = 0
        var_x = 5
        var_y = 5
        speed = 1.5
        win = False
        what_to_display = 3

        while self.running:
            self.screen.update()
            if not win:
                time_count += speed
                x_movement = int(var_y * math.sin(time_count * 0.1))
                y_movement = int(var_x * math.sin(time_count * 0.08))
            self.display_assets_and_background(x_movement, y_movement, battle_floor, battle_floor2, pokemon_enemy, pokemon)

            self.util.draw_option_screen(self.screen)

            if what_to_display == 0:
                self.draw_info_screen(self.pokemon)
            elif what_to_display == 1:
                what_to_display = 1
                self.draw_info_screen(self.pokemon_enemy)

            # self.options = [f"{self.bag.get_potion()} Potions", f"{self.bag.get_pokeball()} Pokeball", "Back"] 
            # Draw menu options
            for i, option in enumerate(self.options):
                color = LIGHT_GREEN if i == self.selected_index else DARK_GREEN  # Highlight selected option
                self.draw_text(option, self.screen.width//2 + i * 200, self.screen.height//8*7  , color)

            pygame.display.flip()  # Refresh the screen

            # Handle user input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # If user closes the window
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    # return
                    if event.key == pygame.K_DOWN or event.key == pygame.K_RIGHT:  # Navigate down
                        self.selected_index = (self.selected_index + 1) % len(self.options)
                    elif event.key == pygame.K_UP or event.key == pygame.K_LEFT:  # Navigate up
                        self.selected_index = (self.selected_index - 1) % len(self.options)
                    elif event.key == pygame.K_RETURN:  # Select an option
                        match self.selected_index:
                            case 0:  # Start a new game
                                what_to_display = 0
                                # self.draw_info_screen(self.pokemon)
                            case 1:
                                what_to_display = 1
                                # self.draw_info_screen(self.pokemon_enemy)
                            case 2:
                                return


    def draw_info_screen(self, actual_pokemon):
        # self.util.draw_color_filter(self.screen)
        self.util.draw_window_with_background(self.screen, self.screen.width //2.5, self.screen.height //2.5)
        font_size = self.screen.height // 20
        x  = self.screen.width //2
        y = self.screen.height // 2
        
        self.util.draw_text(f"{actual_pokemon.name}",\
                              REGULAR_FONT, font_size , self.screen, (x, y - font_size*2))
        self.util.draw_text(f"Level : {str(actual_pokemon.get_level())}",\
                                REGULAR_FONT, font_size , self.screen, (x, y - font_size))
        self.util.draw_text(f"Strength : {str(actual_pokemon.get_strength())}",\
                              REGULAR_FONT, font_size , self.screen, (x, y ))
        self.util.draw_text(f"Defense : {str(actual_pokemon.get_defense())}",\
                              REGULAR_FONT, font_size , self.screen, (x, y + font_size))
        self.util.draw_text(f"Type : {str(", ".join(actual_pokemon.type))}",\
                              REGULAR_FONT, font_size , self.screen, (x, y + font_size*2))
        


        # \
        #                     \nLevel : {str(actual_pokemon.get_level())}\
        #                     \nStrength : {str(self.pokemon.get_strength())}\
        #                     \nDefense : {str(self.pokemon.get_defense())}\
        #                     \nType : {str(", ".join(self.pokemon.type))}"
        # self.util.draw_text(f"You gained {self.pokemon.get_xp_gained(self.pokemon_enemy)} XP", REGULAR_FONT, font_size, self.screen, (x, y))
        # self.util.draw_text(f"Total XP : {self.pokemon.get_xp()}", REGULAR_FONT, font_size, self.screen, (x, y + font_size*2))