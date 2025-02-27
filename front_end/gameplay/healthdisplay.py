import pygame
from __settings__ import DARK_GREEN, LIGHT_GREEN, REGULAR_FONT, LIGHT_RED
from front_end.menu.util_tool import UtilTool

class HealthDisplay():
    def __init__(self):
        self.util = UtilTool()

    def draw_health_bar(self, x, y, pokemon, hp_max, screen, my_center, who_is_displayed="player"):
        width = screen.width // 4
        height = screen.height // 10
        healthbar_width = width - 20
        if hp_max == pokemon.get_hp_max():
            hp_ratio = healthbar_width * (pokemon.get_hp() / pokemon.get_hp_max())
        else:
            actual_hp = pokemon.get_hp() + (pokemon.get_hp_max() - hp_max)
            hp_ratio = healthbar_width * (actual_hp / pokemon.get_hp_max())
        if pokemon.get_hp() <= 0:
            hp_ratio = 0

        self.util.draw_small_window_with_background(screen, width, height, my_center)

        font_size = screen.height // 35
        pet_name = pokemon.pet_name.split()[0]

        self.util.draw_text_from_top_left(f"{pokemon.name} : {pet_name}", REGULAR_FONT,\
                            font_size, screen,\
                            ((my_center[0] - screen.width // 8.5), (my_center[1] - screen.height // 25)))
        
        self.util.draw_text_from_top_left(f"lvl : {pokemon.get_level()}", REGULAR_FONT,\
                            font_size, screen,\
                            ((my_center[0] - screen.width // 8.5), (my_center[1] + screen.height // 50)))
        
        window_surface = pygame.Surface((screen.width, screen.height), pygame.SRCALPHA)
        window_rect = window_surface.get_rect(center = (screen.width //2, screen.height // 2))

        
        health_bar_background = pygame.rect.Rect(0,0, healthbar_width, 18)
        health_bar_background.midleft = (my_center[0] -healthbar_width // 2, my_center[1]+3)
        final_health_bar_background = pygame.draw.rect(window_surface, LIGHT_RED,\
                                                       health_bar_background, border_radius=10)       
        
        health_bar_actual = pygame.rect.Rect(0,0, hp_ratio, 18)
        if who_is_displayed == "enemy":
            health_bar_actual.midright = (my_center[0]+healthbar_width // 2, my_center[1]+3)
        else:
            health_bar_actual.midleft = (my_center[0]-healthbar_width // 2, my_center[1]+3)

        final_health_bar_actual = pygame.draw.rect(window_surface, LIGHT_GREEN,\
                                                health_bar_actual, border_radius=10)
        health_bar_border = pygame.draw.rect(window_surface, DARK_GREEN,\
                                            health_bar_background, 3, border_radius=10)

        screen.display.blit(window_surface, window_rect)

        if hp_max == pokemon.get_hp_max():
            self.util.draw_text_from_bottom_right(f"{pokemon.get_hp()} / {pokemon.get_hp_max()}", REGULAR_FONT,\
                                font_size, screen,\
                                ((my_center[0] + screen.width // 8.75), (my_center[1] + screen.height // 21)))
        else:
            self.util.draw_text_from_bottom_right(f"{actual_hp} / {pokemon.get_hp_max()}", REGULAR_FONT,\
                                font_size, screen,\
                                ((my_center[0] + screen.width // 8.75), (my_center[1] + screen.height // 21)))
