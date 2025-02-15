import pygame


class Screen:
    def __init__(self):
        self.display = pygame.display.set_mode((1200, 720))
        pygame.display.set_caption("Pokémon")
        self.clock = pygame.time.Clock()
        self.framerate = 144
        self.deltatime = 0 #raffrachissement fenetre
        # Ajouter le logo
        self.caption = pygame.display.set_caption("Pokémon")
        self.screen = pygame.display.set_icon(pygame.image.load("assets/logo/pokeball.jpg"))

    def update(self):
        pygame.display.flip()
        pygame.display.update()
        self.clock.tick(self.framerate) #raffraichissement de l'écran
        self.display.fill((0, 0, 0)) #efface l'écran
        self.deltatime = self.clock.get_time()

    def get_deltatime(self):
        return self.deltatime


    def get_size(self):
        return self.display.get_size()

    def get_display(self):
        return self.display
