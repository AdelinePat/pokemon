import pygame

class Screen:
    def __init__(self, width=1200, height=720):
        self.width = width
        self.height = height
        self.display = pygame.display.set_mode((self.width, self.height))
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
    
    def set_background_display(self, background_image):
        background = pygame.transform.smoothscale(pygame.image.load(background_image), (self.width, self.height))
        background_rect = background.get_rect()
        self.display.blit(background, background_rect)

        background_screen = pygame.Surface((self.width, self.height))
        background_rect = background_screen.get_rect(center = (self.width //2, self.height // 2))
        background_screen.set_alpha(155)
        pygame.draw.rect(background_screen, (0,0,0), background_rect)
        self.display.blit(background_screen, background_rect)
