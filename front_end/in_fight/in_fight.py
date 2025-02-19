import pygame
import math

import pygame
import sys
from __settings__ import BATTLE_BACKGROUND, BATTLE_FLOOR, REGULAR_FONT, DARK_GREEN, LIGHT_GREEN
from back_end.data_access.pokemon_pokedex_service import get_first_pokemon
from back_end.data_access.wild_pokemons import get_random_wild_pokemon
from back_end.data_access.bag_pokedex_service import get_bag_from_pokedex
from back_end.models.fight import Fight
from front_end.menu.util_tool import UtilTool
from front_end.menu.bagmenu import BagMenu
from front_end.menu.attack_type_menu import AttackMenu
from front_end.menu.infomenu import InfoMenu

from back_end.data_access.pokemon_pokedex_service import save_pokemon_to_pokedex
from back_end.data_access.bag_pokedex_service import save_bag_to_pokedex
from back_end.data_access.wild_pokemons import save_wild_pokemon
from front_end.menu.change_pokemon_infight import ChangePokemonInFight

from front_end.gameplay.healthdisplay import HealthDisplay
from __settings__ import BATTLE_BACKGROUND

class InFight():
    def __init__(self, screen, player, pokemon):
        """
        Initialize the menu with the screen, font, options, and selected index.
        """
        self.screen = screen
        self.pokemon_enemy = get_random_wild_pokemon()
        self.background = BATTLE_BACKGROUND
        # option_name = f"{self.pokemon_enemy.name} info"
        self.font = pygame.font.Font(None, 50)  # Set the font for menu text
        self.options = ["Attack", "Bag", "Team", "Info", "Flee"]  # Menu options
        self.bag_option = ["Potions", "Pokeball", "Back"]
        self.selected_index = 0  # Index of the currently selected option
        self.running = True  # Controls the menu loop
        self.player = player.player_name
        # self.pokemon = get_first_pokemon(self.player)
        self.pokemon = pokemon
        
        self.bag = get_bag_from_pokedex(self.player)
        self.fight = Fight(self.pokemon, self.pokemon_enemy)
        self.util = UtilTool()
        self.fleeing = False
        self.healthbar = HealthDisplay()

    def draw_text(self, text, x, y, color=(255, 255, 255)):
        """
        Renders text and displays it at the given (x, y) position.
        """
        surface = self.font.render(text, True, color)
        rect = surface.get_rect(center=(x, y))
        self.screen.get_display().blit(surface, rect)

   
    
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

    
        # pass

    def display(self):
        """
        Main menu loop that displays options and handles user input.
        """
        battle_floor = self.util.load_image(BATTLE_FLOOR)
        battle_floor2 = pygame.transform.flip(battle_floor, True, False)
        
        pokemon_enemy = self.util.load_image(self.pokemon_enemy.image)
        time_count = 0
        var_x = 5
        var_y = 5
        speed = 1.5
        win = False
        message_damage = None
        message_attack = None
        another_option = ""
        level = self.pokemon.get_level()
        # stage = self.pokemon.get_stage()
        name = self.pokemon.name
        # # fleeing = False
        # my_pokemon_x = int(self.screen.width // 10 * 2.5)
        # my_pokemon_y = int(self.screen.height // 7 * 5.4)
        my_pokemon_x = int(self.screen.width // 10 * 0.5)
        my_pokemon_y = int(self.screen.height // 10 )

        # pokemon_enemy_x = int(self.screen.width // 10 * 7.5 )               
        # pokemon_enemy_y = int(self.screen.height // 7 * 2)
        pokemon_enemy_x = int(self.screen.width // 10 * 9.5 )               
        pokemon_enemy_y = int(self.screen.height // 10)

        player_turn = False
        if self.fight.is_player_first():
            player_turn = True

        while self.running: 
            pokemon = pygame.transform.flip(self.util.load_image(self.pokemon.get_image()), True, False)
            
            #DISPLAY
            self.screen.update()
            if not win:
                time_count += speed
                x_movement = int(var_y * math.sin(time_count * 0.1))
                y_movement = int(var_x * math.sin(time_count * 0.08))
            self.util.display_assets_and_background(self.screen, x_movement, y_movement, battle_floor, battle_floor2, pokemon_enemy, pokemon)
            # draw_health_bar(x, y, max_hp, current_health, name, screen):

            # pokemon health
            # ,  + y_movement
            # self.healthbar.draw_health_bar(my_pokemon_x, my_pokemon_y, self.pokemon, self.screen)
            self.healthbar.draw_health_bar(my_pokemon_x, my_pokemon_y, self.pokemon, self.screen)
            # enemy health
            #  + x_movement, 
            self.healthbar.draw_health_bar(pokemon_enemy_x, pokemon_enemy_y,
                                            self.pokemon_enemy,\
                                            self.screen)
            
            self.util.draw_option_screen(self.screen)
            # Draw menu options
            for i, option in enumerate(self.options):
                color = LIGHT_GREEN if i == self.selected_index else DARK_GREEN  # Highlight selected option
                self.util.draw_text(option, REGULAR_FONT, self.screen.width //30, self.screen,\
                                    (self.screen.width//2 + i * 120, self.screen.height//8*7), color)

            if win:
                self.options[-1] = "Exit"
                self.fleeing = False
                if self.pokemon.get_hp() <= 0:
                    self.draw_win_bot_screen()
                elif another_option == "Success":
                    self.draw_win_capture_screen(self.pokemon_enemy, level, name)
                else:
                    self.draw_win_player_screen(level, name)

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

                        # if event.key == pygame.K_ESCAPE:
                        #     self.running = False

                        if event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN:  # Navigate down
                            self.selected_index = (self.selected_index + 1) % len(self.options)
                        elif event.key == pygame.K_LEFT or event.key == pygame.K_UP:  # Navigate up
                            self.selected_index = (self.selected_index - 1) % len(self.options)
                        elif event.key == pygame.K_RETURN:  # Select an option
                            match self.selected_index:
                                case 0:  # Start a new game
                                    if win:
                                        self.selected_index = 3
                                    elif self.pokemon.get_hp() > 0:
                                        attack_type = AttackMenu(self.screen, self.pokemon, self.pokemon_enemy).display()
                                        if attack_type == "Back":
                                            player_turn = True
                                        else:
                                            print("attaque")
                                            self.fight.player_attack(attack_type)
                                            if self.pokemon_enemy.get_hp() > 0:
                                                message_attack = self.fight.fightinfo.set_who_attack_message(self.pokemon)
                                                message_damage = self.fight.fightinfo.get_damage_message()
                                                player_turn = False
                                            else:
                                                self.pokemon.update_xp(self.pokemon_enemy)
                                                #TODO IS LEVEL UP??
                                                pokemon = pygame.transform.flip(self.util.load_image(self.pokemon.image), True, False)
                                                win = True
                                            #TODO menu end fight , xp gained...etc
                                    else:
                                        win = True
                                        
                                case 1:
                                    if win:
                                        self.selected_index = 3
                                    else:
                                        # print(f"HP max : {self.pokemon.get_hp_max()}")
                                        # self.pokemon.set_damage_hp(self.pokemon.get_hp() - 30)
                                        # print(f"HP actuel : {self.pokemon.get_hp() }")
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
                                                    # blabla
                                                    match another_option:
                                                        case "Success":
                                                            self.pokemon.update_xp(self.pokemon_enemy)
                                                            pokemon = pygame.transform.flip(self.util.load_image(self.pokemon.image), True, False)
                                                            # save_pokemon_to_pokedex(self.player,self.pokemon)
                                                            save_pokemon_to_pokedex(self.player, self.pokemon_enemy)
                                                            # save_bag_to_pokedex(self.player, self.bag)
                                                            # self.options[-1] = "Exit"
                                                            now_time = pygame.time.get_ticks()
                                                            success_time = 0
                                                            while success_time - now_time < 1000:
                                                                success_time = pygame.time.get_ticks()
                                                                self.capture_message("The pokemon has been captured successfully !")
                                                                pygame.display.update()
                                                            player_turn = False
                                                            win = True
                                                        case "Fail":
                                                            print("échec")
                                                            now_time = pygame.time.get_ticks()
                                                            failed_capture_time = 0
                                                            while failed_capture_time - now_time < 1000:
                                                                failed_capture_time = pygame.time.get_ticks()
                                                                self.capture_message(f"You failed to capture {self.pokemon_enemy.name}...")
                                                                pygame.display.update()
                                                            player_turn = False
                                                        case "Back":
                                                            player_turn = True
                                                    # if another_option:
                                                    #     player_turn == True
                                                    # else:
                                                    #     player_turn = False
                                                case "Back":
                                                    player_turn = True
                                case 2:
                                    print("TEAM")
                                    self.pokemon = ChangePokemonInFight(self.player, self.pokemon, self.pokemon_enemy, self.screen).display()
                                    # pokemon = pygame.transform.flip(self.load_image(self.pokemon.get_image()), True, False
                                    name = self.pokemon.name
                                    level = self.pokemon.get_level()
                                case 3:
                                    print("Info")
                                    InfoMenu(self.screen, self.pokemon, self.pokemon_enemy).display()
                                    player_turn = True  
                                case 4:
                                    if win:
                                        # self.pokemon.update_xp(self.pokemon_enemy)
                                        save_pokemon_to_pokedex(self.player,self.pokemon)
                                        save_bag_to_pokedex(self.player, self.bag)
                                        self.pokemon_enemy.set_hp(self.pokemon_enemy.get_hp_max())
                                        save_wild_pokemon(self.pokemon_enemy)
                                        return self.fleeing
                                        # return
                                    else:
                                        print("fuite")
                                        self.fleeing = self.fight.run_away()
                                        player_turn = False
                                        if self.fleeing:
                                            save_pokemon_to_pokedex(self.player,self.pokemon)
                                            save_bag_to_pokedex(self.player, self.bag)
                                            self.pokemon_enemy.set_hp(self.pokemon_enemy.get_hp_max())
                                            save_wild_pokemon(self.pokemon_enemy)
                                            now_time = pygame.time.get_ticks()
                                            failed_flee_time = 0
                                            while failed_flee_time - now_time < 1000:
                                                failed_flee_time = pygame.time.get_ticks()
                                                # self.failed_fleeing()
                                                self.message_pop_up(self.fight.fightinfo.flee_message)
                                                pygame.display.update()
                                            return self.fleeing
                                            # return
                                        else:
                                            now_time = pygame.time.get_ticks()
                                            failed_flee_time = 0
                                            while failed_flee_time - now_time < 1000:
                                                failed_flee_time = pygame.time.get_ticks()
                                                # self.failed_fleeing()
                                                self.message_pop_up(self.fight.fightinfo.flee_message)
                                                pygame.display.update()
                                        
                                        
                                    # pygame.quit()
                                # sys.exit()
                else:
                    pygame.time.wait(1000)
                    
                    if self.pokemon.get_hp() > 0 :
                        self.fight.bot_attack()
                        message_attack = self.fight.fightinfo.set_who_attack_message(self.pokemon_enemy)
                        message_damage = self.fight.fightinfo.get_damage_message()
                        # pygame.time.wait(1000)
                        # player_turn = True
                    else:
                        win = True
                        # player_turn = True
                        #TODO game_over screen/new menu and allows events for player
                        # pass
                    player_turn = True
            

    def draw_win_player_screen(self, level, name):
        # self.util.draw_color_filter(self.screen)
        self.util.draw_window_with_background(self.screen, self.screen.width //2.5, self.screen.height //2.5)
        font_size = self.screen.height // 22
        x  = self.screen.width //2
        y = self.screen.height // 2

        if self.pokemon.name != name:
            self.util.draw_text("You won the fight!", REGULAR_FONT, font_size , self.screen, (x, y - font_size*2))
            self.util.draw_text(f"Your pokemon evolved", REGULAR_FONT, font_size , self.screen, (x, y - font_size))
            self.util.draw_text(f"from {name} to {self.pokemon.name}",REGULAR_FONT, font_size , self.screen, (x, y))
            self.util.draw_text(f"You gained {self.pokemon.get_xp_gained(self.pokemon_enemy)} XP", REGULAR_FONT, font_size, self.screen, (x, y + font_size))
            self.util.draw_text(f"Total XP : {self.pokemon.get_xp()}", REGULAR_FONT, font_size, self.screen, (x, y + font_size*2))
        
        elif self.pokemon.get_level() != level:
            self.util.draw_text("You won the fight!", REGULAR_FONT, font_size , self.screen, (x, y - font_size*1.5))
            self.util.draw_text(f"You level up : {level} > {self.pokemon.get_level()}", REGULAR_FONT, font_size , self.screen, (x, y - font_size*0.5))
            self.util.draw_text(f"You gained {self.pokemon.get_xp_gained(self.pokemon_enemy)} XP", REGULAR_FONT, font_size, self.screen, (x, y + font_size*0.5))
            self.util.draw_text(f"Total XP : {self.pokemon.get_xp()}", REGULAR_FONT, font_size, self.screen, (x, y + font_size*1.5))

        else:
            font_size = self.screen.height // 18
            self.util.draw_text("You won the fight!", REGULAR_FONT, font_size , self.screen, (x, y - font_size*2))
            self.util.draw_text(f"You gained {self.pokemon.get_xp_gained(self.pokemon_enemy)} XP", REGULAR_FONT, font_size, self.screen, (x, y))
            self.util.draw_text(f"Total XP : {self.pokemon.get_xp()}", REGULAR_FONT, font_size, self.screen, (x, y + font_size*2))

    def draw_win_capture_screen(self, pokemon, level, name):
        # self.util.draw_color_filter(self.screen)
        self.util.draw_window_with_background(self.screen, self.screen.width //2.5, self.screen.height //2.5)
        font_size = self.screen.height // 22
        x  = self.screen.width //2
        y = self.screen.height // 2

        if pokemon.name != name:
            self.util.draw_text(f"Succeed to capture", REGULAR_FONT, font_size , self.screen, (x, y - font_size*2.5))
            self.util.draw_text(f"{pokemon.name}", REGULAR_FONT, font_size , self.screen, (x, y - font_size * 1.5))
            self.util.draw_text(f"Your pokemon evolved", REGULAR_FONT, font_size , self.screen, (x, y - font_size* 0.5))
            self.util.draw_text(f"from {name} to {self.pokemon.name}",REGULAR_FONT, font_size , self.screen, (x, y + font_size * 0.5))
            self.util.draw_text(f"You gained {self.pokemon.get_xp_gained(self.pokemon_enemy)} XP", REGULAR_FONT, font_size, self.screen, (x, y + font_size*1.5))
            self.util.draw_text(f"Total XP : {self.pokemon.get_xp()}", REGULAR_FONT, font_size, self.screen, (x, y + font_size*2.5))
        
        elif pokemon.get_level() != level:
            self.util.draw_text(f"Succeed to capture", REGULAR_FONT, font_size , self.screen, (x, y - font_size*2))
            self.util.draw_text(f"{pokemon.name}", REGULAR_FONT, font_size , self.screen, (x, y - font_size))
            self.util.draw_text(f"You level up : {level} > {self.pokemon.get_level()}", REGULAR_FONT, font_size , self.screen, (x, y))
            self.util.draw_text(f"You gained {self.pokemon.get_xp_gained(self.pokemon_enemy)} XP", REGULAR_FONT, font_size, self.screen, (x, y + font_size))
            self.util.draw_text(f"Total XP : {self.pokemon.get_xp()}", REGULAR_FONT, font_size, self.screen, (x, y + font_size*2))
        else:
            font_size = self.screen.height // 18
            self.util.draw_text(f"Succeed to capture", REGULAR_FONT, font_size , self.screen, (x, y - font_size*1.5))
            self.util.draw_text(f"{pokemon.name}", REGULAR_FONT, font_size , self.screen, (x, y - font_size * 0.5))
            self.util.draw_text(f"You gained {self.pokemon.get_xp_gained(self.pokemon_enemy)} XP", REGULAR_FONT, font_size, self.screen, (x, y + font_size*0.5))
            self.util.draw_text(f"Total XP : {self.pokemon.get_xp()}", REGULAR_FONT, font_size, self.screen, (x, y + font_size*1.5))

    def draw_win_bot_screen(self):
        # self.util.draw_color_filter(self.screen)
        self.util.draw_window_with_background(self.screen, self.screen.width //2.5, self.screen.height //2.5)
        font_size = self.screen.height // 18
        x  = self.screen.width //2
        y = self.screen.height // 2
        self.util.draw_text("You lost the fight!", REGULAR_FONT, font_size , self.screen, (x, y))

    # def failed_fleeing(self):
    #     self.util.draw_info_attack_screen(self.screen, "Votre fuite a échoué", "Le pokemon adverse va vous attaquer")
    
    def capture_message(self, message):
        self.util.draw_info_capture_screen(self.screen, message)
    
    def message_pop_up(self, message):
        self.util.draw_info_capture_screen(self.screen, message)