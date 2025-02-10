import pygame
import sys
from button import Button
from screen import Screen

pygame.init()

class Menu(Screen):
    def __init__(self):
        super().__init__()
        self.bg = pygame.transform.scale(
            pygame.image.load("assets/background.jpg"),
            (self.screen.get_width(), self.screen.get_height()),
        )

        # Creating buttons for the menu
        self.buttons = [
            Button(image=pygame.image.load("assets/Play Rect.png"), pos=(400, 250), text_input="Start", font=self.get_font(75), base_color="#d7fcd4", hovering_color="red"),
            Button(image=pygame.image.load("assets/Options Rect.png"), pos=(400, 400), text_input="Resume Game", font=self.get_font(50), base_color="#d7fcd4", hovering_color="red"),
            Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(400, 550), text_input="QUIT", font=self.get_font(75), base_color="#d7fcd4", hovering_color="red"),
        ]

        self.selected_button = 0  # Index of the currently selected button

    def main_menu(self):
        """Main menu loop"""
        while True:
            self.render_menu()  # Render the menu items
            self.handle_events()  # Handle keyboard and mouse events

    def render_menu(self):
        """Rendering the menu"""
        self.screen.blit(self.bg, (0, 0))  # Display background

        # Rendering the menu title
        menu_text = self.get_font(80).render("MAIN MENU", True, "#b68f40")
        menu_rect = menu_text.get_rect(center=(400, 100))
        self.screen.blit(menu_text, menu_rect)

        # Check mouse position and change selection
        mouse_pos = pygame.mouse.get_pos()
        for i, button in enumerate(self.buttons):
            if button.checkForInput(mouse_pos):
                self.selected_button = i  # Update the selected button

            # Apply highlight if the button is selected
            button.changeColor(i == self.selected_button)

            button.update(self.screen)  # Update button display

        self.update_display()

    def handle_events(self):
        """Handle keyboard and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.selected_button = (self.selected_button + 1) % len(self.buttons)  # Move to the next button
                elif event.key == pygame.K_UP:
                    self.selected_button = (self.selected_button - 1) % len(self.buttons)  # Go back to the previous button
                elif event.key == pygame.K_RETURN:
                    self.select_button()  # Activate the selected button

            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, button in enumerate(self.buttons):
                    if button.checkForInput(pygame.mouse.get_pos()):
                        self.selected_button = i
                        self.select_button()

    def select_button(self):
        """Execute the action of the selected button"""
        if self.selected_button == 0:
            self.play()  # Start the game
        elif self.selected_button == 1:
            self.options()  # Open the options screen
        elif self.selected_button == 2:
            pygame.quit()  # Quit the game
            sys.exit()

    def play(self):
        """Game screen"""
        while True:
            self.screen.fill("black")

            play_back = Button(image=None, pos=(400, 460), text_input="BACK", font=self.get_font(75), base_color="White", hovering_color="Green")
            play_back.changeColor(play_back.checkForInput(pygame.mouse.get_pos()))
            play_back.update(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.main_menu()  # Return to the main menu if ESC is pressed
                if event.type == pygame.MOUSEBUTTONDOWN and play_back.checkForInput(pygame.mouse.get_pos()):
                    self.main_menu()  # Return to the main menu if BACK button is clicked

            self.update_display()
    
    def draw_text(self, text, font, text_color,x, y):
        img = font.render(text, True, text_color)       
        screen.blit(img, (x, y))
    def options(self):
        """Options screen"""
        while True:
            self.screen.fill("white")
            draw_text("Press SPACE to pause the game", self.get_font(30), "black", self.screen, (400, 200))

            options_text = self.get_font(45).render("This is the OPTIONS screen.", True, "Black")
            options_rect = options_text.get_rect(center=(400, 260))
            self.screen.blit(options_text, options_rect)

            options_back = Button(image=None, pos=(400, 460), text_input="BACK", font=self.get_font(75), base_color="Black", hovering_color="Green")
            options_back.changeColor(options_back.checkForInput(pygame.mouse.get_pos()))
            options_back.update(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.main_menu()  # Return to the main menu if ESC is pressed
                if event.type == pygame.MOUSEBUTTONDOWN and options_back.checkForInput(pygame.mouse.get_pos()):
                    self.main_menu()  # Return to the main menu if BACK button is clicked

            self.update_display()

if __name__ == "__main__":
    menu = Menu()
    menu.main_menu()
