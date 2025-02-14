import pygame
import sys
import json
from display.models.screen import Screen
from display.models.button import Button
import display.models.menu as menu

class PlayerSelection(Screen):
    def __init__(self):
        super().__init__()
        self.bg = pygame.transform.smoothscale(
            pygame.image.load("assets/backgroundpika.jpg"),
            (self.screen.get_width(), self.screen.get_height()),
        )
        self.players_data = self.load_players_data()
        self.selected_player_index = 0  # Index of the currently selected player
        self.font = self.get_font(40)

        # Create action buttons (Back, Quit)
        screen_width, screen_height = self.screen.get_width(), self.screen.get_height()
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

        self.buttons = [self.back_button, self.quit_button]

    def load_players_data(self):
        """Load player data from a JSON file"""
        try:
            with open('players.json', 'r') as file:
                players = json.load(file)["players"]
                return players
        except FileNotFoundError:
            print("Players file not found!")  # If the file is missing
            return []  # Return an empty list if the file doesn't exist

    def render_player_list(self):
        """Render the list of player names"""
        y_offset = 200  # Starting y position for the first player
        for i, player in enumerate(self.players_data):
            player_name_text = self.font.render(player["name"], True, "White")
            player_name_rect = player_name_text.get_rect(center=(600, y_offset + i * 50))
            if i == self.selected_player_index:
                pygame.draw.rect(self.screen, "Yellow", player_name_rect.inflate(20, 20), 2)  # Highlight the selected player
            self.screen.blit(player_name_text, player_name_rect)

    def render_buttons(self):
        """Render the action buttons"""
        mouse_pos = pygame.mouse.get_pos()
        for button in self.buttons:
            button.changeColor(button.checkForInput(mouse_pos))
            button.update(self.screen)

    def handle_events(self):
        """Handle mouse and keyboard events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for button in self.buttons:
                    if button.checkForInput(mouse_pos):
                        if button == self.back_button:
                            self.return_to_main_menu()
                        elif button == self.quit_button:
                            pygame.quit()
                            sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.selected_player_index = (self.selected_player_index + 1) % len(self.players_data)
                elif event.key == pygame.K_UP:
                    self.selected_player_index = (self.selected_player_index - 1) % len(self.players_data)
                elif event.key == pygame.K_RETURN:
                    self.start_game_with_selected_player()

    def start_game_with_selected_player(self):
        """Start the game with the selected player"""
        selected_player = self.players_data[self.selected_player_index]
        print(f"Starting the game with {selected_player['name']}!")
        # Add your game start logic here

    def return_to_main_menu(self):
        """Return to the main menu"""
        menu.Menu().display()

    def main_menu(self):
        """Main menu loop"""
        while True:
            self.screen.blit(self.bg, (0, 0))
            self.render_player_list()
            self.render_buttons()
            self.handle_events()
            self.update_display()
