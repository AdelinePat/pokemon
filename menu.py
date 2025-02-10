import pygame
import sys
from button import Button
from screen import Screen
from playerinput import PlayerInput  # Import de l'écran de saisie du nom

pygame.init()

class Menu(Screen):
    def __init__(self):
        super().__init__()
        self.bg = pygame.transform.scale(
            pygame.image.load("assets/background.jpg"),
            (self.screen.get_width(), self.screen.get_height()),
        )

        # Création des boutons du menu
        self.buttons = [
            Button(image=pygame.image.load("assets/Play Rect.png"), pos=(400, 250), text_input="Start", font=self.get_font(75), base_color="#d7fcd4", hovering_color="red"),
            Button(image=pygame.image.load("assets/Options Rect.png"), pos=(400, 400), text_input="Resume Game", font=self.get_font(50), base_color="#d7fcd4", hovering_color="red"),
            Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(400, 550), text_input="QUIT", font=self.get_font(75), base_color="#d7fcd4", hovering_color="red"),
        ]

        self.selected_button = 0  # Index du bouton sélectionné

    def main_menu(self):
        """Boucle du menu principal"""
        while True:
            self.render_menu()
            self.handle_events()

    def render_menu(self):
        """Affichage du menu"""
        self.screen.blit(self.bg, (0, 0))
        
        menu_text = self.get_font(80).render("MAIN MENU", True, "#b68f40")
        menu_rect = menu_text.get_rect(center=(400, 100))
        self.screen.blit(menu_text, menu_rect)

        mouse_pos = pygame.mouse.get_pos()
        for i, button in enumerate(self.buttons):
            if button.checkForInput(mouse_pos):
                self.selected_button = i
            button.changeColor(i == self.selected_button)
            button.update(self.screen)

        self.update_display()

    def handle_events(self):
        """Gestion des événements clavier/souris"""
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
        """Exécute l'action du bouton sélectionné"""
        if self.selected_button == 0:
            self.start_game()
        elif self.selected_button == 1:
            self.options()
        elif self.selected_button == 2:
            pygame.quit()
            sys.exit()

    def start_game(self):
        """Affiche l'écran d'entrée du nom"""
        player_input_screen = PlayerInput()
        player_input_screen.input_name_screen()

    def options(self):
        """Affiche l'écran des options"""
        while True:
            self.screen.fill("white")
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
                    self.main_menu()
                if event.type == pygame.MOUSEBUTTONDOWN and options_back.checkForInput(pygame.mouse.get_pos()):
                    self.main_menu()

            self.update_display()

if __name__ == "__main__":
    menu = Menu()
    menu.main_menu()
    name_input = PlayerInput()
    name_input.input_name_screen()