import pygame
import math

from __settings__ import POKE_FONT, REGULAR_FONT

pygame.init()

# Class for handling the Pokémon battle and game state
class PokemonBattle:
    def __init__(self):
        # Configuration de la fenêtre
        self.window_width = 1220
        self.window_height = 720
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption('Pokemon Battle')

        # Chargement des assets (images)
        self.background = pygame.image.load('./assets/spritesheet-pokemon/fondCombat.png').convert()
        self.background = pygame.transform.scale(self.background, (self.window_width, self.window_height))

        self.perso1 = pygame.image.load('./assets/spritesheet-pokemon/pika.png')
        self.perso1 = pygame.transform.scale(self.perso1, (200, 200))

        self.perso2 = pygame.image.load('./assets/spritesheet-pokemon/draco.png')
        self.perso2 = pygame.transform.scale(self.perso2, (200, 200))

        self.circle1 = pygame.image.load('./assets/spritesheet-pokemon/cerclecombat.png')
        self.circle2 = pygame.image.load('./assets/spritesheet-pokemon/cerclecombat.png')

        # Supprimer le fond blanc des cercles
        self.circle1.set_colorkey((255, 255, 255))
        self.circle2.set_colorkey((255, 255, 255))

        self.circle1 = pygame.transform.scale(self.circle1, (250, 100))
        self.circle2 = pygame.transform.scale(self.circle2, (400, 150))

        # Variables de jeu (pour l'animation et la santé)
        self.time_elapsed = 0
        self.amplitude_vertical = 5
        self.amplitude_horizontal = 5
        self.speed = 2
        self.health_perso1 = 100
        self.health_perso2 = 120
        self.max_health_perso1 = 100
        self.max_health_perso2 = 120

        # Couleurs
        self.WHITE = (255, 255, 255)
        self.LIGHT_GRAY_TRANSPARENT = (200, 200, 200, 180)
        self.HIGHLIGHT_COLOR = (255, 255, 255)
        self.NORMAL_COLOR = (100, 100, 100)

        # Polices pour le texte du jeu
        self.font = pygame.font.Font(REGULAR_FONT, 40)

        # Configuration du menu
        self.menu_width, self.menu_height = 500, 80
        self.menu_x = 600
        self.menu_y = 630
        self.menu_surface = pygame.Surface((self.menu_width, self.menu_height), pygame.SRCALPHA)
        self.menu_surface.fill(self.LIGHT_GRAY_TRANSPARENT)

        # Positions des boutons
        self.button_width, self.button_height = 120, 40
        self.gap = 20

        self.button_attack = pygame.Rect(self.menu_x + 30, self.menu_y + 20, self.button_width, self.button_height)
        self.button_bag = pygame.Rect(self.button_attack.right + self.gap, self.menu_y + 20, self.button_width, self.button_height)
        self.button_run = pygame.Rect(self.button_bag.right + self.gap, self.menu_y + 20, self.button_width, self.button_height)

        self.selected_button = None

        # Horloge pour le taux de rafraîchissement du jeu
        self.clock = pygame.time.Clock()

    def draw_health_bar(self, x, y, health, max_health):
        """
        Draws a health bar above the Pokémon.
        :param x: X coordinate for the health bar position
        :param y: Y coordinate for the health bar position
        :param health: Current health of the Pokémon
        :param max_health: Maximum health of the Pokémon
        """
        health_bar_width = 200
        health_bar_height = 20

        # Dessine la barre de santé blanche (complètement blanche)
        pygame.draw.rect(self.screen, self.WHITE, (x, y, health_bar_width, health_bar_height))

    def handle_button_hover(self, mouse_pos):
        """
        Handles the hovering effect of the buttons (changes button color).
        :param mouse_pos: Current mouse position
        """
        if self.button_attack.collidepoint(mouse_pos):
            self.selected_button = "attack"
        elif self.button_bag.collidepoint(mouse_pos):
            self.selected_button = "bag"
        elif self.button_run.collidepoint(mouse_pos):
            self.selected_button = "run"
        else:
            self.selected_button = None

    def handle_button_click(self, event):
        """
        Handles the click events for the buttons.
        :param event: The event triggered by mouse click
        """
        if self.button_attack.collidepoint(event.pos):
            print("Attack selected!")
        elif self.button_bag.collidepoint(event.pos):
            print("Bag opened!")
        elif self.button_run.collidepoint(event.pos):
            print("Attempted to run away!")

    def update_pokemon_position(self):
        """
        Updates the Pokémon's position based on sinusoidal movement.
        """
        self.time_elapsed += self.speed
        movement_y = int(self.amplitude_vertical * math.sin(self.time_elapsed * 0.1))
        movement_x = int(self.amplitude_horizontal * math.sin(self.time_elapsed * 0.08))

        return movement_x, movement_y

    def draw(self):
        """
        Draws all the elements on the screen: background, Pokémon, health bar, buttons.
        """
        # Blit the background image
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.circle1, (775, 280))
        self.screen.blit(self.circle2, (200, 600))

        # Mise à jour et dessin des positions des Pokémon
        movement_x, movement_y = self.update_pokemon_position()
        self.screen.blit(self.perso1, (800, 200 + movement_y))
        self.screen.blit(self.perso2, (300 + movement_x, 525))

        # Dessiner les barres de santé
        self.draw_health_bar(800, 200 - 30, self.health_perso1, self.max_health_perso1)
        self.draw_health_bar(300, 525 - 30, self.health_perso2, self.max_health_perso2)

        # Dessiner la surface du menu et les boutons
        self.screen.blit(self.menu_surface, (self.menu_x, self.menu_y))

        # Changer la couleur des boutons lorsqu'on passe dessus
        color_attack = self.HIGHLIGHT_COLOR if self.selected_button == "attack" else self.NORMAL_COLOR
        color_bag = self.HIGHLIGHT_COLOR if self.selected_button == "bag" else self.NORMAL_COLOR
        color_run = self.HIGHLIGHT_COLOR if self.selected_button == "run" else self.NORMAL_COLOR

        # Étiquettes des boutons
        self.screen.blit(self.font.render("- Attack -", True, color_attack), (self.button_attack.x + 10, self.button_attack.y))
        self.screen.blit(self.font.render("- Bag -", True, color_bag), (self.button_bag.x + 30, self.button_bag.y))
        self.screen.blit(self.font.render("- Run -", True, color_run), (self.button_run.x + 20, self.button_run.y))

        # Mettre à jour l'écran
        pygame.display.flip()

    def run(self):
        """
        Main game loop that runs the game, handles events, updates the display.
        """
        running = True
        while running:
            mouse_pos = pygame.mouse.get_pos()

            # Gestion des événements
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()

                if event.type == pygame.MOUSEMOTION:
                    self.handle_button_hover(mouse_pos)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_button_click(event)

            # Dessiner tous les éléments à l'écran
            self.draw()

            # Limiter le taux de rafraîchissement
            self.clock.tick(60)

# Run the game
# if __name__ == "__main__":
#     game = PokemonBattle()
#     game.run()
