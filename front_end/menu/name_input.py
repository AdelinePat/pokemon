import pygame
from back_end.data_access.player_pokedex_service import does_player_exist
from back_end.data_access.pokemon_pokedex_service import get_first_pokemon
from .select_pokemons import SelectPokemons

class NameInput:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 50)
        self.player_name = ""

    def draw_text(self, text, x, y, color=(255, 255, 255)):
        surface = self.font.render(text, True, color)
        rect = surface.get_rect(center=(x, y))
        self.screen.get_display().blit(surface, rect)
        

    def get_name(self):
        while True:
            self.screen.update()
            self.screen.get_display().fill((0, 0, 0))

            self.draw_text("Entrez votre nom:", 600, 200, (255, 255, 0))
            self.draw_text(self.player_name, 600, 300, (255, 255, 255))
            self.draw_text("(Appuyez sur Entrée pour valider)", 600, 400)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    # sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and self.player_name:
                        if does_player_exist(self.player_name):
                            pokemon = get_first_pokemon(self.player_name)
                            return self.player_name, pokemon
                        else:
                            my_pokemon = SelectPokemons(self.player_name, self.screen).display()
                            return self.player_name, my_pokemon
                    elif event.key == pygame.K_BACKSPACE:
                        self.player_name = self.player_name[:-1]
                    elif event.unicode.isalnum():
                        self.player_name += event.unicode