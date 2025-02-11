import pygame
import sys
from button import Button
from screen import Screen
from playerinput import Player_Input
from playerselection import PlayerSelection  

pygame.init()

class Menu(Screen):
    def __init__(self):
        super().__init__()

        # Obtenir les dimensions de l'écran
        screen_width, screen_height = self.screen.get_size()

        # Charger et ajuster l'image d'arrière-plan
        self.bg = pygame.transform.smoothscale(
            pygame.image.load("assets/background.jpg"), (screen_width, screen_height)
        )

        # Définir les positions relatives des boutons
        button_width = screen_width * 0.3  # 30% de la largeur de l'écran
        button_x = screen_width * 0.5  # Centrer horizontalement

        self.buttons = [
            Button(
                image=pygame.image.load("assets/Play Rect.png"),
                pos=(button_x, screen_height * 0.3),  # 30% de la hauteur
                text_input="Start",
                font=self.get_font(int(screen_width * 0.05)),  # Taille adaptative
                base_color="#d7fcd4",
                hovering_color="red"
            ),
            Button(
                image=pygame.image.load("assets/Options Rect.png"),
                pos=(button_x, screen_height * 0.5),  # 50% de la hauteur
                text_input="Resume Game",
                font=self.get_font(int(screen_width * 0.04)),
                base_color="#d7fcd4",
                hovering_color="red"
            ),
            Button(
                image=pygame.image.load("assets/Quit Rect.png"),
                pos=(button_x, screen_height * 0.7),  # 70% de la hauteur
                text_input="QUIT",
                font=self.get_font(int(screen_width * 0.05)),
                base_color="#d7fcd4",
                hovering_color="red"
            ),
        ]

        self.selected_button = 0  # Index du bouton sélectionné

    def main_menu(self):
        """Affiche le menu principal"""
        while True:
            self.render_menu()
            self.handle_events()

    def render_menu(self):
        """Affiche les éléments du menu"""
        self.screen.blit(self.bg, (0, 0))

        # Afficher le texte du menu principal
        menu_text = self.get_font(int(self.screen.get_width() * 0.08)).render("MAIN MENU", True, "#b68f40")
        menu_rect = menu_text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() * 0.15))
        self.screen.blit(menu_text, menu_rect)

        # Gérer les boutons et la souris
        mouse_pos = pygame.mouse.get_pos()
        for i, button in enumerate(self.buttons):
            if button.checkForInput(mouse_pos):
                self.selected_button = i
            button.changeColor(i == self.selected_button)
            button.update(self.screen)

        self.update_display()

    def handle_events(self):
        """Gère les événements du clavier et de la souris"""
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
            player_selection_screen = PlayerSelection()
            player_selection_screen.main_menu()
        elif self.selected_button == 2:
            pygame.quit()
            sys.exit()

    def start_game(self):
        """Affiche l'écran de saisie du nom du joueur"""
        player_input_screen = Player_Input()
        player_input_screen.input_name_screen()

if __name__ == "__main__":
    menu = Menu()
    menu.main_menu()
