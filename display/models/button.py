import pygame
from display.models.screen import Screen
class Button(Screen):
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        """Displays the button"""
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        """Checks if the button is clicked"""
        return self.rect.collidepoint(position)

    def changeColor(self, is_selected):
        """Changes button text color based on selection"""
        if is_selected:
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)

    # def set_background_button(self):
    #     background_screen = pygame.Surface((SCREEN.width, SCREEN.height))
    #     background_rect = background_screen.get_rect(center = (SCREEN.width //2, SCREEN.height // 2))
    #     background_screen.set_alpha(155)
    #     pygame.draw.rect(background_screen, (0,0,0), background_rect)
