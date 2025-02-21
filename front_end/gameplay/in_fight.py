import pygame
import math

import pygame
import sys
from __settings__ import BATTLE_BACKGROUND, BATTLE_FLOOR, REGULAR_FONT, DARK_GREEN, LIGHT_GREEN
# from back_end.data_access.pokemon_pokedex_service import get_first_pokemon
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

class InFight():
    def __init__(self, screen, player, pokemon):
        """
        Initialize the menu with the screen, font, options, and selected index.
        """
        self.screen = screen
        self.pokemon_enemy = get_random_wild_pokemon()

        self.background = BATTLE_BACKGROUND
      
        self.font = pygame.font.Font(None, 50)  # Set the font for menu text
        self.options = ["Attack", "Bag", "Team", "Info", "Flee"]  # Menu options
        self.bag_option = ["Potions", "Pokeball", "Back"]
        self.selected_index = 0  # Index of the currently selected option
        self.running = True  # Controls the menu loop
        self.player = player.player_name
        self.pokemon = pokemon
        
        self.bag = get_bag_from_pokedex(self.player)
        self.fight = Fight(self.pokemon, self.pokemon_enemy)
        self.util = UtilTool()
        self.fleeing = False
        self.healthbar = HealthDisplay()

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
        name = self.pokemon.name
        winner = ""
      
        my_pokemon_x = int(self.screen.width // 10 * 0.5)
        my_pokemon_y = int(self.screen.height // 10 )

        pokemon_enemy_x = int(self.screen.width // 10 * 7.5 )               
        pokemon_enemy_y = int(self.screen.height // 10)

        player_turn = False
        if self.fight.is_player_first():
            player_turn = True

        while self.running: 
            pokemon = self.util.load_image(self.pokemon.get_back_image())
            
            #DISPLAY
            self.screen.update()
            if not win:
                time_count += speed
                x_movement = int(var_y * math.sin(time_count * 0.1))
                y_movement = int(var_x * math.sin(time_count * 0.08))
            self.util.display_assets_and_background_in_fight(self.screen, x_movement, y_movement, battle_floor, battle_floor2, pokemon_enemy, pokemon)
          
            self.healthbar.draw_health_bar(my_pokemon_x, my_pokemon_y, self.pokemon, self.screen)
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
                if winner == "enemy":
                    self.util.draw_win_bot_screen(self.screen)
                elif another_option == "Success":
                    self.util.draw_win_capture_screen(self.pokemon_enemy, self.pokemon, level, name, self.screen)
                else:
                    self.util.draw_win_player_screen(self.pokemon, self.pokemon_enemy, level, name, self.screen)

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
                                            self.fight.player_attack(attack_type)
                                            if self.pokemon_enemy.get_hp() > 0:
                                                message_attack = self.fight.fightinfo.set_who_attack_message(self.pokemon)
                                                message_damage = self.fight.fightinfo.get_damage_message()
                                                player_turn = False
                                            else:
                                                self.pokemon.update_xp(self.pokemon_enemy)
                                                winner = "player"
                                                pokemon = pygame.transform.flip(self.util.load_image(self.pokemon.image), True, False)
                                                win = True
                                    else:
                                        win = True
                                        
                                case 1: #bag
                                    if win:
                                        self.selected_index = 3
                                    else:
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
                                                    match another_option:
                                                        case "Success":
                                                            self.pokemon.update_xp(self.pokemon_enemy)
                                                            pokemon = pygame.transform.flip(self.util.load_image(self.pokemon.image), True, False)
                                                            now_time = pygame.time.get_ticks()
                                                            success_time = 0
                                                            while success_time - now_time < 1000:
                                                                success_time = pygame.time.get_ticks()
                                                                self.capture_message("The pokemon has been captured successfully !")
                                                                pygame.display.update()
                                                            player_turn = False
                                                            winner = "player"
                                                            win = True
                                                        case "Fail":
                                                            now_time = pygame.time.get_ticks()
                                                            failed_capture_time = 0
                                                            while failed_capture_time - now_time < 1000:
                                                                failed_capture_time = pygame.time.get_ticks()
                                                                self.capture_message(f"You failed to capture {self.pokemon_enemy.name}...")
                                                                pygame.display.update()
                                                            player_turn = False
                                                        case "Back":
                                                            player_turn = True
                                                case "Back":
                                                    player_turn = True
                                case 2: #team
                                    self.pokemon = ChangePokemonInFight(self.player, self.pokemon, self.pokemon_enemy, self.screen).display()
                                    self.fight.set_first_pokemon(self.pokemon)
                                    name = self.pokemon.name
                                    level = self.pokemon.get_level()
                                case 3: #info
                                    InfoMenu(self.screen, self.pokemon, self.pokemon_enemy).display()
                                    player_turn = True  
                                case 4: #exit or flee
                                    if win:
                                        if another_option == "Success":
                                            self.save_all_to_pokedex()
                                        else:
                                            self.save()
                                        return self.fleeing
                                    else:
                                        self.fleeing = self.fight.run_away()
                                        player_turn = False
                                        if self.fleeing:
                                            self.save()
                                            now_time = pygame.time.get_ticks()
                                            failed_flee_time = 0
                                            while failed_flee_time - now_time < 1000:
                                                failed_flee_time = pygame.time.get_ticks()
                                                self.message_pop_up(self.fight.fightinfo.flee_message)
                                                pygame.display.update()
                                                
                                            return self.fleeing
                                        else:
                                            now_time = pygame.time.get_ticks()
                                            failed_flee_time = 0
                                            while failed_flee_time - now_time < 1000:
                                                failed_flee_time = pygame.time.get_ticks()
                                                self.message_pop_up(self.fight.fightinfo.flee_message)
                                                pygame.display.update()       
                else:
                    pygame.time.wait(800)
                    if self.pokemon.get_hp() > 0 :
                        self.fight.bot_attack()
                        message_attack = self.fight.fightinfo.set_who_attack_message(self.pokemon_enemy)
                        message_damage = self.fight.fightinfo.get_damage_message()
                        if self.pokemon.get_hp() == 0 or self.pokemon.get_hp() < 0:
                            self.pokemon_enemy.update_xp(self.pokemon)
                            pokemon_enemy = self.util.load_image(self.pokemon_enemy.get_image())
                            winner = "enemy"
                            win = True
                    else:
                        self.pokemon_enemy.update_xp(self.pokemon)
                        winner = "enemy"
                        win = True
                    player_turn = True
         
    def capture_message(self, message):
        self.util.draw_info_capture_screen(self.screen, message)
    
    def message_pop_up(self, message):
        self.util.draw_info_capture_screen(self.screen, message)

    def reset_hp(self):
        self.pokemon.set_hp(self.pokemon.get_hp_max())
        self.pokemon_enemy.set_hp(self.pokemon_enemy.get_hp_max())

    def save_all_to_pokedex(self):
        self.reset_hp()
        save_pokemon_to_pokedex(self.player,self.pokemon)
        save_bag_to_pokedex(self.player, self.bag)
        save_pokemon_to_pokedex(self.player, self.pokemon_enemy)
    
    def save(self):
        self.reset_hp()
        save_pokemon_to_pokedex(self.player,self.pokemon)
        save_bag_to_pokedex(self.player, self.bag)
        save_wild_pokemon(self.pokemon_enemy)