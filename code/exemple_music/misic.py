import pygame

class Music:
    def __init__(self):
        pygame.mixer.init()
    
    def launch_bg_music(self):
        self.bg_music = pygame.mixer.Sound\
            ("Music/dreams.ogg")
    
    def stop_bg_music(self):
        self.bg_music.stop()
    
    def touch_sound(self):
        self.bg_music = pygame.mixer.Sound\
            ("Music/iphone_son_de_touche.ogg")
    
if __name__ == "__main__":
    m = Music()
    
    m.launch_bg_music()
    #m.stop_bg_music()
    #m.touch_sound()