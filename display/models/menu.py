import pygame
import sys
from display.models.button import Button
from display.models.screen import Screen
from input.player_input import Player_Input
from selections.playerselection import PlayerSelection
from __settings__ import MAIN_MENU_BG

class Menu(Screen):
    def __init__(self, background, caption="Pokemon"):
        super().__init__(background, caption)
        button_x = self.width * 0.5

        self.buttons = [
            Button(
                image=pygame.image.load("assets/Play Rect.png"),
                pos=(button_x, self.height * 0.3),  # 30% of the screen height
                text_input="Start",
                font=self.get_font(int(self.width * 0.05)),  # Adaptive font size
                base_color="#d7fcd4",
                hovering_color="red"
            ),
            Button(
                image=pygame.image.load("assets/Options Rect.png"),
                pos=(button_x, self.height * 0.5),  # 50% of the screen height
                text_input="Resume Game",
                font=self.get_font(int(self.width * 0.04)),
                base_color="#d7fcd4",
                hovering_color="red"
            ),
            Button(
                image=pygame.image.load("assets/Quit Rect.png"),
                pos=(button_x, self.height * 0.7),  # 70% of the screen height
                text_input="QUIT",
                font=self.get_font(int(self.width * 0.05)),
                base_color="#d7fcd4",
                hovering_color="red"
            ),
        ]

        self.selected_button = 0   # Index of the selected button
        # self.game = game
        # self.screen = game.screen

        

    def display(self):
        """Displays the main menu"""
        while True:
            self.render_menu()
            self.handle_events()

    def render_menu(self):
        """Renders the menu elements"""
        self.screen.blit(self.background, (0, 0))

        # Display the main menu title
        menu_text = self.get_font(int(self.screen.get_width() * 0.08)).render("MAIN MENU", True, "#b68f40")
        menu_rect = menu_text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() * 0.15))
        self.screen.blit(menu_text, menu_rect)

        # Handle buttons and mouse hover effect
        mouse_pos = pygame.mouse.get_pos()
        for i, button in enumerate(self.buttons):
            if button.checkForInput(mouse_pos):
                self.selected_button = i
            button.changeColor(i == self.selected_button)
            button.update(self.screen)

        self.update_display()

    def handle_events(self):
        """Handles keyboard and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.selected_button = (self.selected_button + 1) % len(self.buttons)
                elif event.key == pygame.K_UP:
                    self.selected_button = (self.selected_button - 1) % len(self.buttons)
                elif event.key == pygame.K_RETURN:
                    self.select_button()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, button in enumerate(self.buttons):
                    if button.checkForInput(pygame.mouse.get_pos()):
                        self.selected_button = i
                        self.select_button()

    def select_button(self):
        """Executes the selected button's action"""
        if self.selected_button == 0:
            self.input_player()
        elif self.selected_button == 1:
            player_selection_screen = PlayerSelection()
            selected_player = player_selection_screen.main_menu()
        elif self.selected_button == 2:
            pygame.quit()
            sys.exit()

    def input_player(self):
        """Displays the player name input screen"""
        player_input_screen = Player_Input()
        player_input_screen.input_name_screen()


