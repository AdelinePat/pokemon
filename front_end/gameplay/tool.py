import pygame

"""
recupere les images du sprit
"""
class Tool:
    @staticmethod  # pas besoin de specifier le self
    def split_image(spritsheet: pygame.Surface, x: int, y:int, width: int, height: int):
        return spritsheet.subsurface(pygame.Rect(x, y,width, height))

