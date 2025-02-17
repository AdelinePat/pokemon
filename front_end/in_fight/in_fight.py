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
from front_end.menu.bagmenu import BagMenu
from front_end.menu.attack_type_menu import AttackMenu
from front_end.menu.infomenu import InfoMenu

class InFight():
    def __init__(self, screen, player):
        """
        Initialize the menu with the screen, font, options, and selected index.
        """
        self.screen = screen
        self.pokemon_enemy = get_random_wild_pokemon()
        # option_name = f"{self.pokemon_enemy.name} info"
        self.font = pygame.font.Font(None, 50)  # Set the font for menu text
        self.options = ["Attack", "Bag","Info", "Run away"]  # Menu options
        self.bag_option = ["potions", "pokeball", "retour"]
        self.selected_index = 0  # Index of the currently selected option
        self.running = True  # Controls the menu loop
        self.player = player
        self.pokemon = get_first_pokemon(self.player)
        
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

    def display_assets_and_background(self,x_movement, y_movement, battle_floor, battle_floor2, pokemon_enemy, pokemon):
        self.screen.set_background_without_black(BATTLE_BACKGROUND)
        floor1 = self.display_asset_battle(battle_floor, self.screen.width // 5, self.screen.height // 7, self.screen.width // 10 * 7.5, self.screen.height // 7 * 3.2)
        floor = self.display_asset_battle(battle_floor2, self.screen.width // 3, self.screen.height // 5, self.screen.width // 10 * 2.5, self.screen.height // 7 * 6.6)

        enemy = self.display_asset_battle(pokemon_enemy, self.screen.width //6, self.screen.width //6, self.screen.width // 10 * 7.5 + x_movement, self.screen.height // 7 * 3)
        my_pokemon = self.display_asset_battle(pokemon, self.screen.width // 3, self.screen.width // 3, self.screen.width // 10 * 2.5, self.screen.height // 7 * 6.4 + y_movement)

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
        message_damage = None
        message_attack = None
        
        player_turn = False
        if self.fight.is_player_first():
            player_turn = True

        while self.running: 
            
            #DISPLAY
            self.screen.update()
            # self.screen.get_display().fill((0, 0, 0))
            if not win:
                time_count += speed
                x_movement = int(var_y * math.sin(time_count * 0.1))
                y_movement = int(var_x * math.sin(time_count * 0.08))
            self.display_assets_and_background(x_movement, y_movement, battle_floor, battle_floor2, pokemon_enemy, pokemon)
            
            self.util.draw_option_screen(self.screen)
            # Draw menu options
            for i, option in enumerate(self.options):
                color = (255, 255, 0) if i == self.selected_index else (0,0,0)  # Highlight selected option
                self.draw_text(option, self.screen.width//2 + i * 150, self.screen.height//8*7  , color)

            if win:
                if self.pokemon.get_hp() == 0:
                    self.draw_win_bot_screen()
                else:
                    # self.screen.update()
                    # self.running = False
                    # self.screen.set_background_without_black(BATTLE_BACKGROUND)
                    self.draw_win_player_screen()

            if message_attack and message_damage and not win:
                now_time = pygame.time.get_ticks()
                message_time = 0
                while message_time - now_time < 1000:
                    message_time = pygame.time.get_ticks()
                    self.util.draw_info_attack_screen(self.screen, message_attack, message_damage)
                    pygame.display.update()

                message_attack = None
                message_damage = None
                
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
                                    if win:
                                        self.selected_index = 3
                                    else:
                                        attack_type = AttackMenu(self.screen, self.pokemon, self.pokemon_enemy).display()
                                        if attack_type == "Retour":
                                            player_turn = True
                                        else:
                                            print("attaque")
                                            self.fight.player_attack(attack_type)
                                            if self.pokemon_enemy.get_hp() > 0:
                                                message_attack = self.fight.fightinfo.set_who_attack_message(self.pokemon)
                                                message_damage = self.fight.fightinfo.set_damage_message()
                                                player_turn = False
                                            else:
                                                win = True
                                            #TODO menu end fight , xp gained...etc
                                        
                                case 1:
                                    if win:
                                        self.selected_index = 3
                                    else:
                                        print(f"HP max : {self.pokemon.get_hp_max()}")
                                        self.pokemon.set_damage_hp(self.pokemon.get_hp() - 30)
                                        print(f"HP actuel : {self.pokemon.get_hp() }")
                                        bag_option = BagMenu(self.screen, self.pokemon, self.pokemon_enemy, self.bag).display()
                                        if bag_option:
                                            match bag_option:
                                                case "Potions":
                                                    another_option = self.fight.use_potion(self.pokemon, self.bag)
                                                    if another_option:
                                                        player_turn == True
                                                    else:
                                                        player_turn = False
                                                case "Pokeball":
                                                    another_option = self.fight.use_pokeball(self.player, self.bag, self.pokemon, self.pokemon_enemy)
                                                    if another_option:
                                                        player_turn == True
                                                    else:
                                                        player_turn = False
                                                case "Retour":
                                                    player_turn = True

                                case 2:
                                    if win:
                                        self.selected_index = 3
                                    else:
                                        print("Info")
                                        InfoMenu(self.screen, self.pokemon, self.pokemon_enemy).display()
                                        player_turn = True
                                    
                                case 3:
                                    if win:
                                        return
                                    else:
                                        print("fuite")
                                        self.fight.run_away()
                                        player_turn = False
                                    # pygame.quit()
                                # sys.exit()
                else:
                    pygame.time.wait(1000)
                    player_turn = True
                    if self.pokemon.get_hp() > 0 :
                        self.fight.bot_attack()
                        message_attack = self.fight.fightinfo.set_who_attack_message(self.pokemon_enemy)
                        message_damage = self.fight.fightinfo.set_damage_message()
                        # pygame.time.wait(1000)
                        # player_turn = True
                    else:
                        win = True
                        # player_turn = True
                        #TODO game_over screen/new menu and allows events for player
                        pass
            

    def draw_win_player_screen(self):
        # self.util.draw_color_filter(self.screen)
        self.util.draw_window_with_background(self.screen, self.screen.width //2.5, self.screen.height //2.5)
        font_size = self.screen.height // 18
        x  = self.screen.width //2
        y = self.screen.height // 2
        self.util.draw_text("You won the fight!", REGULAR_FONT, font_size , self.screen, (x, y - font_size*2))
        self.util.draw_text(f"You gained {self.pokemon.get_xp_gained(self.pokemon_enemy)} XP", REGULAR_FONT, font_size, self.screen, (x, y))
        self.util.draw_text(f"Total XP : {self.pokemon.get_xp()}", REGULAR_FONT, font_size, self.screen, (x, y + font_size*2))

    def draw_win_bot_screen(self):
        # self.util.draw_color_filter(self.screen)
        self.util.draw_window_with_background(self.screen, self.screen.width //2.5, self.screen.height //2.5)
        font_size = self.screen.height // 18
        x  = self.screen.width //2
        y = self.screen.height // 2
        self.util.draw_text("You lost the fight!", REGULAR_FONT, font_size , self.screen, (x, y))