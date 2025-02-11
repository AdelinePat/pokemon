import pygame
import sys
import random
from screen import Screen
from button import Button
from pokemonselection import PokemonSelection


class Player_Input(Screen):
    def __init__(self):
        super().__init__()
        self.bg = pygame.transform.smoothscale(
            pygame.image.load("assets/backgroundpika.jpg"),
            (self.screen.get_width(), self.screen.get_height()),
        )
        self.player_name = ""

        # Get screen dimensions
        screen_width, screen_height = self.screen.get_width(), self.screen.get_height()

        # Define buttons with dynamic positioning
        self.confirm_button = Button(
            image=None,
            pos=(screen_width * 0.5, screen_height * 0.6),
            text_input="CONFIRM",
            font=self.get_font(int(screen_width * 0.04)),
            base_color="White",
            hovering_color="Green"
        )
        self.back_button = Button(
            image=None,
            pos=(screen_width * 0.10, screen_height * 0.95),
            text_input="BACK",
            font=self.get_font(int(screen_width * 0.04)),
            base_color="White",
            hovering_color="Blue"
        )
        self.quit_button = Button(
            image=None,
            pos=(screen_width * 0.90, screen_height * 0.95),
            text_input="QUIT",
            font=self.get_font(int(screen_width * 0.04)),
            base_color="White",
            hovering_color="Red"
        )

        # List of available Pokémon names
        self.pokemon_list = ["Pikachu", "Bulbasaur", "Charmander", "Squirtle",
                             "Eevee", "Jigglypuff", "Meowth", "Psyduck"]
        
        self.buttons = [
            self.back_button,
            self.quit_button,
        ]

    def input_name_screen(self):
        """Displays the name input screen"""
        while True:
            self.screen.blit(self.bg, (0, 0))
            screen_width, screen_height = self.screen.get_width(), self.screen.get_height()

            self.draw_text("Enter your name:", self.get_font(int(screen_width * 0.035)), "Black", screen_width * 0.5, screen_height * 0.3)
            self.draw_text(self.player_name, self.get_font(int(screen_width * 0.04)), "Yellow", screen_width * 0.5, screen_height * 0.4)

            self.confirm_button.changeColor(
                self.confirm_button.checkForInput(pygame.mouse.get_pos())
            )
            self.confirm_button.update(self.screen)

            # Update and draw other buttons (Back, Quit)
            for button in self.buttons:
                button.changeColor(button.checkForInput(pygame.mouse.get_pos()))
                button.update(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        self.player_name = self.player_name[:-1]
                    elif event.key == pygame.K_RETURN and self.player_name:
                        self.select_pokemon()
                    elif event.key in [pygame.K_q, pygame.K_ESCAPE]:  # Press Q or ESC to quit
                        pygame.quit()
                        sys.exit()
                    else:
                        self.player_name += event.unicode
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.confirm_button.checkForInput(pygame.mouse.get_pos()) and self.player_name:
                        self.select_pokemon()
                    for button in self.buttons:
                        if button.checkForInput(pygame.mouse.get_pos()):
                            if button == self.back_button:
                                self.main_menu()
                            elif button == self.quit_button:
                                pygame.quit()
                                sys.exit()

            self.update_display()

    def select_pokemon(self):
        """Proceeds to the Pokémon selection screen"""
        selected_pokemons = random.sample(self.pokemon_list, 2)
        PokemonSelection(self.player_name, selected_pokemons).select_pokemon_screen()

    def draw_text(self, text, font, color, x, y):
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y))
        outline_color = "White"
        offsets = [(-2, 0), (2, 0), (0, -2), (0, 2), (-2, -2), (2, -2), (-2, 2), (2, 2)]
        for dx, dy in offsets:
            outline_surface = font.render(text, True, outline_color)
            self.screen.blit(outline_surface, text_rect.move(dx, dy))
        self.screen.blit(text_surface, text_rect)