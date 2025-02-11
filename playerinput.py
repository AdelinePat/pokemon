import pygame
import sys
import random
from screen import Screen
from button import Button
from pokemonselection import PokemonSelection


class PlayerInput(Screen):
    def __init__(self):
        super().__init__()
        self.bg = pygame.transform.scale(
            pygame.image.load("assets/backgroundpika.jpg"),
            (self.screen.get_width(), self.screen.get_height()),
        )
        self.player_name = ""  # Stores the player's name
             # Define buttons
        self.confirm_button = Button(
            image=None,
            pos=(600, 550),
            text_input="CONFIRM",
            font=self.get_font(50),
            base_color="White",
            hovering_color="Green"
        )
        self.back_button = Button(
            image=None,
            pos=(300, 650),
            text_input="BACK",
            font=self.get_font(50),
            base_color="White",
            hovering_color="Blue"
        )
        self.quit_button = Button(
            image=None,
            pos=(900, 650),
            text_input="QUIT",
            font=self.get_font(50),
            base_color="White",
            hovering_color="Red"
        )

        # List of available Pokémon names
        self.pokemon_list = ["Pikachu", "Bulbasaur", "Charmander", "Squirtle",
                             "Eevee", "Jigglypuff", "Meowth", "Psyduck"]
        
        self.buttons = [
            Button(image=None, pos=(110, 650), text_input="Back", font=self.get_font(50), base_color="#d7fcd4", hovering_color="Blue"),
            Button(image=None, pos=(1100, 650), text_input="Quit", font=self.get_font(50), base_color="#d7fcd4", hovering_color="Red"),
        ]

    def input_name_screen(self):
        """Displays the name input screen"""
        while True:
            self.screen.blit(self.bg, (0, 0))
            self.draw_text("Enter your name:", self.get_font(35), "Black", 600, 250)
            self.draw_text(self.player_name, self.get_font(40), "Yellow", 600, 320)

            self.confirm_button.changeColor(
                self.confirm_button.checkForInput(pygame.mouse.get_pos())
            )
            self.confirm_button.update(self.screen)

            # Update and draw other buttons (Start Game, Back, Quit)
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
                    elif event.key == pygame.K_q:  # Press Q to quit
                        pygame.quit()
                        sys.exit()
                    elif event.key == pygame.K_ESCAPE:  # Press ESC to exit
                        pygame.quit()
                        sys.exit()
                    else:
                        self.player_name += event.unicode
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.confirm_button.checkForInput(pygame.mouse.get_pos()) and self.player_name:
                        self.select_pokemon()
                    # Handle button clicks for Start Game, Back, and Quit
                    for i, button in enumerate(self.buttons):
                        if button.checkForInput(pygame.mouse.get_pos()):
                            if i == 0:  # Select pokemon
                                self.select_button()
                            elif i == 1:  # Back
                                self.main_menu()
                            elif i == 2:  # Quit
                                pygame.quit()
                                sys.exit()

            self.update_display()

    def start_game(self):
        """Start the game with the selected Pokémon"""
        print(f"Starting the game!")
        # Logic to start the game goes here

    def go_back(self):
        """Go back to the previous screen"""
        print("Going back to previous screen")
        # Logic to navigate back to the previous screen goes here


    def select_pokemon(self):
        """Proceeds to the Pokémon selection screen"""
        # Randomly select two different Pokémon
        selected_pokemons = random.sample(self.pokemon_list, 2)
        PokemonSelection(self.player_name, selected_pokemons).select_pokemon_screen()

    def draw_text(self, text, font, color, x, y):
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y))

        # Bordure blanche autour du texte (effet contour)
        outline_color = "White"
        offsets = [(-2, 0), (2, 0), (0, -2), (0, 2), (-2, -2), (2, -2), (-2, 2), (2, 2)]
        for dx, dy in offsets:
            outline_surface = font.render(text, True, outline_color)
            self.screen.blit(outline_surface, text_rect.move(dx, dy))

        # Texte principal en noir
        self.screen.blit(text_surface, text_rect)

