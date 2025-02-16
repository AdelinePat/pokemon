import pygame
import math

import pygame
import sys
from __settings__ import BATTLE_BACKGROUND, BATTLE_FLOOR, REGULAR_FONT
from back_end.data_access.pokemon_pokedex_service import get_first_pokemon
from back_end.data_access.wild_pokemons import get_random_wild_pokemon
from back_end.data_access.bag_pokedex_service import get_bag_from_pokedex
from back_end.models.fight import Fight
from front_end.menu.util_tool import UtilTool

class InFight():
    def __init__(self, screen, player):
        """
        Initialize the menu with the screen, font, options, and selected index.
        """
        self.screen = screen
        self.font = pygame.font.Font(None, 50)  # Set the font for menu text
        self.options = ["Attack", "Bag", "Run away"]  # Menu options
        self.selected_index = 0  # Index of the currently selected option
        self.running = True  # Controls the menu loop
        self.player = player
        self.pokemon = get_first_pokemon(self.player)
        self.pokemon_enemy = get_random_wild_pokemon()
        self.bag = get_bag_from_pokedex(self.player)
        self.fight = Fight(self.pokemon, self.pokemon_enemy)
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

    def display(self):
        pass

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
        
        player_turn = False
        if self.fight.is_player_first():
            player_turn = True

        while self.running: 
            #DISPLAY
            self.screen.update()
            self.screen.get_display().fill((0, 0, 0))

            self.screen.set_background_without_black(BATTLE_BACKGROUND)

            if not win:
                time_count += speed
                x_movement = int(var_y * math.sin(time_count * 0.1))
                y_movement = int(var_x * math.sin(time_count * 0.08))


            floor1 = self.display_asset_battle(battle_floor, self.screen.width // 5, self.screen.height // 7, self.screen.width // 10 * 7.5, self.screen.height // 7 * 3.2)
            floor = self.display_asset_battle(battle_floor2, self.screen.width // 3, self.screen.height // 5, self.screen.width // 10 * 2.5, self.screen.height // 7 * 6.6)

            enemy = self.display_asset_battle(pokemon_enemy, self.screen.width //6, self.screen.width //6, self.screen.width // 10 * 7.5 + x_movement, self.screen.height // 7 * 3)
            my_pokemon = self.display_asset_battle(pokemon, self.screen.width // 3, self.screen.width // 3, self.screen.width // 10 * 2.5, self.screen.height // 7 * 6.4 + y_movement)
            
            
            # Draw menu options
            for i, option in enumerate(self.options):
                color = (255, 255, 0) if i == self.selected_index else (255, 255, 255)  # Highlight selected option
                self.draw_text(option, self.screen.width//2 + i * 200, self.screen.height//8*7  , color)

            if win:
                # self.running = False
                # self.screen.set_background_without_black(BATTLE_BACKGROUND)
                self.draw_win_screen()

            pygame.display.flip()  # Refresh the screen
            
            
            # Handle user input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # If user closes the window
                    pygame.quit()
                    sys.exit()
                    
                if player_turn:
                    if event.type == pygame.KEYDOWN:

                        if event.key == pygame.K_ESCAPE:
                            self.running = False

                        if event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN:  # Navigate down
                            self.selected_index = (self.selected_index + 1) % len(self.options)
                        elif event.key == pygame.K_LEFT or event.key == pygame.K_UP:  # Navigate up
                            self.selected_index = (self.selected_index - 1) % len(self.options)
                        elif event.key == pygame.K_RETURN:  # Select an option
                            match self.selected_index:
                                case 0:  # Start a new game
                                    attack_type = self.pokemon.type[0]
                                    #TODO create menu returning attack_type
                                    
                                    self.fight.player_attack(attack_type)
                                    if self.pokemon_enemy.get_hp() > 0 :
                                        player_turn = False
                                    else:
                                        win = True
                                        #TODO menu end fight , xp gained...etc

                                    
                                    print("attaque")
                                    # name_input = NameInput(self.screen)
                                    # player_name, pokemon = name_input.get_name()
                                    # print(player_name, pokemon)
                                    # # game = Game(self.screen, player_name)
                                    # game.run()
                                    
                                case 1:
                                    print("sac ouvert")
                                    #TODO menu for bag 

                                    # # select_player = SelectPlayer(self.screen).display()
                                    # # game = Game(self.screen, select_player)
                                    # print(select_player)
                                    # game.run()
                                    # # game = Game(self.screen, "test")
                                    # # game.run()
                                    # # print("Reprendre la partie (à faire)")
                                    player_turn = False
                                case 2:
                                    print("fuite")
                                    player_turn = False
                                    # pygame.quit()
                                # sys.exit()
                else:
                    
                    self.fight.bot_attack()
                    if self.pokemon.get_hp() > 0 :
                        player_turn = True
                    else:
                        #TODO game_over screen/new menu and allows events for player
                        pass
            

    def draw_win_screen(self):
        # self.util.draw_color_filter(self.screen)
        self.util.draw_window_with_background(self.screen)
        font_size = self.screen.height // 18
        x  = self.screen.width //2
        y = self.screen.height // 2
        self.util.draw_text("You won the fight!", REGULAR_FONT, font_size , self.screen, (x, y - font_size*2))
        self.util.draw_text(f"You gained {self.pokemon.get_xp_gained(self.pokemon_enemy)} XP", REGULAR_FONT, font_size, self.screen, (x, y))
        self.util.draw_text(f"Total XP : {self.pokemon.get_xp()}", REGULAR_FONT, font_size, self.screen, (x, y + font_size*2))
