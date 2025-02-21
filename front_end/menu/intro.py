import pygame
from __settings__ import CHEN

pygame.init()

class IntroChoice():
    def __init__(self, player_name, screen):
        self.player_name = player_name
        self.screen = screen
        self.chen_image = pygame.image.load(CHEN)
        self.chen_image = pygame.transform.scale(self.chen_image, (1110, 550))
        self.dialogues = [
            f"Welcome to the Pokemon Center {self.player_name},\n I'm professor Oak.",
            "The Pokemon world is vast and fascinating, trainers and extraordinary creatures named pokemon live together.\nEach pokemon has its own unique caracteristics and is able to evolve in more powerful form.",
            "As a trainer, you'll have to travel the world to capture and train Pokemons.\nYour goal is to become a Pokemon League Champion after winning fight against other trainers in arena and win badges.",
            "You'll need to be brave and smart, use your Pokemons ability in the best way.\nEach fight you win, your Pokemon will gain experience, making them stronger."
            "To help you achieve your goal, you can choose among this three Pokemons to start your adventure.\nGood luck !"
        ]
        self.dialogues_fr = [
            f"Bonjour {self.player_name}, bienvenue au centre Pokémon.\nJe suis le Professeur Chen.",
            "L'univers de Pokémon est un monde riche et fascinant, où les humains, appelés Dresseurs, et des créatures fantastiques appelées Pokémon coexistent.\nChaque Pokémon possède des caractéristiques uniques et la capacité d'évoluer en formes plus puissantes.",
            "Ton rôle en tant que dresseur sera de voyager à travers différentes régions pour capturer et entraîner des Pokémon.\nTon objectif est de devenir un Maître Pokémon en remportant des badges d'arène et en affrontant d'autres Dresseurs.",
            "Fais preuve de force et d'intelligence pour exploiter au mieux les capacités de tes Pokémon.\nChaque combat réussi leur fera gagner de l'expérience, les rendant plus forts et pouvant les faire évoluer !",
            "Pour t'aider à accomplir ton objectif, tu pourras choisir un Pokémon pour débuter ton aventure.\nBonne chance !"
        ]

    def display(self):
        show_intro = True
        dialogue_index = 0

        while True:
            self.screen.display.fill((173, 216, 230))
            pygame.draw.circle(self.screen.display, (255, 255, 255), (300, 150), 80)
            pygame.draw.circle(self.screen.display, (255, 255, 255), (350, 130), 90)
            pygame.draw.circle(self.screen.display, (255, 255, 255), (400, 150), 80)
            pygame.draw.circle(self.screen.display, (255, 255, 255), (1000, 200), 100)
            pygame.draw.circle(self.screen.display, (255, 255, 255), (1050, 170), 110)
            pygame.draw.circle(self.screen.display, (255, 255, 255), (1100, 200), 100)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        dialogue_index += 1 
                        if dialogue_index >= len(self.dialogues):
                            show_intro = False
            
            if not show_intro:
                return

            dialogue_index = self.professor_chen_talk(self.screen.display, self.dialogues, self.chen_image, dialogue_index)

            pygame.display.flip()

    def professor_chen_talk(self, fenetre, dialogues, image, dialogue_index):

        chen_rect = image.get_rect(midbottom=(self.screen.width // 2, self.screen.height))
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

        return dialogue_index