import pygame
from __settings__ import REGULAR_FONT, BACKGROUND, DARK_GREEN, LIGHT_GREEN, BATTLE_BACKGROUND, BATTLE_FLOOR

class UtilTool():
    def draw_text(self, text, font, font_size, screen, my_center, color=DARK_GREEN):
        font_load = pygame.font.Font(font, font_size)
        dialog = font_load.render(text, True, color)
        dialog_rect = dialog.get_rect(center = my_center)
        screen.display.blit(dialog, dialog_rect)

    def draw_color_filter(self, screen, color="black"):
        background_screen = pygame.Surface((screen.width, screen.height))
        background_rect = background_screen.get_rect(center = (screen.width //2, screen.height // 2))
        background_screen.set_alpha(155)
        pygame.draw.rect(background_screen, color, background_rect)
        screen.display.blit(background_screen, background_rect)

    def load_image(self, image):
        return pygame.image.load(image)
    
    def display_asset_battle(self, screen, image, scale_x, scale_y, x, y):
        image.set_colorkey((255, 255, 255))
        battle_floor = pygame.transform.scale(image, (scale_x, scale_y))
        battle_floor_rect = battle_floor.get_rect(center = (x, y))
        screen.display.blit(battle_floor, battle_floor_rect)

    def display_assets_and_background(self, screen, x_movement, y_movement, battle_floor, battle_floor2, pokemon_enemy, pokemon):
        screen.set_background_without_black(BATTLE_BACKGROUND)
        floor1 = self.display_asset_battle(screen, battle_floor, screen.width // 5, screen.height // 7, screen.width // 10 * 7.5, screen.height // 7 * 3.2)
        floor = self.display_asset_battle(screen, battle_floor2, screen.width // 3, screen.height // 5, screen.width // 10 * 2.5, screen.height // 7 * 6.6)

        enemy = self.display_asset_battle(screen, pokemon_enemy, screen.width //6, screen.width //6, screen.width // 10 * 7.5 + x_movement, screen.height // 7 * 3)
        my_pokemon = self.display_asset_battle(screen, pokemon, screen.width // 3, screen.width // 3, screen.width // 10 * 2.5, screen.height // 7 * 6.4 + y_movement)


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