import pygame
from back_end.controller import create_player
from back_end.data_access.player_pokedex_service import does_player_exist
from __settings__ import LIGHT_GREEN, REGULAR_FONT, DARK_GREEN
# from select_pokemons import SelectPokemons
from front_end.menu.util_tool import UtilTool

class PokemonStat():
    def __init__(self, player_name, pokemon_list, pokemon, pokemon_enemy, screen, background, identification):
        self.player_name = player_name
        self.pokemon_list = pokemon_list
        self.pokemon = pokemon
        self.pokemon_enemy = pokemon_enemy
        self.screen = screen
        self.font = pygame.font.Font(None, 50)
        self.util = UtilTool()
        self.background = background
        self.identification = identification
       
        self.selected_index = 0
        self.running = True

    def display(self):
        while self.running:
            self.screen.update()
            # self.screen.display.blit(self.background, (0,0))
            self.screen.set_background_display(self.background)
            self.util.draw_color_filter(self.screen)

            y_position = self.screen.height // 2

            image = pygame.transform.smoothscale(pygame.image.load(self.pokemon.get_image()), (self.screen.height//3, self.screen.height//3) )
            image_rect = image.get_rect(center = (self.screen.width //4, self.screen.height //2))
            self.screen.display.blit(image, image_rect)
            font_size = self.screen.width // 30

            self.util.draw_text(self.pokemon.name.upper(), REGULAR_FONT, font_size, self.screen, (self.screen.width//2, y_position -175), "white")
            # (self, text, font, font_size, screen, my_center, color=DARK_GREEN):
            self.util.draw_text(f"Level : {str(self.pokemon.get_level())}", REGULAR_FONT, font_size, self.screen, (self.screen.width//2, y_position - 125), "white")
            self.util.draw_text(f"Type : {str(", ".join(self.pokemon.type))}", REGULAR_FONT, font_size, self.screen, (self.screen.width//2, y_position -75), "white")
            self.util.draw_text(f"HP : {str(self.pokemon.get_hp())}", REGULAR_FONT, font_size, self.screen, (self.screen.width//2, y_position -25), "white")
            self.util.draw_text(f"Strength : {str(self.pokemon.get_strength())}", REGULAR_FONT, font_size, self.screen, (self.screen.width//2, y_position + 25), "white")
            self.util.draw_text(f"Defense : {str(self.pokemon.get_defense())}", REGULAR_FONT, font_size, self.screen, (self.screen.width//2, y_position + 75), "white")
            self.util.draw_text(f"Speed : {str(self.pokemon.get_speed())}", REGULAR_FONT, font_size, self.screen, (self.screen.width//2, y_position + 125), "white")
            self.util.draw_text(f"XP : {str(self.pokemon.get_xp())}", REGULAR_FONT, font_size, self.screen, (self.screen.width//2, y_position + 175), "white")
            
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    # sys.exit()
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_DOWN:
                        self.selected_index = (self.selected_index + 1) % len(self.options)
                    elif event.key == pygame.K_UP:
                        self.selected_index = (self.selected_index - 1) % len(self.options)

                    elif event.key == pygame.K_RETURN:
                                # PokemonStat(self.pokemons[index], self.screen)
                            # create_player(self.player_name, self.pokemon)
                            if not does_player_exist(self.player_name):
                                create_player(self.player_name, self.pokemon)
                            return self.pokemon
                    elif event.key == pygame.K_ESCAPE:
                        if self.identification == "pokemon_choice":
                            from .selectpokemon import SelectPokemon
                            # (self, player_name, screen, pokemon_list=[]):
                            return SelectPokemon(self.player_name, self.screen, self.pokemon_list).display()
                        elif self.identification == "in_pause_menu":
                            from .change_pokemon import ChangePokemon
                            # self, player_name, screen, pokemon_list=[]):
                            return ChangePokemon(self.player_name, self.screen, self.pokemon_list)
                        elif self.identification == "in_fight":
                            from .change_pokemon_infight import ChangePokemonInFight
                            return ChangePokemonInFight(self.player_name, self.screen, self.pokemon_list)