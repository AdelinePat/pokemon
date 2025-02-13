
import pygame

class Sounds:
    def __init__(self):
        pygame.mixer.init()



        # Chargement de la musique de fond
        self.background_music = "./assets/sounds/Opening.mp3"  # Chemin vers votre fichier MP3

        # Initialisation des canaux
        self.music_channel = pygame.mixer.Channel(0)  # Canal dédié à la 


    def play_background_music(self, volume=0.1):
        pygame.mixer.music.load(self.background_music)
        pygame.mixer.music.set_volume(volume)  # Ajuste le volume (0.0 à 1.0)
        pygame.mixer.music.play(-1)  # Joue la musique en boucle

    def stop_background_music(self):
        pygame.mixer.music.stop()
