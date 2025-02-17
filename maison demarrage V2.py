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

def load_image(path, scale=1):
    img = pygame.image.load(path).convert_alpha()
    img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
    return img

def generate_random_pokemon(pokemon):
    pokemon_path = f"image-pokemon/{pokemon}.png"
    img = load_image(pokemon_path, 2)
    img_rect = img.get_rect()
    return {'img': img, 'rect': img_rect, 'original_img': img, 'name': pokemon}

def get_centered_position(pokemons, espacement):
    total_width = sum(pokemon['rect'].width for pokemon in pokemons) + espacement * (len(pokemons) - 1)
    start_x = (largeur - total_width) // 2
    for i, pokemon in enumerate(pokemons):
        pokemon['rect'].x = start_x + i * (pokemon['rect'].width + espacement)
        pokemon['rect'].y = hauteur // 2 - pokemon['rect'].height // 2

def draw_pokemon_with_hover(pokemon, mouse_x, mouse_y, fenetre):
    if pokemon['rect'].collidepoint(mouse_x, mouse_y):
        zoom = 1.5
        new_width = int(pokemon['rect'].width * zoom)
        new_height = int(pokemon['rect'].height * zoom)
        zoomed_img = pygame.transform.scale(pokemon['original_img'], (new_width, new_height))
        zoomed_rect = zoomed_img.get_rect(center=pokemon['rect'].center)
        fenetre.blit(zoomed_img, zoomed_rect.topleft)

        # Afficher le nom des pokemon
        font = pygame.font.Font(None, 36)
        text = font.render(pokemon['name'], True, (0, 0, 0))
        text_rect = text.get_rect(midtop=(zoomed_rect.centerx, zoomed_rect.top - 10))
        fenetre.blit(text, text_rect)
    else:
        fenetre.blit(pokemon['img'], pokemon['rect'].topleft)

def professeur_chen(fenetre, dialogues, image, dialogue_index, show_intro):
    if show_intro:
        chen_rect = image.get_rect(midbottom=(largeur // 2, hauteur))
        fenetre.blit(image, chen_rect.topleft)

        font = pygame.font.Font(None, 36)
        max_width = 900  
        bubble_rect = pygame.Rect(chen_rect.centerx - max_width // 2, chen_rect.top - 140, max_width, 140)

        pygame.draw.rect(fenetre, (255, 255, 255), bubble_rect, border_radius=10)
        pygame.draw.rect(fenetre, (0, 0, 0), bubble_rect, 2, border_radius=10)

        words = dialogues[dialogue_index].split()
        lines = []
        line = ""
        for word in words:
            test_line = line + word + " "
            if font.size(test_line)[0] < max_width - 20:
                line = test_line
            else:
                lines.append(line.strip())
                line = word + " "
        lines.append(line.strip())

        for i, line in enumerate(lines):
            text = font.render(line, True, (0, 0, 0))
            text_rect = text.get_rect(midtop=(bubble_rect.centerx, bubble_rect.top + 10 + i * 30))
            fenetre.blit(text, text_rect)

    return dialogue_index, show_intro


dialogues = [
    "Bonjour jeune dresseur, bienvenue au centre Pokémon.\nJe suis le Professeur Chen.",
    "L'univers de Pokémon est un monde riche et fascinant, où les humains, appelés Dresseurs, et des créatures fantastiques appelées Pokémon coexistent.\nChaque Pokémon possède des caractéristiques uniques et la capacité d'évoluer en formes plus puissantes.",
    "Ton rôle en tant que dresseur sera de voyager à travers différentes régions pour capturer et entraîner des Pokémon.\nTon objectif est de devenir un Maître Pokémon en remportant des badges d'arène et en affrontant d'autres Dresseurs.",
    "Fais preuve de force et d'intelligence pour exploiter au mieux les capacités de tes Pokémon.\nChaque combat réussi leur fera gagner de l'expérience, les rendant plus forts et pouvant les faire évoluer !",
    "Pour t'aider à accomplir ton objectif, tu pourras choisir un Pokémon pour débuter ton aventure.\nBonne chance !"
]

background = load_background('./spritesheet-pokemon/centre-pokemon.png')
chen_img = load_image("./spritesheet-pokemon/chen.png", 3)

pokemon_files = [f.split('.')[0] for f in os.listdir("image-pokemon") if f.endswith(".png")]
random_pokemons = random.sample(pokemon_files, 3)
data = [generate_random_pokemon(pokemon) for pokemon in random_pokemons]
get_centered_position(data, 200)

dialogue_index = 0
show_intro = True

# Boucle principale
while True:
    fenetre.fill((173, 216, 230))  
    pygame.draw.circle(fenetre, (255, 255, 255), (300, 150), 80)
    pygame.draw.circle(fenetre, (255, 255, 255), (350, 130), 90)
    pygame.draw.circle(fenetre, (255, 255, 255), (400, 150), 80)
    pygame.draw.circle(fenetre, (255, 255, 255), (1000, 200), 100)
    pygame.draw.circle(fenetre, (255, 255, 255), (1050, 170), 110)
    pygame.draw.circle(fenetre, (255, 255, 255), (1100, 200), 100)

    mouse_x, mouse_y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN and show_intro:
            dialogue_index += 1
            if dialogue_index >= len(dialogues):
                show_intro = False

    dialogue_index, show_intro = professeur_chen(fenetre, dialogues, chen_img, dialogue_index, show_intro)

    if not show_intro:
        fenetre.blit(background, (0, 0))
        for pokemon in data:
            draw_pokemon_with_hover(pokemon, mouse_x, mouse_y, fenetre)

    pygame.display.flip()
