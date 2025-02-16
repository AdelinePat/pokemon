import pygame
import sys
from back_end.controller import create_player
from .display_pokemon_stat import PokemonStat

# from codes.name_input import NameInput  
# from codes.game import Game
# from codes.select_player import SelectPlayer
from back_end.controller import get_starter_pokemons


class SelectPokemons():
    def __init__(self, player_name, screen, pokemon_list=[]):
        self.player_name = player_name
        self.screen = screen
        self.font = pygame.font.Font(None, 50)
        if not pokemon_list:
            self.pokemons = get_starter_pokemons()
        else:
            self.pokemons = pokemon_list

        self.options = []
        for pokemon in self.pokemons:
            option = pokemon.name
            self.options.append(option)

        self.selected_index = 0
        self.running = True

    def draw_text(self, text, x, y, color=(255, 255, 255)):
        surface = self.font.render(text, True, color)
        rect = surface.get_rect(center=(x, y))
        self.screen.get_display().blit(surface, rect)

    def display(self):
        while self.running:
            self.screen.update()
            self.screen.get_display().fill((0, 0, 0))

            self.draw_text("Choisissez votre premier pokemon", 600, 150, (255, 255, 0))

            for i, option in enumerate(self.options):
                color = (255, 255, 0) if i == self.selected_index else (255, 255, 255)
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

                    elif event.key == pygame.K_ESCAPE:

                        pass
                        # return