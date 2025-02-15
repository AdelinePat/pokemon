class Button2():
    def __init__(self, text, screen_size, screen):
        self.text = text
        self.width = self.get_text_rect().get_size()[0]
        self.height = self.get_text_rect().get_size()[1]
        self.rect = self.get_text_rect()
        self.center = (self.width // 2, self.height // 2)
        self.screen = screen
        self.screen_size = screen_size
    
    def get_font(self, size, font=MAIN_FONT):
        return pygame.font.Font(font, size)

    def get_text_rect(self, size, font=MAIN_FONT, color=FONT_COLOR):
        # render(text, antialias, color, background=None) -> Surface


        # font = pygame.font.Font.render(self.text, True, color)
        font_load = self.get_font(size, font)
        dialog = font_load.render(self.text, True, color)

        dialog_rect = dialog.get_rect()
        # dialog_size = dialog_rect.get_size()
        # self.rect = dialog_rect
        
        return dialog_rect
    
    def render_button(self):
        background_rect, background_button = self.get_button_background()
        self.screen.blit(background_button, background_rect)


    def set_button_position(self):
        pass


    def get_button_background(self):
        text_rect = self.get_text_rect()
        text_rect.get_rect(center = self.center)
        background_button = pygame.Surface((self.width, self.height))
        background_rect = background_button.get_rect(center = self.center)
        background_button.set_alpha(155)
        pygame.draw.rect(background_button, (0,0,0), background_rect)

        return background_rect, background_button