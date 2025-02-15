import pygame
import sys

class BattleScreen:
    def __init__(self, screen, player):
        self.screen = screen
        self.player = player
        self.running = True
        self.font = pygame.font.Font(None, 50)

    def draw_text(self, text, x, y, color=(255, 255, 255)):
        surface = self.font.render(text, True, color)
        rect = surface.get_rect(center=(x, y))
        self.screen.get_display().blit(surface, rect)

    def run(self):
        while self.running:
            # Remplir l'écran avec un fond noir
            self.screen.get_display().fill((0, 0, 0))

            # Afficher les textes
            self.draw_text("Combat Pokémon !", 600, 150, (255, 255, 0))
            self.draw_text("Appuie sur Échap pour fuir", 600, 300)

            # Mettre à jour l'affichage
            pygame.display.flip()

            # Mettre à jour l'écran avec la méthode de l'objet 'screen'
            self.screen.update()

            # Gérer les événements
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
