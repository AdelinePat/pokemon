import pygame
import random
import os

pygame.init()


largeur, hauteur = 1220, 720
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption('Pokemon Battle')

def load_background(path):
    
    background = pygame.image.load(path).convert()
    return pygame.transform.scale(background, (largeur, hauteur))

def generate_random_pokemon(pokemon):
    
    pokemon_path = f"./assets/image-pokemon/{pokemon}.png"
    img = pygame.image.load(pokemon_path)
    scale_factor = 2  
    img = pygame.transform.scale(img, (img.get_width() * scale_factor, img.get_height() * scale_factor))
    img_rect = img.get_rect()
    return {'img': img, 'rect': img_rect, 'original_img': img}

def get_centered_position(pokemons, espacement):
    
    total_width = sum(pokemon['rect'].width for pokemon in pokemons) + espacement * (len(pokemons) - 1)
    start_x = (largeur - total_width) // 2
    for i, pokemon in enumerate(pokemons):
        pokemon['rect'].x = start_x + i * (pokemon['rect'].width + espacement)
        pokemon['rect'].y = hauteur // 2 - pokemon['rect'].height // 2  

def draw_outline(img, rect, thickness):
    
    mask = pygame.mask.from_surface(img)
    outline_surface = pygame.Surface(img.get_size(), pygame.SRCALPHA)
    outline_surface.fill((0, 0, 0, 0))  

    
    for i in range(thickness):
        for point in mask.outline():
            outline_surface.set_at((point[0] + i, point[1] + i), (255, 255, 255))  

    return outline_surface, rect

def draw_pokemon_with_hover(pokemon, mouse_x, mouse_y, fenetre):
    
    if pokemon['rect'].collidepoint(mouse_x, mouse_y):
        
        zoom_factor = 1.4
        new_width = int(pokemon['rect'].width * zoom_factor)
        new_height = int(pokemon['rect'].height * zoom_factor)
        zoomed_img = pygame.transform.scale(pokemon['original_img'], (new_width, new_height))
        zoomed_rect = zoomed_img.get_rect(center=pokemon['rect'].center)  

        
        fenetre.blit(zoomed_img, zoomed_rect.topleft)

        
        outline_surface, _ = draw_outline(zoomed_img, zoomed_rect, 5)
        fenetre.blit(outline_surface, zoomed_rect.topleft)
    else:
        
        fenetre.blit(pokemon['img'], pokemon['rect'].topleft)


background = load_background('./assets/spritesheet-pokemon/centre-pokemon.png')


pokemon_files = [f.split('.')[0] for f in os.listdir("./assets/image-pokemon") if f.endswith(".png")]
random_pokemons = random.sample(pokemon_files, 3)
data = [generate_random_pokemon(pokemon) for pokemon in random_pokemons]

# Centre les Pokémon a l'horizontal ;)
espacement = 200
get_centered_position(data, espacement)

# Boucle principale
going = True
while going:
    fenetre.blit(background, (0, 0))

    mouse_x, mouse_y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            going = False

    # Affiche le hover et contour
    for pokemon in data:
        draw_pokemon_with_hover(pokemon, mouse_x, mouse_y, fenetre)

    pygame.display.flip()

pygame.quit()
