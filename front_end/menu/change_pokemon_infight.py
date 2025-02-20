import pygame
import sys
# from back_end.controller import create_player
from .display_pokemon_stat import PokemonStat
from back_end.data_access.pokemon_pokedex_service import get_all_pokemons_from_pokedex
from __settings__ import LIGHT_GREEN
import math
from __settings__ import BATTLE_BACKGROUND, BATTLE_FLOOR, REGULAR_FONT, LIGHT_GREEN, DARK_GREEN
# from front_end.gameplay.game import Game
from front_end.menu.util_tool import UtilTool

from back_end.data_access.pokemon_pokedex_service import save_pokemon_to_pokedex
# from back_end.data_access.bag_pokedex_service import save_bag_to_pokedex
# from back_end.data_access.wild_pokemons import save_wild_pokemon

class ChangePokemonInFight():
    def __init__(self, player_name, pokemon, pokemon_enemy, screen, pokemon_list=[]):
        self.player_name = player_name
        self.screen = screen
        self.background = BATTLE_BACKGROUND
        self.font = pygame.font.Font(None, 50)
        self.util = UtilTool()
        self.pokemon_enemy = pokemon_enemy
        self.pokemon = pokemon

        if not pokemon_list:
            self.pokemons = get_all_pokemons_from_pokedex(self.player_name)
        else:
            self.pokemons = pokemon_list

        self.options = []
        for pokemon in self.pokemons:
            option = pokemon.name
            self.options.append(option)

        self.selected_index = 0
        self.running = True

    def display(self):
        battle_floor = self.util.load_image(BATTLE_FLOOR)
        battle_floor2 = pygame.transform.flip(battle_floor, True, False)
        
        pokemon_enemy = self.util.load_image(self.pokemon_enemy.get_image())
        time_count = 0
        var_x = 5
        var_y = 5
        speed = 1.5
        win = False
        my_pokemon_x = int(self.screen.width // 10 * 0.5)
        my_pokemon_y = int(self.screen.height // 10 )

        pokemon_enemy_x = int(self.screen.width // 10 * 9.5 )               
        pokemon_enemy_y = int(self.screen.height // 10)
        self.screen.set_background_display(self.background)

        while self.running:
           
            pokemon = pygame.transform.flip(self.util.load_image(self.pokemon.get_image()), True, False)

            self.screen.update()
            if not win:
                time_count += speed
                x_movement = int(var_y * math.sin(time_count * 0.1))
                y_movement = int(var_x * math.sin(time_count * 0.08))
            self.util.display_assets_and_background(self.screen, x_movement, y_movement, battle_floor, battle_floor2, pokemon_enemy, pokemon)


            self.util.draw_window_with_background(self.screen, self.screen.width//2, self.screen.height //2)

            for i, option in enumerate(self.options):
                if i == self.selected_index:
                    color = LIGHT_GREEN
                else:
                    color = DARK_GREEN

                y = i % 3
                if i in range(0,3):

                    self.util.draw_text(option, REGULAR_FONT, self.screen.height//22, self.screen,\
                                    (self.screen.width // 8*3, self.screen.height // 8 * y + self.screen.height // 8*3), color)
                
                elif i in range(3, 6):
                    self.util.draw_text(option, REGULAR_FONT, self.screen.height//22, self.screen,\
                                    (self.screen.width // 8*4, self.screen.height // 8 * y + self.screen.height // 8*3), color)

                elif i in range(6, 9):

                    self.util.draw_text(option, REGULAR_FONT, self.screen.height//22, self.screen,\
                                        (self.screen.width // 8*5, self.screen.height // 8 * y + self.screen.height // 8*3), color)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_DOWN or event.key == pygame.K_RIGHT:
                        self.selected_index = (self.selected_index + 1) % len(self.options)
                    elif event.key == pygame.K_UP or event.key == pygame.K_LEFT:
                        self.selected_index = (self.selected_index - 1) % len(self.options)

                    elif event.key == pygame.K_RETURN:
                        for index in range(len(self.options)):
                            if self.selected_index == index:
                                # (self, player_name, pokemon_list, pokemon, pokemon_enemy, screen):
                                save_pokemon_to_pokedex(self.player_name, self.pokemon)
                                PokemonStat(self.player_name, self.pokemons, self.pokemons[index], self.pokemon_enemy, self.screen, self.background, "in_fight").display()
                                
                                return self.pokemons[self.selected_index]
                                # game = Game(self.screen, self.player_name, pokemon).run()

                    elif event.key == pygame.K_ESCAPE:
                        return self.pokemon