import pygame, sys
from button import Button
from screen import Screen

pygame.init()


class Menu(Screen):
    def __init__(self):
        super().__init__()
        self.bg = pygame.transform.scale(pygame.image.load("assets/background.jpg"), (self.screen.get_width(), self.screen.get_height()))

    def play(self):
        while True:
            play_back = Button(image=None, pos=(400, 460), text_input="BACK", font=self.get_font(75), base_color="White", hovering_color="Green")
            play_back.changeColor(pygame.mouse.get_pos())
            play_back.update(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and play_back.checkForInput(pygame.mouse.get_pos()):
                    self.main_menu()
            
            self.update_display()
    
    def options(self):
        while True:
            self.screen.fill("white")
            options_text = self.get_font(45).render("This is the OPTIONS screen.", True, "Black")
            options_rect = options_text.get_rect(center=(400, 260))
            self.screen.blit(options_text, options_rect)

            options_back = Button(image=None, pos=(400, 460), text_input="BACK", font=self.get_font(75), base_color="Black", hovering_color="Green")
            options_back.changeColor(pygame.mouse.get_pos())
            options_back.update(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and options_back.checkForInput(pygame.mouse.get_pos()):
                    self.main_menu()

            self.update_display()
    
    def main_menu(self):
        while True:
            self.screen.blit(self.bg, (0, 0))
            menu_mouse_pos = pygame.mouse.get_pos()

            menu_text = self.get_font(80).render("MAIN MENU", True, "#b68f40")
            menu_rect = menu_text.get_rect(center=(400, 100))
            self.screen.blit(menu_text, menu_rect)

            play_button = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(400, 250), text_input="Start", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")
            options_button = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(400, 400), text_input="Resume Game", font=self.get_font(50), base_color="#d7fcd4", hovering_color="White")
            quit_button = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(400, 550), text_input="QUIT", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")

            for button in [play_button, options_button, quit_button]:
                button.changeColor(menu_mouse_pos)
                button.update(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button.checkForInput(menu_mouse_pos):
                        self.play()
                    if options_button.checkForInput(menu_mouse_pos):
                        self.options()
                    if quit_button.checkForInput(menu_mouse_pos):
                        pygame.quit()
                        sys.exit()
            
            self.update_display()

if __name__ == "__main__":
    menu = Menu()
    menu.main_menu()
