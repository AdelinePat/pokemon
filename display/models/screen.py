import pygame

class Screen:
    def __init__(self, width=1200, height=720):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Pokemon")

    def get_font(self, size):
        return pygame.font.Font("assets/font.ttf", size)

    def update_display(self):
        pygame.display.update()