from playsound import playsound

class Music:
    def __init__(self):
        self.bg_music_path = "Music/dreams.mp3"
        self.touch_sound_path = "Music/iphone_son_de_touche.mp3"
    
    def launche_bg_music(self):
        playsound(self.bg_music_path)
    
    def touch_sound(self):
        playsound(self.touch_sound_path)

if __name__ == "__main__":
    m = Music()
    
    m.launche_bg_music()
    # m.touch_sound()