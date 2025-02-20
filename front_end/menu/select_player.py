import pygame
import sys

# from codes.name_input import NameInput  
# from codes.game import Game
# from codes.select_player import SelectPlayer
from back_end.controller import get_player_names
from __settings__ import MAIN_MENU_BACKGROUND2, LIGHT_GREEN, REGULAR_FONT, DARK_GREEN
from front_end.menu.util_tool import UtilTool


class SelectPlayer:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 50)
        self.options = get_player_names()
        self.selected_index = 0
        self.running = True
        self.util = UtilTool()

    def display(self):
        while self.running:
            self.screen.update()
            self.screen.get_display().fill((0, 0, 0))

            self.screen.set_background_display(MAIN_MENU_BACKGROUND2)
            font_size = self.screen.height // 10
            self.util.draw_text("Select your player",REGULAR_FONT, font_size, self.screen,\
                                 (self.screen.width//2, self.screen.height // 10*2), LIGHT_GREEN)

            # for i, option in enumerate(self.options):
            #     color = LIGHT_GREEN if i == self.selected_index else (255, 255, 255)
            #     self.util.draw_text(option, REGULAR_FONT, font_size,\
            #                         self.screen, (self.screen.width //2, self.screen.height // 10*3 + i*60), color)
            for i, option in enumerate(self.options):
                if i == self.selected_index:
                    color = LIGHT_GREEN
                else:
                    color = "white"

                y = i % 5
                if i in range(0,5):
                    self.util.draw_text(option, REGULAR_FONT, self.screen.height//22, self.screen,\
                                    (self.screen.width // 8*2, self.screen.height // 8 * y + self.screen.height // 8*3), color)
                
                elif i in range(5, 10):
                    self.util.draw_text(option, REGULAR_FONT, self.screen.height//22, self.screen,\
                                    (self.screen.width // 8*4, self.screen.height // 8 * y + self.screen.height // 8*3), color)

                elif i in range(10, 15):
                    self.util.draw_text(option, REGULAR_FONT, self.screen.height//22, self.screen,\
                                        (self.screen.width // 8*6, self.screen.height // 8 * y + self.screen.height // 8*3), color)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    
                    if event.key == pygame.K_DOWN:
                        self.selected_index = (self.selected_index + 1) % len(self.options)
                    elif event.key == pygame.K_UP:
                        self.selected_index = (self.selected_index - 1) % len(self.options)

                    elif event.key == pygame.K_RETURN:
                        for index in range(len(self.options)):
                            if self.selected_index == index:
                                return self.options[index]

                    elif event.key == pygame.K_ESCAPE:
                        pass
                        # return