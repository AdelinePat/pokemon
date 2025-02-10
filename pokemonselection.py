import pygame
# from playerinput import PlayerInput

class PokemonSelection(Screen):
    def __init__(self, player_name):
        super().__init__()
        self.player_name = player_name
        self.bg = pygame.transform.scale(
            pygame.image.load("assets/background.jpg"),
            (self.screen.get_width(), self.screen.get_height()),
        )

        # Buttons for Pokémon selection and navigation
        self.pokemon1_button = Button(image=None, pos=(300, 400), text_input="POKEMON 1", font=self.get_font(40), base_color="White", hovering_color="Green")
        self.pokemon2_button = Button(image=None, pos=(500, 400), text_input="POKEMON 2", font=self.get_font(40), base_color="White", hovering_color="Green")
        self.return_button = Button(image=None, pos=(400, 500), text_input="RETURN", font=self.get_font(40), base_color="White", hovering_color="Green")
        self.quit_button = Button(image=None, pos=(400, 600), text_input="QUIT", font=self.get_font(40), base_color="White", hovering_color="Red")

    def select_pokemon_screen(self):
        """Displays the Pokémon selection screen"""
        while True:
            self.screen.blit(self.bg, (0, 0))
            self.draw_text(f"{self.player_name}, choose your Pokémon:", self.get_font(40), "White", 400, 250)
            
            for button in [self.pokemon1_button, self.pokemon2_button, self.return_button, self.quit_button]:
                button.changeColor(button.checkForInput(pygame.mouse.get_pos()))
                button.update(self.screen)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.pokemon1_button.checkForInput(pygame.mouse.get_pos()):
                        print(f"{self.player_name} chose Pokémon 1!")
                    elif self.pokemon2_button.checkForInput(pygame.mouse.get_pos()):
                        print(f"{self.player_name} chose Pokémon 2!")
                    elif self.return_button.checkForInput(pygame.mouse.get_pos()):
                        PlayerInput().input_name_screen()
                    elif self.quit_button.checkForInput(pygame.mouse.get_pos()):
                        pygame.quit()
                        sys.exit()
            
            self.update_display()

    def draw_text(self, text, font, text_color, x, y):
        """Displays text on the screen"""
        img = font.render(text, True, text_color)
        self.screen.blit(img, img.get_rect(center=(x, y)))
