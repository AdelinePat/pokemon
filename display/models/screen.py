import pygame

class Screen:
    def __init__(self, background, caption, width=1200, height=720):
        self.width = width
        self.height = height
        self.size = (self.width, self.height)       
        self.screen = pygame.display.set_mode(self.size)
        # self.size = self.screen.get_size()
        
        # self.icon = self.get_icon()
        
        self.background = self.set_background(background, caption)

    def get_font(self, size):
        return pygame.font.Font("assets/font.ttf", size)

    def update_display(self):
        pygame.display.update()

    def set_background(self, background, caption):
        pygame.display.set_caption(caption)
        final_background = pygame.transform.smoothscale(
            pygame.image.load(background), self.size)
        return final_background
        
    
    def get_icon(self):
        size = (40,40)
        icon_smoothedscaled = pygame.transform.smoothscale("test.png".convert_alpha(), size)
        # icon_rotate = pygame.transform.rotozoom(icon_smoothedscaled, 25, 10)
        final_icon = pygame.display.set_icon(icon_smoothedscaled)

        return final_icon