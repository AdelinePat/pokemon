
import pygame
import sys
from __settings__ import LIGHT_GREEN

class BattleScreen:
    def __init__(self, screen, player):
        self.screen = screen
        self.player = player
        self.running = True
        self.font = pygame.font.Font(None, 50)

    def draw_text(self, text, x, y, color=(255, 255, 255)):
        """Render text on the screen at a specific position."""
        surface = self.font.render(text, True, color)
        rect = surface.get_rect(center=(x, y))
        self.screen.get_display().blit(surface, rect)

    def run(self):
        """Main loop for the battle screen."""
        while self.running:
            # Fill the screen with a black background
            self.screen.get_display().fill((0, 0, 0))

            # Display text messages
            self.draw_text("Pokémon Battle!", 600, 150, LIGHT_GREEN)
            self.draw_text("Press Escape to flee", 600, 300)

            # Update the display
            pygame.display.flip()

            # Update the screen using the 'screen' object method
            self.screen.update()

            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
