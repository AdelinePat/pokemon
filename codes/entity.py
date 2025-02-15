import pygame
from codes.tool import Tool
from codes.keylistener import KeyListener
from codes.screen import Screen

class Entity(pygame.sprite.Sprite):
    def __init__(self, keyListener: KeyListener, screen: Screen, x: int, y: int):
        super().__init__()
        self.keyListener = keyListener
        self.screen = screen
        self.spritesheet = pygame.image.load("assets/sprite/hero_01_red_m_walk.png")  # Charger spritesheet
        self.image = Tool.split_image(self.spritesheet, 0, 0, 30, 32)
        self.position: pygame.math.Vector2 = pygame.math.Vector2(x + 16, y)
        self.rect: pygame.Rect = self.image.get_rect()
        self.all_images = self.get_all_images(self.spritesheet)  
        self.index_image = 0
        self.image_part = 0 #pour qu'il marche un coup à gauche un coup à droite
        self.hitbox: pygame.Rect = pygame.Rect(0, 0, 16, 16)  # coordonnées des PNJ
        self.step = 0
        self.animation_walk = False
        self.direction = "down"
        self.animation_steptime = 0.0  # mise à jour du compteur ecran
        self.action_animation = 16  # si steptime > action_animation on avance de 1px
        self.reset_animation = False
        self.speed = 1

    def update(self):
        self.animation_sprite()
        self.move()
        self.rect.center = self.position
        self.hitbox.midbottom = self.rect.midbottom  # hitbox localiser sur le corps pas sur la tete
        self.image = self.all_images[self.direction][self.index_image]




    def move_left(self):
        self.animation_walk = True
        self.direction = "left"
        # self.image = self.all_images["left"][self.index_image]

    def move_right(self):
        self.animation_walk = True
        self.direction = "right"
        # self.image = self.all_images["right"][self.index_image]

    def move_up(self):
        self.animation_walk = True
        self.direction = "up"
        # self.image = self.all_images["up"][self.index_image]

    def move_down(self):
        self.animation_walk = True
        self.direction = "down"
        # self.image = self.all_images["down"][self.index_image]

    def animation_sprite(self):
        if int(self.step // 8) + self.image_part >= 4:
            self.image_part = 0
            self.reset_animation = True
        

        self.index_image = int(self.step // 8) + self.image_part

    def move(self) -> None:
        if self.animation_walk:
            self.animation_steptime += self.screen.get_deltatime()
            if self.step < 16 and self.animation_steptime >= self.action_animation:
                self.step += self.speed
                if self.direction == "left":
                    self.position.x -= self.speed
                elif self.direction == "right":
                    self.position.x += self.speed
                elif self.direction == "up":
                    self.position.y -= self.speed
                elif self.direction == "down":
                    self.position.y += self.speed
                self.animation_steptime = 0
            elif self.step >= 16:
                self.step = 0
                self.animation_walk = False
                if self.reset_animation:
                    self.reset_animation = False
                else:
                    if self.image_part == 0:
                        self.image_part = 2
                    else:
                        self.image_part = 0
    

    def align_hitbox(self) -> None:
        self.rect.center = self.position
        self.hitbox.midbottom = self.rect.midbottom
        while self.hitbox.x % 16 != 0:
            self.rect.x -= 1
            self.hitbox.midbottom = self.rect.midbottom
        while self.hitbox.y % 16 != 0:
            self.rect.y -= 1
            self.hitbox.midbottom = self.rect.midbottom
        self.position = pygame.math.Vector2(self.rect.center)
        print(self.hitbox)

    def get_all_images(self, spritesheet):
        all_images = {
            "down": [],
            "left": [],
            "right": [],
            "up": []
        }

        width: int = spritesheet.get_width() // 4
        height: int = spritesheet.get_height() // 4

        for i in range(4):
            for j, key in enumerate(all_images.keys()):
                all_images[key].append(Tool.split_image(spritesheet, i * width, j * height, 24, 32))
        return all_images
