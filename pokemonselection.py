import pygame
from button import Button
from screen import Screen
import sys
from playerselection import PlayerSelection

class PokemonSelection(Screen):
    def __init__(self, player_name, selected_pokemons):
        # Initialize the parent class
        super().__init__()

        # Store the player's name and selected Pokémon list
        self.player_name = player_name
        self.selected_pokemons = selected_pokemons

        # Load and scale the background image
        self.bg = pygame.transform.scale(
            pygame.image.load("assets/backgroundpika.jpg"),
            (self.screen.get_width(), self.screen.get_height()),
        )

        # Create buttons for Pokémon selection and navigation
        self.pokemon1_button = Button(
            image=None,
            pos=(350, 400),
            text_input=self.selected_pokemons[0],
            font=self.get_font(40),
            base_color="White",
            hovering_color="Green"
        )
        self.pokemon2_button = Button(
            image=None,
            pos=(900, 400),
            text_input=self.selected_pokemons[1],
            font=self.get_font(40),
            base_color="White",
            hovering_color="Green"
        )
        self.return_button = Button(
            image=None,
            pos=(self.screen.get_width() * 0.10, self.screen.get_height() * 0.95),
            text_input="RETURN",
            font=self.get_font(int(self.screen.get_width() * 0.04)),
            base_color="White",
            hovering_color="Blue"
        )
        self.quit_button = Button(
            image=None,
            pos=(self.screen.get_width() * 0.90, self.screen.get_height() * 0.95),
            text_input="QUIT",
            font=self.get_font(int(self.screen.get_width() * 0.04)),
            base_color="White",
            hovering_color="Red"
        )
        self.play_button = Button(
            image=None,
            pos=(560, 550),
            text_input="PLAY",
            font=self.get_font(35),
            base_color="White",
            hovering_color="Green"
        )
        self.selected_button = 0  # Index of the currently selected button

    def select_pokemon_screen(self):
        """Displays the Pokémon selection screen"""
        while True:
            # Draw the background
            self.screen.blit(self.bg, (0, 0))

            # Draw the text prompt
            self.draw_text(f"{self.player_name}, choose your Pokémon:", self.get_font(40), "White", 600, 250)

            # Update and draw the buttons
            for i, button in enumerate([self.pokemon1_button, self.pokemon2_button, self.return_button, self.quit_button, self.play_button]):
                button.changeColor(i == self.selected_button)
                button.update(self.screen)

            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.selected_button = (self.selected_button + 1) % len([self.pokemon1_button, self.pokemon2_button, self.return_button, self.quit_button, self.play_button])
                    elif event.key == pygame.K_UP:
                        self.selected_button = (self.selected_button - 1) % len([self.pokemon1_button, self.pokemon2_button, self.return_button, self.quit_button, self.play_button])
                    elif event.key == pygame.K_RETURN:
                        if self.selected_button == 2:  # Return button
                            self.go_back()
                        elif self.selected_button == 3:  # Quit button
                            pygame.quit()
                            sys.exit()
                        elif self.selected_button in [0, 1]:  # Pokemon selection
                            self.start_game()
                    elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            # Update the display
            self.update_display()

    def select_button(self):
        """Execute the selected button's action"""
        if self.selected_button == 0:
            print(f"{self.player_name} chose {self.selected_pokemons[0]}!")
            self.play_game()
        elif self.selected_button == 1:
            print(f"{self.player_name} chose {self.selected_pokemons[1]}!")
            self.play_game()
        elif self.selected_button == 2:
             player_selection_screen = PlayerSelection()
             player_selection_screen.select_button()
        elif self.selected_button == 3:
            pygame.quit()
            sys.exit()
        elif self.selected_button == 4:
            self.start_game()

    def start_game(self):
        """Start the game with the selected Pokémon"""
        print(f"Starting the game with {self.selected_pokemons[self.selected_button]}!")
        pygame.quit()
        sys.exit()

    def draw_text(self, text, font, color, x, y):
        """Draw text with an outline effect"""
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y))

        # Draw the outline
        outline_color = "White"
        offsets = [(-2, 0), (2, 0), (0, -2), (0, 2), (-2, -2), (2, -2), (-2, 2), (2, 2)]
        for dx, dy in offsets:
            outline_surface = font.render(text, True, outline_color)
            self.screen.blit(outline_surface, text_rect.move(dx, dy))

        # Draw the main text
        self.screen.blit(text_surface, text_rect)
