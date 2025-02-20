import pygame
import math
pygame.init()
from __settings__ import DARK_GREEN, LIGHT_GREEN

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

        
        font = pygame.font.SysFont(None, 24)
        health_text = font.render(f"{current_health} / {max_hp}", True, "black")
        name_text = font.render(f"{name} LV: 1", True, "black")

        screen.display.blit(name_text, (x, y - 20))
        screen.display.blit(health_text, (x, y + 25))


# screen = pygame.display.set_mode((1220, 720))
# pygame.display.set_caption('Pokemon Battle')


# background = pygame.image.load('./spritesheet-pokemon/fondCombat.png').convert()
# background = pygame.transform.scale(background, (1220, 720))

# perso1 = pygame.image.load('./spritesheet-pokemon/pika.png')
# perso1 = pygame.transform.scale(perso1, (200, 200))

# perso2 = pygame.image.load('./spritesheet-pokemon/draco.png')
# perso2 = pygame.transform.scale(perso2, (200, 200))

# cercle1 = pygame.image.load('./spritesheet-pokemon/cerclecombat.png')
# cercle2 = pygame.image.load('./spritesheet-pokemon/cerclecombat.png')

# # Définition des couleurs
# WHITE = (255, 255, 255)
# GREEN = (0, 255, 0)
# BLACK = (0, 0, 0)
# LIGHT_GRAY = (200, 200, 200, 100)

# max_health = 350
# dracaufeu_health = 350
# pikachu_health = 350
# initial_width = 200  # Largeur initiale
# narrow_width = 100   # Largeur après l'oblique
# health_bar_height = 20
# oblique_height = 20  # Hauteur de la remontée après l' oblique
# background_height = health_bar_height + oblique_height + 10

# # Supprimer le fond blanc des cercles
# cercle1.set_colorkey((255, 255, 255))
# cercle2.set_colorkey((255, 255, 255))

# cercle1 = pygame.transform.scale(cercle1, (250, 100))
# cercle2 = pygame.transform.scale(cercle2, (400, 150))

# # Variables d'animation
# clock = pygame.time.Clock()
# time_elapsed = 0
# amplitude_vertical = 5
# amplitude_horizontal = 5
# speed = 2

# # def draw_health_bar(x, y, current_health, name):
# #     health_ratio = current_health / max_health
# #     initial_health_width = int(initial_width * health_ratio)
# #     narrow_health_width = int(narrow_width * health_ratio)

# #     # Fond gris 
# #     background_rect = pygame.Surface((initial_width + 2, background_height), pygame.SRCALPHA)
# #     background_rect.fill(LIGHT_GRAY)
# #     screen.blit(background_rect, (x, y - 8))

# #     # Barre de vie en vert
# #     points = [(x, y),
# #               (x + initial_health_width, y),
# #               (x + initial_health_width, y + health_bar_height),
# #               (x + initial_health_width - (initial_width - narrow_width), y + health_bar_height + oblique_height),
# #               (x + narrow_health_width, y + health_bar_height + oblique_height),
# #               (x + narrow_health_width, y + health_bar_height),
# #               (x, y + health_bar_height)]

# #     pygame.draw.polygon(screen, GREEN, points)
# #     pygame.draw.polygon(screen, BLACK, points, 2)

    
# #     font = pygame.font.SysFont(None, 24)
# #     health_text = font.render(f"{current_health} / {max_health}", True, BLACK)
# #     name_text = font.render(f"{name} LV: 1", True, BLACK)

# #     screen.blit(name_text, (x, y - 20))
# #     screen.blit(health_text, (x, y + 25))

# # Menu contextuel
# menu_width, menu_height = 500, 80
# menu_x = 600
# menu_y = 630
# menu_surface = pygame.Surface((menu_width, menu_height), pygame.SRCALPHA)
# menu_surface.fill((200, 200, 200, 180))  

# # Positions des boutons
# button_width, button_height = 120, 40
# gap = 20

# button_attack = pygame.Rect(menu_x + 30, menu_y + 20, button_width, button_height)
# button_bag = pygame.Rect(button_attack.right + gap, menu_y + 20, button_width, button_height)
# button_run = pygame.Rect(button_bag.right + gap, menu_y + 20, button_width, button_height)

# selected_button = None


# font = pygame.font.SysFont(None, 24)

# jouer = True

# while jouer:
#     mouse_pos = pygame.mouse.get_pos()

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             jouer = False
#             pygame.quit()

#         if event.type == pygame.MOUSEMOTION:
#             if button_attack.collidepoint(mouse_pos):
#                 selected_button = "attack"
#             elif button_bag.collidepoint(mouse_pos):
#                 selected_button = "bag"
#             elif button_run.collidepoint(mouse_pos):
#                 selected_button = "run"
#             else:
#                 selected_button = None

#         if event.type == pygame.MOUSEBUTTONDOWN:
#             if button_attack.collidepoint(event.pos):
#                 dracaufeu_health = max(0, dracaufeu_health - 50)  # Dracaufeu test
#             elif button_bag.collidepoint(event.pos):
#             elif button_run.collidepoint(event.pos):

#     time_elapsed += speed
#     mouvement_y = int(amplitude_vertical * math.sin(time_elapsed * 0.1))
#     mouvement_x = int(amplitude_horizontal * math.sin(time_elapsed * 0.08))

#     screen.blit(background, (0, 0))
#     screen.blit(cercle1, (775, 280))
#     screen.blit(cercle2, (200, 600))
#     screen.blit(perso1, (800, 200 + mouvement_y))
#     screen.blit(perso2, (300 + mouvement_x, 525))

    
#     draw_health_bar(120, 520, dracaufeu_health, "Dracaufeu")  
#     draw_health_bar(970, 175, pikachu_health, "Pikachu")  

#     screen.blit(menu_surface, (menu_x, menu_y))

#     # Couleur hover
#     color_attack = (255, 255, 255) if selected_button == "attack" else (100, 100, 100)
#     color_bag = (255, 255, 255) if selected_button == "bag" else (100, 100, 100)
#     color_run = (255, 255, 255) if selected_button == "run" else (100, 100, 100)

#     screen.blit(font.render("- Attaque -", True, color_attack), (button_attack.x + 10, button_attack.y + 10))
#     screen.blit(font.render("- Sac -", True, color_bag), (button_bag.x + 30, button_bag.y + 10))
#     screen.blit(font.render("- Fuite -", True, color_run), (button_run.x + 20, button_run.y + 10))

#     pygame.display.flip()
#     clock.tick(60)