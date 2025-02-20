import pygame
from .keylistener import KeyListener
from .map import Map
from .player import Player

class Game:
    def __init__(self, screen, player_name, pokemon):
        """
        Initializes the game, setting up the main components such as the map, player, and key listener.
        """
        self.running = True  # Determines if the game loop should continue running
        self.screen = screen  # Reference to the game screen
        self.map: Map = Map(self.screen)  # Create the game map
        self.keylistener = KeyListener()  # Initialize the key listener to track player input
        self.player: Player = Player(self.keylistener, self.screen, 100, 300, player_name, pokemon)  # Create the player character
        self.map.add_player(self.player)  # Add the player to the map 
        self.pokemon = pokemon

    def run(self):
        """
        Main game loop that continuously updates and renders the game.
        """
        while self.running:
            self.handle_input()  # Process user input events
            self.map.update()  # Update the map (including objects, NPCs, etc.)
            self.screen.update()  # Refresh the game screen
            self.player.update()  # Update the player's position and state

    def handle_input(self):
        """
        Handles user input by listening for key presses and game quit events.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If the player closes the window, exit the game
                pygame.quit()
            elif event.type == pygame.KEYDOWN:  # When a key is pressed, add it to the key listener
                self.keylistener.add_key(event.key)
            elif event.type == pygame.KEYUP:  # When a key is released, remove it from the key listener
                self.keylistener.remove_key(event.key)
