import pygame
import sys
from button import Button
from screen import Screen
import player_input
import playerselection

# from game import Game


pygame.init()

class Menu(Screen):
    def __init__(self):
        super().__init__()

        # Get screen dimensions
        screen_width, screen_height = self.screen.get_size()

        # Load and scale the background image
        self.bg = pygame.transform.smoothscale(
            pygame.image.load("assets/background.jpg"), (screen_width, screen_height)
        )

        # Define relative button positions
        button_width = screen_width * 0.3  # 30% of the screen width
        button_x = screen_width * 0.5  # Center horizontally
        

        self.buttons = [
            Button(
                image=pygame.image.load("assets/Play Rect.png"),
                pos=(button_x, screen_height * 0.3),  # 30% of the screen height
                text_input="Start",
                font=self.get_font(int(screen_width * 0.05)),  # Adaptive font size
                base_color="#d7fcd4",
                hovering_color="red"
            ),
            Button(
                image=pygame.image.load("assets/Options Rect.png"),
                pos=(button_x, screen_height * 0.5),  # 50% of the screen height
                text_input="Resume Game",
                font=self.get_font(int(screen_width * 0.04)),
                base_color="#d7fcd4",
                hovering_color="red"
            ),
            Button(
                image=pygame.image.load("assets/Quit Rect.png"),
                pos=(button_x, screen_height * 0.7),  # 70% of the screen height
                text_input="QUIT",
                font=self.get_font(int(screen_width * 0.05)),
                base_color="#d7fcd4",
                hovering_color="red"
            ),
        ]

        self.selected_button = 0  # Index of the selected button
        # self.game = game
        # self.screen = game.screen

        

    def display(self):
        """Displays the main menu"""
        while True:
            self.render_menu()
            self.handle_events()

    def render_menu(self):
        """Renders the menu elements"""
        self.screen.blit(self.bg, (0, 0))

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
            self.start_game()
        elif self.selected_button == 1:
            player_selection_screen = playerselection.PlayerSelection()
            player_selection_screen.main_menu()
        elif self.selected_button == 2:
            pygame.quit()
            sys.exit()

    def start_game(self):
        """Displays the player name input screen"""
        player_input_screen = player_input.Player_Input()
        player_input_screen.input_name_screen()

if __name__ == "__main__":
    menu = Menu()
    menu.display()
