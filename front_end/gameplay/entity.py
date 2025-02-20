import pygame
from .tool import Tool
from .keylistener import KeyListener
from front_end.screen import Screen

class Entity(pygame.sprite.Sprite):
    def __init__(self, keyListener: KeyListener, screen: Screen, x: int, y: int):
        """
        Initializes the Entity with movement controls, sprite loading, and position.
        """
        super().__init__()
        self.keyListener = keyListener
        self.screen = screen
        self.spritesheet = pygame.image.load("assets/sprite/hero_01_red_m_walk.png")  # Load the sprite sheet
        self.image = Tool.split_image(self.spritesheet, 0, 0, 30, 32)  # Extract the initial sprite image
        self.position: pygame.math.Vector2 = pygame.math.Vector2(x + 16, y)  # Set the initial position
        self.rect: pygame.Rect = self.image.get_rect()  # Define the entity's rectangle
        self.all_images = self.get_all_images(self.spritesheet)  # Store all animation frames
        self.index_image = 0
        self.image_part = 0  # Used to alternate between left and right foot during movement animation
        self.hitbox: pygame.Rect = pygame.Rect(0, 0, 16, 16)  # Define the collision box of the entity
        self.step = 0
        self.animation_walk = False  # Indicates if the entity is currently walking
        self.direction = "down"  # Default movement direction
        self.animation_steptime = 0.0  # Timer for animation updates
        self.action_animation = 16  # Determines how frequently the character moves per frame
        self.reset_animation = False  # Used to reset animations when needed
        self.speed = 1  # Movement speed

    def update(self):
        """
        Updates the entity's animation and movement.
        """
        self.animation_sprite()  # Update the animation
        self.move()  # Move the entity if needed
        self.rect.center = self.position  # Keep the sprite aligned with the entity's position
        self.hitbox.midbottom = self.rect.midbottom  # Ensure the hitbox is aligned with the character's body
        self.image = self.all_images[self.direction][self.index_image]  # Update the current displayed sprite

    # Movement methods to set the walking animation and direction
    def move_left(self):
        self.animation_walk = True
        self.direction = "left"

    def move_right(self):
        self.animation_walk = True
        self.direction = "right"

    def move_up(self):
        self.animation_walk = True
        self.direction = "up"

    def move_down(self):
        self.animation_walk = True
        self.direction = "down"

    def animation_sprite(self):
        """
        Handles the animation frames during movement.
        """
        if int(self.step // 8) + self.image_part >= 4:  # Reset animation sequence after 4 frames
            self.image_part = 0
            self.reset_animation = True

        self.index_image = int(self.step // 8) + self.image_part  # Update frame index

    def move(self) -> None:
        """
        Moves the entity based on its current direction and animation state.
        """
        if self.animation_walk:
            self.animation_steptime += self.screen.get_deltatime()  # Increment time counter
            if self.step < 16 and self.animation_steptime >= self.action_animation:
                self.step += self.speed  # Move the entity by speed pixels
                if self.direction == "left":
                    self.position.x -= self.speed
                elif self.direction == "right":
                    self.position.x += self.speed
                elif self.direction == "up":
                    self.position.y -= self.speed
                elif self.direction == "down":
                    self.position.y += self.speed
                self.animation_steptime = 0  # Reset animation timer
            elif self.step >= 16:
                self.step = 0
                self.animation_walk = False  # Stop walking animation
                if self.reset_animation:
                    self.reset_animation = False
                else:
                    self.image_part = 2 if self.image_part == 0 else 0  # Toggle footstep animation

    def align_hitbox(self) -> None:
        """
        Aligns the hitbox to the entity's position.
        Ensures the hitbox remains correctly positioned on a grid.
        """
        self.rect.center = self.position
        self.hitbox.midbottom = self.rect.midbottom
        while self.hitbox.x % 16 != 0:  # Align to a 16-pixel grid horizontally
            self.rect.x -= 1
            self.hitbox.midbottom = self.rect.midbottom
        while self.hitbox.y % 16 != 0:  # Align to a 16-pixel grid vertically
            self.rect.y -= 1
            self.hitbox.midbottom = self.rect.midbottom
        self.position = pygame.math.Vector2(self.rect.center)
        # print(self.hitbox)  # Debugging: Print hitbox position

    def get_all_images(self, spritesheet):
        """
        Extracts all animation frames from the sprite sheet and organizes them by direction.
        """
        all_images = {
            "down": [],
            "left": [],
            "right": [],
            "up": []
        }

        width: int = spritesheet.get_width() // 4  # Determine the width of each sprite
        height: int = spritesheet.get_height() // 4  # Determine the height of each sprite

        for i in range(4):  # Iterate over columns (frames)
            for j, key in enumerate(all_images.keys()):  # Iterate over rows (directions)
                all_images[key].append(Tool.split_image(spritesheet, i * width, j * height, 24, 32))  # Extract images

        return all_images
