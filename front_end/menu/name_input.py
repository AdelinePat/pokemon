import pygame
from __settings__ import MAIN_MENU_BACKGROUND4, LIGHT_GREEN, REGULAR_FONT, POKE_FONT
from .util_tool import UtilTool
from .selectpokemon import SelectPokemon
from .intro import IntroChoice
from back_end.controller import does_player_exist, get_first_pokemon

class NameInput:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 50)
        self.player_name = ""
        self.util = UtilTool()

    def get_name(self):
        while True:
            self.screen.update()
            self.screen.get_display().fill((0, 0, 0))
            self.screen.set_background_display(MAIN_MENU_BACKGROUND4)
            font_size = self.screen.height // 15
            
            self.util.draw_text("Enter your name", POKE_FONT, font_size, self.screen,\
                                (self.screen.width // 2, self.screen.height // 3), "white")

            self.util.draw_text(self.player_name, REGULAR_FONT, font_size, self.screen,\
                                (self.screen.width // 2, self.screen.height // 2), LIGHT_GREEN)
 
            self.util.draw_text("(Press enter key to continue)", REGULAR_FONT, font_size, self.screen,\
                                (self.screen.width // 2, self.screen.height // 3*2), "white")

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pass
                    if event.key == pygame.K_RETURN and self.player_name:
                        if does_player_exist(self.player_name):
                            pygame.time.wait(1000)
                            pokemon = get_first_pokemon(self.player_name)
                            return self.player_name, pokemon
                        
                        else:
                            IntroChoice(self.player_name, self.screen).display()
                            my_pokemon = SelectPokemon(self.player_name, self.screen).display()

                            return self.player_name, my_pokemon
                    elif event.key == pygame.K_BACKSPACE:
                        self.player_name = self.player_name[:-1]
                    elif event.unicode.isalnum():
                        self.player_name += event.unicode