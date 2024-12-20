import pygame
import threading

class Music:
    def __init__(self):
        self.bg_music = None

    def launch_bg_music(self):
        """ Lance la musique de fond dans un thread séparé pour éviter les conflits avec Tkinter. """
        def play_music():
            pygame.mixer.init()  # Initialisation de Pygame
            self.bg_music = pygame.mixer.Sound("Music/dreams.ogg")
            self.bg_music.play(-1)  # La musique est en boucle (-1)

        # Lancer la musique dans un thread séparé
        music_thread = threading.Thread(target=play_music)
        music_thread.daemon = True  # Le thread se ferme automatiquement quand le programme principal se termine
        music_thread.start()

    def stop_bg_music(self):
        """ Arrête la musique de fond. """
        if self.bg_music:
            self.bg_music.stop()

    def touch_sound(self):
        """ Joue un son de touche. """
        def play_touch_sound():
            pygame.mixer.init()
            touch_sound = pygame.mixer.Sound("Music/iphone_son_de_touche.ogg")
            touch_sound.play()

        # Lancer le son dans un thread séparé
        touch_thread = threading.Thread(target=play_touch_sound)
        touch_thread.daemon = True
        touch_thread.start()

# Code principal pour tester la classe
if __name__ == "__main__":
    m = Music()
    m.launch_bg_music()  # Lance la musique de fond
    # m.stop_bg_music()  # Si tu veux arrêter la musique
    # m.touch_sound()  # Si tu veux jouer le son de touche
