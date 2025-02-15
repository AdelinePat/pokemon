import pygame
from codes.keylistener import KeyListener
from codes.map import Map
from codes.player import Player


class Game:
    def __init__(self, screen, player_name):
        self.running = True
        self.screen = screen
        self.map: Map = Map(self.screen)
        self.keylistener  = KeyListener()
        self.player: Player = Player(self.keylistener, self.screen, 100, 300, player_name)
        self.map.add_player(self.player)
        

    def run(self) :
        while self.running:
            self.handle_input()
            self.map.update()
            self.screen.update()
            self.player.update()

    def handle_input(self) :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                self.keylistener.add_key(event.key)
            elif event.type == pygame.KEYUP:
                self.keylistener.remove_key(event.key)
