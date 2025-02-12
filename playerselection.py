import pygame
import sys
import json
from screen import Screen
from button import Button
import menu  # Assurez-vous que le module 'menu' est importé correctement

class PlayerSelection(Screen):
    def __init__(self):
        super().__init__()
        self.bg = pygame.transform.smoothscale(
            pygame.image.load("assets/backgroundpika.jpg"),
            (self.screen.get_width(), self.screen.get_height()),
        )
        self.players_data = self.load_players_data()
        self.selected_player_index = 0  # Index du joueur actuellement sélectionné
        self.font = self.get_font(40)

        # Création des boutons d'action (Back, Quit)
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
        """Charge les données des joueurs à partir d'un fichier JSON"""
        try:
            with open('players.json', 'r') as file:
                players = json.load(file)["players"]
                return players
        except FileNotFoundError:
            print("Fichier des joueurs non trouvé !")  # Si le fichier est manquant
            return []  # Retourne une liste vide si le fichier n'existe pas

    def render_player_list(self):
        """Affiche la liste des noms des joueurs"""
        y_offset = 200  # Position y de départ pour le premier joueur
        for i, player in enumerate(self.players_data):
            player_name_text = self.font.render(player["name"], True, "White")
            player_name_rect = player_name_text.get_rect(center=(600, y_offset + i * 50))
            if i == self.selected_player_index:
                pygame.draw.rect(self.screen, "Yellow", player_name_rect.inflate(20, 20), 2)  # Surligne le joueur sélectionné
            self.screen.blit(player_name_text, player_name_rect)

    def render_buttons(self):
        """Affiche les boutons d'action"""
        mouse_pos = pygame.mouse.get_pos()
        for button in self.buttons:
            button.changeColor(button.checkForInput(mouse_pos))
            button.update(self.screen)

    def handle_events(self):
        """Gère les événements clavier et souris"""
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
                    self.start_game_with_selected_player()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for button in self.buttons:
                    if button.checkForInput(mouse_pos):
                        if button == self.back_button:
                            self.return_to_main_menu()
                        elif button == self.quit_button:
                            pygame.quit()
                            sys.exit()

    def start_game_with_selected_player(self):
        """Démarre le jeu avec le joueur sélectionné"""
        selected_player = self.players_data[self.selected_player_index]
        print(f"Lancement du jeu avec {selected_player['name']} !")
        # Ajoutez ici la logique pour démarrer le jeu avec le joueur sélectionné

    def return_to_main_menu(self):
        """Retourne au menu principal"""
        menu.Menu().display()

    def main_menu(self):
        """Boucle principale du menu"""
        while True:
            self.screen.blit(self.bg, (0, 0))
            self.render_player_list()
            self.render_buttons()
            self.handle_events()
            self.update_display()
