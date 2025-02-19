import pygame
from back_end.controller import create_player
from __settings__ import LIGHT_GREEN, REGULAR_FONT, DARK_GREEN
# from select_pokemons import SelectPokemons
from front_end.menu.util_tool import UtilTool

class PokemonStat():
    def __init__(self, player_name, pokemon_list, pokemon, pokemon_enemy, screen, background):
        self.player_name = player_name
        self.pokemon_list = pokemon_list
        self.pokemon = pokemon
        self.pokemon_enemy = pokemon_enemy
        self.screen = screen
        self.font = pygame.font.Font(None, 50)
        self.util = UtilTool()
        self.background = pygame.transform.scale(background, (self.screen.width, self.screen.height))
       
        self.selected_index = 0
        self.running = True

    def display(self):
        while self.running:
            self.screen.update()
            self.screen.display.blit(self.background, (0,0))
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
                            create_player(self.player_name, self.pokemon)
                            return self.pokemon
                    elif event.key == pygame.K_ESCAPE:
                        from .change_pokemon_infight import ChangePokemonInFight
                        return ChangePokemonInFight(self.player_name, self.pokemon, self.pokemon_enemy, self.screen, self.pokemon_list).display()