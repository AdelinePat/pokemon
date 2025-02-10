import pygame
import sys
import random
from screen import Screen
from button import Button
# from menu import Menu

class PlayerInput(Screen):
    def __init__(self):
        super().__init__()
        self.bg = pygame.transform.scale(
            pygame.image.load("assets/téléchargement.jpg"),
            (self.screen.get_width(), self.screen.get_height()),
        )
        self.player_name = ""  # Stores the player's name
             # Define buttons
        self.confirm_button = Button(
            image=None,
            pos=(500, 550),
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
            hovering_color="Yellow"
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
            Button(image=None, pos=(400, 550), text_input="Start Game", font=self.get_font(50), base_color="#d7fcd4", hovering_color="red"),
            Button(image=None, pos=(400, 650), text_input="Back", font=self.get_font(50), base_color="#d7fcd4", hovering_color="red"),
            Button(image=None, pos=(400, 750), text_input="Quit", font=self.get_font(50), base_color="#d7fcd4", hovering_color="blue"),
        ]

    def input_name_screen(self):
        """Displays the name input screen"""
        while True:
            self.screen.blit(self.bg, (0, 0))
            self.draw_text("Enter your name:", self.get_font(35), "White", 500, 250)
            self.draw_text(self.player_name, self.get_font(40), "Yellow", 500, 320)

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
                            if i == 0:  # Start Game
                                self.start_game()
                            elif i == 1:  # Back
                                self.select_button()
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

    def draw_text(self, text, font, text_color, x, y):
        """Displays text on the screen"""
        img = font.render(text, True, text_color)
        self.screen.blit(img, img.get_rect(center=(x, y)))


class PokemonSelection(Screen):
    def __init__(self, player_name, selected_pokemons):
        super().__init__()
        self.player_name = player_name
        self.selected_pokemons = selected_pokemons
        self.bg = pygame.transform.scale(
            pygame.image.load("assets/backgroundpokemon.png"),
            (self.screen.get_width(), self.screen.get_height()),
        )
        # Buttons for Pokémon selection and navigation
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
            pos=(400, 500),
            text_input="RETURN",
            font=self.get_font(35),
            base_color="White",
            hovering_color="Green"
        )
        self.quit_button = Button(
            image=None,
            pos=(600, 600),
            text_input="QUIT",
            font=self.get_font(35),
            base_color="White",
            hovering_color="Red"
        )
        self.play_button = Button(
            image=None,
            pos=(900, 500),
            text_input="PLAY",
            font=self.get_font(35),
            base_color="White",
            hovering_color="Green"
        )
        self.selected_button = 0  # Index of the currently selected button

    def select_pokemon_screen(self):
        """Displays the Pokémon selection screen"""
        while True:
            self.screen.blit(self.bg, (0, 0))
            self.draw_text(f"{self.player_name}, choose your Pokémon:", self.get_font(40), "White", 600, 250)

            for i, button in enumerate([self.pokemon1_button, self.pokemon2_button, self.return_button, self.quit_button, self.play_button]):
                button.changeColor(i == self.selected_button)
                button.update(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.selected_button = (self.selected_button + 1) % 5
                    elif event.key == pygame.K_UP:
                        self.selected_button = (self.selected_button - 1) % 5
                    elif event.key == pygame.K_RETURN:
                        self.go_back()
                    elif event.key == pygame.K_q:  # Press Q to quit
                        pygame.quit()
                        sys.exit()
                    elif event.key == pygame.K_ESCAPE:  # Press ESC to exit
                        pygame.quit()
                        sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i, button in enumerate([self.pokemon1_button, self.pokemon2_button, self.return_button, self.quit_button, self.play_button]):
                        if button.checkForInput(pygame.mouse.get_pos()):
                            self.selected_button = i
                            self.select_button()

            self.update_display()

    def select_button(self):
        """Execute the selected button's action"""
        if self.selected_button == 0:
            print(f"{self.player_name} chose {self.selected_pokemons[0]}!")
        elif self.selected_button == 1:
            print(f"{self.player_name} chose {self.selected_pokemons[1]}!")
        elif self.selected_button == 2:
            PlayerInput().input_name_screen()
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

    def draw_text(self, text, font, text_color, x, y):
        """Displays text on the screen"""
        img = font.render(text, True, text_color)
        self.screen.blit(img, img.get_rect(center=(x, y)))
