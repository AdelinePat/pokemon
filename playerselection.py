import pygame
import sys
import json
from screen import Screen
from button import Button



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

        # Create the action buttons (Play, Back, Quit)
        self.buttons = [
            # Button(image=None, pos=(400, 550), text_input="Start Game", font=self.get_font(50), base_color="#d7fcd4", hovering_color="red"),
            Button(image=None, pos=(110, 650), text_input="Back", font=self.get_font(50), base_color="#d7fcd4", hovering_color="Blue"),
            Button(image=None, pos=(1100, 650), text_input="Quit", font=self.get_font(50), base_color="#d7fcd4", hovering_color="Red"),
        ]

    def load_players_data(self):
        """Loads player data from a JSON file"""
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
                pygame.draw.rect(self.screen, "Yellow", player_name_rect.inflate(20, 20), 2)  # Highlight selected player
            self.screen.blit(player_name_text, player_name_rect)

    def render_buttons(self):
        """Render the action buttons"""
        mouse_pos = pygame.mouse.get_pos()
        for i, button in enumerate(self.buttons):
            if button.checkForInput(mouse_pos):
                button.changeColor(True)
            else:
                button.changeColor(False)
            button.update(self.screen)

    def handle_events(self):
        """Handle keyboard and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.selected_player_index = (self.selected_player_index + 1) % len(self.players_data)
                elif event.key == pygame.K_UP:
                    self.selected_player_index = (self.selected_player_index - 1) % len(self.players_data)
                elif event.key == pygame.K_RETURN:
                    self.select_action()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for i, button in enumerate(self.buttons):
                    if button.checkForInput(mouse_pos):
                        self.select_action(i)

    def select_action(self, action_index=None):
        """Handle the selected action (Start Game, Back, Quit)"""
        if action_index is None:
            return  # No action selected from mouse click

        if action_index == 0:  # Start Game
            selected_player = self.players_data[self.selected_player_index]
            print(f"Starting the game with {selected_player['name']}!")
            # Add game start logic here
            pygame.quit()
            sys.exit()  # Remove this after integrating game start

        elif action_index == 1:  # Back
            print("Going back to previous menu.")
            # Implement logic to go back to the previous screen
            pygame.quit()  # Exit for demonstration; Replace with previous menu navigation

        elif action_index == 2:  # Quit
            print("Quitting the game.")
            pygame.quit()
            sys.exit()

    def main_menu(self):
        """Main menu loop"""
        while True:
            self.screen.blit(self.bg, (0, 0))
            self.render_player_list()
            self.render_buttons()
            self.handle_events()
            self.update_display()


