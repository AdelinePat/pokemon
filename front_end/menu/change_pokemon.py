import pygame
import sys
# from back_end.controller import create_player
from .display_pokemon_stat import PokemonStat
from back_end.data_access.pokemon_pokedex_service import get_all_pokemons_from_pokedex
from __settings__ import LIGHT_GREEN, BATTLE_BACKGROUND, REGULAR_FONT
# from front_end.gameplay.game import Game
from front_end.menu.util_tool import UtilTool


class ChangePokemon():
    def __init__(self, player_name, screen, pokemon_list=[]):
        self.player_name = player_name
        self.screen = screen
        self.background = pygame.image.load(BATTLE_BACKGROUND)
        self.font = pygame.font.Font(None, 50)
        self.util = UtilTool()
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
        while self.running:
            self.screen.update()
            self.screen.get_display().fill((0, 0, 0))
            # draw_text(self, text, font, font_size, screen, my_center, color=DARK_GREEN):
            font_size = self.screen.height // 20
            self.util.draw_text("Choose your pokemon", REGULAR_FONT, font_size, self.screen,\
                                 (self.screen.width//2, self.screen.height // 10*2), LIGHT_GREEN)

            # draw_text(self, text, font, font_size, screen, my_center, color=DARK_GREEN):
            for i, option in enumerate(self.options):
                color = LIGHT_GREEN if i == self.selected_index else (255, 255, 255)
                self.util.draw_text(option, REGULAR_FONT, font_size,\
                                    self.screen, (self.screen.width //2, self.screen.height // 10*3 + i*60), color)
                # 600, 300 + i * 60, color)

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
                                # self, player_name, pokemon_list, pokemon, pokemon_enemy, screen, background)
                                pokemon_enemy = None
                                pokemon = PokemonStat(self.player_name, self.pokemons, self.pokemons[index], pokemon_enemy, self.screen, self.background).display()
                                return pokemon
                                # game = Game(self.screen, self.player_name, pokemon).run()

                    elif event.key == pygame.K_ESCAPE:

                        pass
                        # return