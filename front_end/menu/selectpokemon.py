import pygame
import sys
from .display_pokemon_stat import PokemonStat
from back_end.controller import get_starter_pokemons
from __settings__ import LIGHT_GREEN, POKEMON_CENTER

class SelectPokemon():
    def __init__(self, player_name, screen, pokemon_list=[]):
        self.player_name = player_name
        self.screen = screen
        self.font = pygame.font.Font(None, 50)
        if not pokemon_list:
            self.pokemons = get_starter_pokemons()
        else:
            self.pokemons = pokemon_list

        self.options = []
        self.options_rect = []
        my_x = 0.5
        for pokemon in self.pokemons:
            option = self.load_image(pokemon.get_image(), (self.screen.width // 6, self.screen.width //  6))
            # option = pygame.transform.smoothscale(pygame.image.load(pokemon.get_image()), (self.screen.width // 6, self.screen.width //  6))
            option_rect = option.get_rect(center = (self.screen.width // 3 * my_x, self.screen.height // 5*2.5))
            my_x += 1
            self.options.append(option)
            self.options_rect.append(option_rect)

        self.selected_index = 0
        self.running = True

    def load_image(self, path, scaling):
        img = pygame.image.load(path).convert_alpha()
        img = pygame.transform.scale(img, (scaling))
        return img

    def draw_text(self, text, x, y, color=(255, 255, 255)):
        surface = self.font.render(text, True, color)
        rect = surface.get_rect(center=(x, y))
        self.screen.get_display().blit(surface, rect)

    def display(self):
        image = pygame.transform.scale(pygame.image.load(POKEMON_CENTER), (self.screen.width, self.screen.height))
        image_rect = image.get_rect(center = (self.screen.width // 2, self.screen.height //2))

        while self.running:
            self.screen.update()
            # self.screen.get_display().fill((0, 0, 0))
            self.screen.display.blit(image, image_rect)

            self.draw_text("Choose your first pokemon", 600, 150, LIGHT_GREEN)

            for i, option in enumerate(self.options):
                if i == self.selected_index:
                    # color = LIGHT_GREEN
                    option = pygame.transform.smoothscale(pygame.image.load(self.pokemons[i].get_image()), (self.screen.width // 4, self.screen.width //  4))
                    option.get_rect(center= (self.screen.width // 3 * 0.5+i, self.screen.height // 5*2.5))
                    self.screen.display.blit(option, self.options_rect[i])

                    # self.load_image(pokemon.get_image(), (self.screen.width // 6, self.screen.width //  6))
                else:
                    # color = (bidule)
                    option = pygame.transform.smoothscale(pygame.image.load(self.pokemons[i].get_image()), (self.screen.width // 6, self.screen.width //  6))
                    self.screen.display.blit(option, self.options_rect[i])
                # color = LIGHT_GREEN if i == self.selected_index else (255, 255, 255)
                # self.draw_text(option, 600, 300 + i * 60, color)
                

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
                                pokemon = PokemonStat(self.player_name, self.pokemons, self.pokemons[index], self.screen).display()
                                return pokemon

                    elif event.key == pygame.K_ESCAPE:

                        pass
                        # return