import pygame
import sys
from screen import Screen
from button import Button

class PlayerInput(Screen):
    def __init__(self):
        super().__init__()
        self.bg = pygame.transform.scale(
            pygame.image.load("assets/téléchargement.jpg"),
            (self.screen.get_width(), self.screen.get_height()),
        )

        self.player_name = ""  # Stores the player's name
        self.confirm_button = Button(image=None, pos=(400, 500), text_input="CONFIRM", font=self.get_font(50), base_color="White", hovering_color="Green")

    def input_name_screen(self):
        """Displays the name input screen"""
        while True:
            self.screen.blit(self.bg, (0, 0))
            self.draw_text("Enter your name:", self.get_font(40), "White", 400, 250)
            self.draw_text(self.player_name, self.get_font(40), "Yellow", 400, 320)
            
            self.confirm_button.changeColor(self.confirm_button.checkForInput(pygame.mouse.get_pos()))
            self.confirm_button.update(self.screen)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        self.player_name = self.player_name[:-1]
                    elif event.key == pygame.K_RETURN and self.player_name:
                        self.select_pokemon()
                    else:
                        self.player_name += event.unicode
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.confirm_button.checkForInput(pygame.mouse.get_pos()) and self.player_name:
                        self.select_pokemon()
            
            self.update_display()

    def select_pokemon(self):
        """Proceeds to the Pokémon selection screen"""
        PokemonSelection(self.player_name).select_pokemon_screen()

    def draw_text(self, text, font, text_color, x, y):
        """Displays text on the screen"""
        img = font.render(text, True, text_color)
        self.screen.blit(img, img.get_rect(center=(x, y)))
