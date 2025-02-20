import pygame
import sys
from .display_pokemon_stat import PokemonStat
from back_end.controller import get_starter_pokemons
from __settings__ import LIGHT_GREEN, POKEMON_CENTER, POKEMON_CENTER, REGULAR_FONT, POKEBALL
from front_end.menu.util_tool import UtilTool
from back_end.controller import create_player

class SelectPokemon():
    def __init__(self, player_name, screen, pokemon_list=[]):
        self.player_name = player_name
        self.screen = screen
        self.background = pygame.transform.scale(pygame.image.load(POKEMON_CENTER), (self.screen.width, self.screen.height))
        self.util = UtilTool()
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

    def capturePokemon(self, pokemon, pokemon_rect, pokemons, pokemons_rect):
        pokeball_img = pygame.transform.scale(pygame.image.load(POKEBALL), (50,60))
        pokeball_img.set_colorkey((255,255,255))
        pokeball_rect = pokeball_img.get_rect(center=(self.screen.width // 2, self.screen.height - 100))
        # pokemon_rect = pygame.image.load(pokemon.get_image()).get_rect()
        target_pos = pokemon_rect.center
        
        vitesse = 15
        captured = False

        while not captured:
            self.screen.display.fill((173, 216, 230))
            self.screen.display.blit(self.background, (0, 0))


            for index, p in enumerate(pokemons):

                # p_rect = p_img.get_rect()
                self.screen.display.blit(p, pokemons_rect[index].topleft)

            if pokeball_rect.colliderect(pokemon_rect):
                captured = True

            else:
                dx = target_pos[0] - pokeball_rect.centerx
                dy = target_pos[1] - pokeball_rect.centery
                dist = max(1, (dx ** 2 + dy ** 2) ** 0.5)
                pokeball_rect.x += int(vitesse * dx / dist)
                pokeball_rect.y += int(vitesse * dy / dist)

            self.screen.display.blit(pokeball_img, pokeball_rect.topleft)
            pygame.display.flip()
            pygame.time.delay(30)
    

    def draw_text(self, text, x, y, color=(255, 255, 255)):
        surface = self.font.render(text, True, color)
        rect = surface.get_rect(center=(x, y))
        self.screen.get_display().blit(surface, rect)

    def display(self):
        image = self.background
        # image = pygame.transform.scale(pygame.image.load(POKEMON_CENTER), (self.screen.width, self.screen.height))
        image_rect = image.get_rect(center = (self.screen.width // 2, self.screen.height //2))

        while self.running:
            self.screen.update()
            # self.screen.get_display().fill((0, 0, 0))
            self.screen.display.blit(image, image_rect)

            # self.draw_text("Choose your first pokemon", 600, 150, LIGHT_GREEN)

            for i, option in enumerate(self.options):
                font_size = self.screen.height // 15
                if i == self.selected_index:
                    # color = LIGHT_GREEN
                    option = pygame.transform.smoothscale(pygame.image.load(self.pokemons[i].get_image()), (self.screen.width // 4, self.screen.width //  4))
                    option.get_rect(center= (self.screen.width // 3 * 0.5+i, self.screen.height // 5*2.5))
                    self.screen.display.blit(option, self.options_rect[i])
                    self.util.draw_text(self.pokemons[i].name, REGULAR_FONT, font_size, self.screen, (self.screen.width // 2, self.screen.height // 5*1.5))
                    # def draw_text(self, text, font, font_size, screen, my_center, color=DARK_GREEN):
                    
                    # self.util.draw_text(option.name, REGULAR_FONT, font_size, self.screen, (self.screen.width // 3 * 0.5+i, self.screen.height // 5*1.5))

                    # self.load_image(pokemon.get_image(), (self.screen.width // 6, self.screen.width //  6))
                else:
                    # color = (bidule)
                    option = pygame.transform.smoothscale(pygame.image.load(self.pokemons[i].get_image()), (self.screen.width // 6, self.screen.width //  6))
                    option.get_rect(center= (self.screen.width // 3 * 0.5+i, self.screen.height // 5*2.5))
                    self.screen.display.blit(option, self.options_rect[i])
                    # self.util.draw_text(self.pokemons[i].name, REGULAR_FONT, font_size, self.screen,\
                                        # (self.screen.width // 3 * 0.5+i, self.screen.height // 5*1.5))
                # color = LIGHT_GREEN if i == self.selected_index else (255, 255, 255)
                # self.draw_text(option, 600, 300 + i * 60, color)
            
            # for y, pokemon in enumerate(self.pokemons):
            #     self.util.draw_text(pokemon[y].name, REGULAR_FONT, font_size, self.screen, (self.screen.width // 3 * 0.5+y, self.screen.height // 5*1.5))


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
                                pokemon_enemy = None
                                pokemon = PokemonStat(self.player_name, self.pokemons, self.pokemons[index], pokemon_enemy, self.screen, self.background, "pokemon_choice").display()
                                # pokemon_data = { 'img': self.options[self.selected_index], 'rect': self.options_rect[self.selected_index] }
                    
                    if event.key == pygame.K_LSHIFT:
                        create_player(self.player_name, self.pokemons[self.selected_index])
                        self.capturePokemon(self.options[self.selected_index], self.options_rect[self.selected_index], self.options, self.options_rect)
                        return self.pokemons[self.selected_index]

                                #  player_name, pokemon_list, pokemon, pokemon_enemy, screen, self.background
                                # pokemon = PokemonStat(self.player_name, self.pokemons, self.pokemons[index], pokemon_enemy, self.screen, self.background).display()
                                # self.capturePokemon(pokemon_data, self.pokemons)
                                # return pokemon

                    elif event.key == pygame.K_ESCAPE:
                        # return self.pokemons[0]
                        # return
                        pass