import pygame

class Sounds:
    def __init__(self):
        # Initialize the Pygame mixer for sound handling
        pygame.mixer.init()

        # Load the music files (MP3 format)
        self.opening_music = "assets/sounds/Introduction.mp3"  # Path to your MP3 file
        self.background_music = "assets/sounds/Astoria.mp3"  # Path to your MP3 file
        self.map_music = "assets/sounds/Centre Pokémon.mp3"  # Path to your map music file
        self.combat_music = "assets/sounds/combat.mp3"  # Path to your combat music file
        self.maison_music = "assets/sounds/Harmonia.mp3"  # Path to your combat music file
        self.pokeshop_music = "assets/sounds/pokeshop.mp3"#Path to pokeshop file
        self.pokecenter_music = "assets/sounds/Route 1.mp3"
        self.labo_music = "assets/sounds/Route 2.mp3"

        # Initialize audio channels
        self.music_channel = pygame.mixer.Channel(0)  # Dedicated channel for music

    def play_opening_music(self, volume=0.1):
        """Plays the opening music with the specified volume."""
        pygame.mixer.music.load(self.opening_music)
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(-1)


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

    def play_maison_music(self, volume=0.1):
        """Plays the combat music with the specified volume."""
        pygame.mixer.music.load(self.maison_music)
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(-1)

    def play_pokeshop_music(self,volume =0.1):
        """Plays the combat music with the specified volume."""
        pygame.mixer.music.load(self.pokeshop_music)
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(-1)
    
    def play_pokecenter_music(self, volume=0.1):
        """Plays the opening music with the specified volume."""
        pygame.mixer.music.load(self.pokecenter_music)
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(-1)

    def play_labo_music(self, volume=0.1):
        """Plays the opening music with the specified volume."""
        pygame.mixer.music.load(self.labo_music)
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(-1)



    def stop_background_music(self):
        """Stops the background music."""
        pygame.mixer.music.stop()

    def stop_combat_music(self):
        """Stops the combat music."""
        pygame.mixer.music.stop()
    
    def stop_map_music(self):
        """Stops the map music."""
        pygame.mixer.music.stop()
    
    def stop_opening_music(self):
        """Stops the opening music."""
        pygame.mixer.music.stop()

    def stop_maison_music(self):
        """Stops the maison music."""
        pygame.mixer.music.stop()

    def stop_pokeshop_music(self):
        """Stops the pokeshop music"""
        pygame.mixer.music.stop()

    def stop_pokecenter_music(self):
        """Stops the pokeshop music"""
        pygame.mixer.music.stop()

    def stop_labo_music(self):
        """Stops the pokeshop music"""
        pygame.mixer.music.stop()


