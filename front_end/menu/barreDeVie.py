max_health = 350
initial_width = 200  # Largeur initiale
narrow_width = 100   # Largeur après l'oblique
health_bar_height = 20
oblique_height = 20  # Hauteur de la remontée après l' oblique


def draw_health_bar(x, y, current_health, name):
    health_ratio = max(current_health / max_health, 0)  
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

    pygame.draw.polygon(screen, BLACK, points_border, 2)  # Contour noir

    # efface intérieur  barre 
    pygame.draw.polygon(screen, LIGHT_GRAY, points_border)  

    #  partie verte qui diminue de droite à gauche
    if current_health > 0:
        points_health = [(x, y),
                         (x + initial_health_width, y),
                         (x + initial_health_width, y + health_bar_height),
                         (x + max(0, initial_health_width - (initial_width - narrow_width)), y + health_bar_height + oblique_height),
                         (x + max(0, narrow_health_width), y + health_bar_height + oblique_height),
                         (x + max(0, narrow_health_width), y + health_bar_height),
                         (x, y + health_bar_height)]

        pygame.draw.polygon(screen, GREEN, points_health)  

    # Texte du nom et des HP
    font = pygame.font.SysFont(None, 24)
    health_text = font.render(f"{current_health} / {max_health}", True, BLACK)
    name_text = font.render(f"{name} LV: 1", True, BLACK)

    screen.blit(name_text, (x, y - 20))
    screen.blit(health_text, (x, y + 25))