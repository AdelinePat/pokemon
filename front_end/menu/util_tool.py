import pygame
from __settings__ import REGULAR_FONT, BACKGROUND, DARK_GREEN, LIGHT_GREEN

class UtilTool():
    def draw_text(self, text, font, font_size, screen, my_center, color=DARK_GREEN):
        font_load = pygame.font.Font(font, font_size)
        dialog = font_load.render(text, True, color)
        dialog_rect = dialog.get_rect(center = my_center)
        screen.display.blit(dialog, dialog_rect)

    def draw_color_filter(self, screen, color=DARK_GREEN):
        background_screen = pygame.Surface((screen.width, screen.height))
        background_rect = background_screen.get_rect(center = (screen.width //2, screen.height // 2))
        background_screen.set_alpha(155)
        pygame.draw.rect(background_screen, color, background_rect)
        screen.display.blit(background_screen, background_rect)

    def draw_window_with_background(self, screen, width, height, color=BACKGROUND):

# screen.width //2.5
        window_surface = pygame.Surface((screen.width, screen.height), pygame.SRCALPHA)
        # window_surface.fill(color)
        window_surface.set_alpha(180)
        
        window_rect = window_surface.get_rect(center = (screen.width //2, screen.height // 2))
        
        my_window_rect = pygame.rect.Rect(0,0, width, height)
        my_window_rect.center = (screen.width//2, screen.height//2)

        my_border_rect = pygame.rect.Rect(0,0, width, height)
        my_border_rect.center = (screen.width//2, screen.height//2)
        # my_border_rect.center = (screen.width //2, screen.height //2)

        
        final_background_rect = pygame.draw.rect(window_surface, BACKGROUND, my_window_rect, border_radius=10)
        
        final_rect = pygame.draw.rect(window_surface, DARK_GREEN, my_border_rect, 3, border_radius=10)
        
        screen.display.blit(window_surface, window_rect)
        

    def draw_option_screen(self, screen):

        # self.screen.width//2 + i * 200, self.screen.height//8*7  , color
        window_surface = pygame.Surface((screen.width, screen.height), pygame.SRCALPHA)
        # window_surface.fill(color)
        
        window_surface.set_alpha(180)

        window_rect = window_surface.get_rect(center = (screen.width //2, screen.height //2))
        
        my_window_rect = pygame.rect.Rect(0,0, screen.width //1.75, screen.height //8)
        my_window_rect.center = (screen.width//4*2.75, screen.height//8*7)

        my_border_rect = pygame.rect.Rect(0,0, screen.width //1.75, screen.height //8)
        my_border_rect.center = (screen.width//4*2.75, screen.height//8*7)
        # my_border_rect.center = (screen.width //2, screen.height //2)
        final_background_rect = pygame.draw.rect(window_surface, BACKGROUND, my_window_rect, border_radius=10)
        final_rect = pygame.draw.rect(window_surface, DARK_GREEN, my_border_rect, 3, border_radius=10)
        
        screen.display.blit(window_surface, window_rect)


    def draw_info_attack_screen(self, screen, message1, message2):
        # self.util.draw_color_filter(self.screen)
        #BLABLA
        self.draw_window_with_background(screen, screen.width // 1.7, screen.height // 6.5)
        font_size = screen.height // 20
        x  = screen.width //2
        y = screen.height // 2
        
        self.draw_text(message1,\
                              REGULAR_FONT, font_size , screen, (x, y - font_size * 0.5))
        self.draw_text(message2,\
                                REGULAR_FONT, font_size , screen, (x, y + font_size * 0.5))
        
    def draw_info_capture_screen(self, screen, message1):
        # self.util.draw_color_filter(self.screen)
        #BLABLA
        self.draw_window_with_background(screen, screen.width // 1.5, screen.height // 6.5)
        font_size = screen.height // 20
        x  = screen.width //2
        y = screen.height // 2
        
        self.draw_text(message1,\
                              REGULAR_FONT, font_size , screen, (x, y))