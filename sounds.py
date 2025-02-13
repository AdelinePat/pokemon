import pygame

class Sounds:
    def __init__(self):
        # Initialize the Pygame mixer for sound handling
        pygame.mixer.init()

        # Load the background music file (MP3 format)
        self.background_music = "./assets/sounds/Opening.mp3"  # Path to your MP3 file

        # Initialize audio channels
        self.music_channel = pygame.mixer.Channel(0)  # Dedicated channel for music

    def play_background_music(self, volume=0.1):
        """Plays the background music with the specified volume."""
        pygame.mixer.music.load(self.background_music)  # Load the music file
        pygame.mixer.music.set_volume(volume)  # Adjust the volume (range: 0.0 to 1.0)
        pygame.mixer.music.play(-1)  # Play the music in a continuous loop

    def stop_background_music(self):
        """Stops the background music."""
        pygame.mixer.music.stop()
