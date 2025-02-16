import pygame
import math

from __settings__ import POKE_FONT, REGULAR_FONT

pygame.init()

# Configuration de la fenêtre
fenetre = pygame.display.set_mode((1220, 720))
pygame.display.set_caption('Pokemon Battle')

# Chargement des images
background = pygame.image.load('./assets/spritesheet-pokemon/fondCombat.png').convert()
background = pygame.transform.scale(background, (1220, 720))

perso1 = pygame.image.load('./assets/spritesheet-pokemon/pika.png')
perso1 = pygame.transform.scale(perso1, (200, 200))

perso2 = pygame.image.load('./assets/spritesheet-pokemon/draco.png')
perso2 = pygame.transform.scale(perso2, (200, 200))

cercle1 = pygame.image.load('./assets/spritesheet-pokemon/cerclecombat.png')
cercle2 = pygame.image.load('./assets/spritesheet-pokemon/cerclecombat.png')

# Supprimer le fond blanc des cercles
cercle1.set_colorkey((255, 255, 255))
cercle2.set_colorkey((255, 255, 255))


cercle1 = pygame.transform.scale(cercle1, (250, 100))
cercle2 = pygame.transform.scale(cercle2, (400, 150))

# Variables d'animation
clock = pygame.time.Clock()
time_elapsed = 0
amplitude_vertical = 5
amplitude_horizontal = 5
speed = 2

# Définition des couleurs
WHITE = (255, 255, 255)
LIGHT_GRAY_TRANSPARENT = (200, 200, 200, 180)  
HIGHLIGHT_COLOR = (255, 255, 255)
NORMAL_COLOR = (100, 100, 100)


font = pygame.font.Font(REGULAR_FONT, 40)

# menu contextuelle
menu_width, menu_height = 500, 80
menu_x = 600  
menu_y = 630  
menu_surface = pygame.Surface((menu_width, menu_height), pygame.SRCALPHA)
menu_surface.fill(LIGHT_GRAY_TRANSPARENT)

# Positions des boutons
button_width, button_height = 120, 40
gap = 20  

button_attack = pygame.Rect(menu_x + 30, menu_y + 20, button_width, button_height)
button_bag = pygame.Rect(button_attack.right + gap, menu_y + 20, button_width, button_height)
button_run = pygame.Rect(button_bag.right + gap, menu_y + 20, button_width, button_height)

selected_button = None

jouer = True

while jouer:
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jouer = False
            pygame.quit()

        if event.type == pygame.MOUSEMOTION:
            if button_attack.collidepoint(mouse_pos):
                selected_button = "attack"
            elif button_bag.collidepoint(mouse_pos):
                selected_button = "bag"
            elif button_run.collidepoint(mouse_pos):
                selected_button = "run"
            else:
                selected_button = None

        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_attack.collidepoint(event.pos):
                print("Attaque sélectionnée !")
            elif button_bag.collidepoint(event.pos):
                print("Sac ouvert !")
            elif button_run.collidepoint(event.pos):
                print("Fuite tentée !")

    
    time_elapsed += speed
    mouvement_y = int(amplitude_vertical * math.sin(time_elapsed * 0.1))
    mouvement_x = int(amplitude_horizontal * math.sin(time_elapsed * 0.08))

    
    fenetre.blit(background, (0, 0))
    fenetre.blit(cercle1, (775, 280))
    fenetre.blit(cercle2, (200, 600))
    fenetre.blit(perso1, (800, 200 + mouvement_y))
    fenetre.blit(perso2, (300 + mouvement_x, 525))

    
    fenetre.blit(menu_surface, (menu_x, menu_y))

    # couleur hover
    color_attack = HIGHLIGHT_COLOR if selected_button == "attack" else NORMAL_COLOR
    color_bag = HIGHLIGHT_COLOR if selected_button == "bag" else NORMAL_COLOR
    color_run = HIGHLIGHT_COLOR if selected_button == "run" else NORMAL_COLOR

    
    fenetre.blit(font.render("- Attaque -", True, color_attack), (button_attack.x + 10, button_attack.y))
    fenetre.blit(font.render("- Sac -", True, color_bag), (button_bag.x + 30, button_bag.y))
    fenetre.blit(font.render("- Fuite -", True, color_run), (button_run.x + 20, button_run.y))

    pygame.display.flip()
    clock.tick(60)
