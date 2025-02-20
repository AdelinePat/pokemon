import pygame
# import math
pygame.init()
from __settings__ import DARK_GREEN, LIGHT_GREEN, REGULAR_FONT

class HealthDisplay():
    def draw_health_bar(self, x, y, pokemon, screen):

        initial_width = 200  # Largeur initiale
        narrow_width = 100   # Largeur après l'oblique
        health_bar_height = 20
        oblique_height = 20  # Hauteur de la remontée après l' oblique

        current_health = pokemon.get_hp()
        max_hp = pokemon.get_hp_max()
        name = pokemon.name
        health_ratio = max(current_health / max_hp, 0)  
        initial_health_width = int(initial_width * health_ratio)
        narrow_health_width = int(narrow_width * health_ratio)

        #  le contour fixe en noir
        points_border = [(x, y),
                        (x + initial_width, y),
                        (x + initial_width, y + health_bar_height),
                        (x + initial_width - (initial_width - narrow_width), y + health_bar_height + oblique_height),
                        (x + narrow_width, y + health_bar_height + oblique_height),
                        (x + narrow_width, y + health_bar_height),
                        (x, y + health_bar_height)]

        pygame.draw.polygon(screen.display, "black", points_border, 2)  # Contour noir

        # efface intérieur  barre 
        pygame.draw.polygon(screen.display, DARK_GREEN, points_border)  

        #  partie verte qui diminue de droite à gauche
        if current_health > 0:
                points_health = [(x, y),
                                (x + initial_health_width, y),
                                (x + initial_health_width, y + health_bar_height),
                                (x + max(0, initial_health_width - (initial_width - narrow_width)), y + health_bar_height + oblique_height),
                                (x + max(0, narrow_health_width), y + health_bar_height + oblique_height),
                                (x + max(0, narrow_health_width), y + health_bar_height),
                                (x, y + health_bar_height)]

                pygame.draw.polygon(screen.display, LIGHT_GREEN, points_health)  

        # Texte du nom et des HP


                
        font = pygame.font.Font(REGULAR_FONT, 18)
        health_text = font.render(f"{current_health} / {max_hp}", True, "white")
        name_text = font.render(f"{name} LV: {pokemon.get_level()}", True, "white")

        screen.display.blit(name_text, (x, y - 20))
        screen.display.blit(health_text, (x, y + 25))
