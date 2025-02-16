import pygame

class UtilTool():
    def draw_text(self, text, font, font_size, screen, center, color="black"):
        font_load = pygame.font.Font(font, font_size)
        dialog = font_load.render(text, True, color)
        dialog_rect = dialog.get_rect(center = center)
        screen.display.blit(dialog, dialog_rect)

    def draw_color_filter(self, screen, color=(0,0,0)):
        background_screen = pygame.Surface((screen.width, screen.height))
        background_rect = background_screen.get_rect(center = (screen.width //2, screen.height // 2))
        background_screen.set_alpha(155)
        pygame.draw.rect(background_screen, color, background_rect)
        screen.display.blit(background_screen, background_rect)

    def draw_window_with_background(self, screen, color=(255,255,255)):
        window_surface = pygame.Surface((screen.width //2, screen.height // 2))
        window_surface.fill(color)
        window_rect = window_surface.get_rect(center = (screen.width //2, screen.height // 2))

        screen.display.blit(window_surface, window_rect)


