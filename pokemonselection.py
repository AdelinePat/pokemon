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
        self.buttons = [self.pokemon1_button, self.pokemon2_button, self.return_button, self.quit_button, self.play_button]

    def select_pokemon_screen(self):
        """Displays the Pokémon selection screen"""
        while True:
            # Draw the background
            self.screen.blit(self.bg, (0, 0))

            # Draw the text prompt
            self.draw_text(f"{self.player_name}, choose your Pokémon:", self.get_font(40), "White", 600, 250)

            # Update and draw the buttons
            for button in self.buttons:
                button.update(self.screen)

            # Handle mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if self.pokemon1_button.checkForInput(mouse_pos):
                        self.start_game(0)
                    elif self.pokemon2_button.checkForInput(mouse_pos):
                        self.start_game(1)
                    elif self.return_button.checkForInput(mouse_pos):
                        self.go_back()
                    elif self.quit_button.checkForInput(mouse_pos):
                        pygame.quit()
                        sys.exit()
                    elif self.play_button.checkForInput(mouse_pos):
                        self.start_game(self.selected_button)

            # Update the display
            self.update_display()

    def start_game(self, selected_pokemon_index):
        """Start the game with the selected Pokémon"""
        selected_pokemon = self.selected_pokemons[selected_pokemon_index]
        print(f"Starting the game with {selected_pokemon}!")
        # Implement the logic to start the game with the selected Pokémon
        pygame.quit()
        sys.exit()

    def go_back(self):
        """Navigate back to the previous screen"""
        player_selection_screen = PlayerSelection()
        player_selection_screen.select_button()

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
