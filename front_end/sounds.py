import pygame

class Sounds:
    def __init__(self):
        # Initialize the Pygame mixer for sound handling
        pygame.mixer.init()

        # Load the music files (MP3 format)
        self.background_music = "./assets/sounds/Opening.mp3"  # Path to your MP3 file
        self.map_music = "./assets/sounds/map.mp3"  # Path to your map music file
        self.combat_music = "./assets/sounds/combat.mp3"  # Path to your combat music file

        # Initialize audio channels
        self.music_channel = pygame.mixer.Channel(0)  # Dedicated channel for music

    def play_background_music(self, volume=0.1):
        """Plays the opening background music with the specified volume."""
        pygame.mixer.music.load(self.background_music)  # Load the music file
        pygame.mixer.music.set_volume(volume)  # Adjust the volume (range: 0.0 to 1.0)
        pygame.mixer.music.play(-1)  # Play the music in a continuous loop

    def play_map_music(self, volume=0.1):
        """Plays the map background music with the specified volume."""
        pygame.mixer.music.load(self.map_music)  # Load the map music file
        pygame.mixer.music.set_volume(volume)  # Adjust the volume (range: 0.0 to 1.0)
        pygame.mixer.music.play(-1)  # Play the music in a continuous loop

    def play_combat_music(self, volume=0.1):
        """Plays the combat music with the specified volume."""
        pygame.mixer.music.load(self.combat_music)  # Load the combat music file
        pygame.mixer.music.set_volume(volume)  # Adjust the volume (range: 0.0 to 1.0)
        pygame.mixer.music.play(-1)  # Play the music in a continuous loop

    def stop_background_music(self):
        """Stops the background music."""
        pygame.mixer.music.stop()


