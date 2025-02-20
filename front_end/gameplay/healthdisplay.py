import pygame
# import math
pygame.init()
from __settings__ import DARK_GREEN, LIGHT_GREEN, REGULAR_FONT

class HealthDisplay():
    def draw_health_bar(self, x, y, pokemon, screen):
        current_health = pokemon.get_hp()
        max_hp = pokemon.get_hp_max()
        name = pokemon.name
        health_ratio = current_health / max_hp

        initial_width = 200  # Largeur initiale
        narrow_width = 100   # Largeur après l'oblique
        health_bar_height = 20
        oblique_height = 20  # Hauteur de la remontée après l' oblique
        background_height = health_bar_height + oblique_height + 10

        initial_health_width = int(initial_width * health_ratio)
        narrow_health_width = int(narrow_width * health_ratio)

        # Fond gris 
        # background_rect = pygame.Surface((initial_width + 2, background_height), pygame.SRCALPHA)
        # background_rect.fill(DARK_GREEN)
        # screen.display.blit(background_rect, (x, y - 8))

        # window_surface = pygame.Surface((screen.width, screen.height), pygame.SRCALPHA)
        # window_surface.fill(DARK_GREEN)
        # window_surface.set_alpha(180)

        # Barre de vie en vert
        other_points = [(x, y),
                (x + initial_width, y),
                (x + initial_width, y + health_bar_height),
                (x + initial_width - (initial_width - narrow_width), y + health_bar_height + oblique_height),
                (x + narrow_width, y + health_bar_height + oblique_height),
                (x + narrow_width, y + health_bar_height),
                (x, y + health_bar_height)]
        
        points = [(x, y),
                (x + initial_health_width, y),
                (x + initial_health_width, y + health_bar_height),
                (x + initial_health_width - (initial_width - narrow_width), y + health_bar_height + oblique_height),
                (x + narrow_health_width, y + health_bar_height + oblique_height),
                (x + narrow_health_width, y + health_bar_height),
                (x, y + health_bar_height)]
        

        pygame.draw.polygon(screen.display, DARK_GREEN, other_points)
        pygame.draw.polygon(screen.display, "black", other_points, 2)

        pygame.draw.polygon(screen.display, LIGHT_GREEN, points)
        pygame.draw.polygon(screen.display, "black", points, 2)

        
        font = pygame.font.Font(REGULAR_FONT, 18)
        health_text = font.render(f"{current_health} / {max_hp}", True, "white")
        name_text = font.render(f"{name} LV: {pokemon.get_level()}", True, "white")

        screen.display.blit(name_text, (x, y - 20))
        screen.display.blit(health_text, (x, y + 25))
