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


class ChangePokemonInFight():
    def __init__(self, player_name, pokemon, pokemon_enemy, screen, pokemon_list=[]):
        self.player_name = player_name
        self.screen = screen
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

    # def draw_text(self, text, x, y, color=(255, 255, 255)):
    #     surface = self.font.render(text, True, color)
    #     rect = surface.get_rect(center=(x, y))
    #     self.screen.get_display().blit(surface, rect)

    def display_2(self):
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

        while self.running: 
            pokemon = pygame.transform.flip(self.util.load_image(self.pokemon.get_image()), True, False)

           
            #DISPLAY
            self.screen.update()
            if not win:
                time_count += speed
                x_movement = int(var_y * math.sin(time_count * 0.1))
                y_movement = int(var_x * math.sin(time_count * 0.08))
            self.util.display_assets_and_background(self.screen, x_movement, y_movement, battle_floor, battle_floor2, pokemon_enemy, pokemon)
            
            # def draw_window_with_background(self, screen, width, height, color=BACKGROUND):

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

                # color = LIGHT_GREEN if i == self.selected_index else color = (255, 255, 255)
                # self.util.draw_text(option, REGULAR_FONT, self.screen.height//22, self.screen, (self.screen.width // 2 * i, self.screen.height // 10 ), color)
                                    #  600, 300 + i * 60, color)

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
                        for index in range(len(self.options)):
                            if self.selected_index == index:
                                pokemon = PokemonStat(self.player_name, self.pokemons, self.pokemons[index], self.screen).display()
                                return pokemon
                                # game = Game(self.screen, self.player_name, pokemon).run()

                    elif event.key == pygame.K_ESCAPE:
                        return self.pokemon


    def display(self):
        while self.running:
            self.screen.update()
            self.screen.get_display().fill((0, 0, 0))

            self.draw_text("Choose your pokemon", 600, 150, LIGHT_GREEN)

            for i, option in enumerate(self.options):
                color = LIGHT_GREEN if i == self.selected_index else (255, 255, 255)
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
                        for index in range(len(self.options)):
                            if self.selected_index == index:
                                pokemon = PokemonStat(self.player_name, self.pokemons, self.pokemons[index], self.screen).display()
                                return pokemon
                                # game = Game(self.screen, self.player_name, pokemon).run()

                    elif event.key == pygame.K_ESCAPE:

                        pass
                        # return