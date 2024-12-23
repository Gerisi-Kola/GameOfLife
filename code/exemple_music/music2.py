import pygame

class Music:
    def __init__(self,json_data):
        pygame.init()
        self.json = json_data["music"]
        self.bg = json_data["music"]["bg_music"]
        self.touch = json_data["music"]
        self.file = "Musique"
    
    
    
    def launche_bg_music(self):
        try:
            self.bg_music = pygame.mixer.Sound\
            (f"{self.file}/iphone_son_de_touche.ogg")
        except:
            pass
    
    def stop_bg_music(self):
        try:
            self.bg_music.stop()
        except:
            pass
    
    def touch_sound(self):
        try:
            self.bg_music = pygame.mixer.Sound\
            (f"{self.file}/{self.bg[0]['source']}")
        except:
            pass
    
if __name__ == "__main__":
    from json_controler import get_constant_and_limit

    json_data = get_constant_and_limit()
    json_data = {
    "BORN" : 3,
    "STASE_DOWN" : 12,
    "STASE_UP" : 13,
    
    "grid_size" : 10,
    "history_len" : 32,
    
    "music" : {
    "touch_music" : {
            "source" : "iphone_son_de_touche.ogg",
            "name" : "Son de Touche",
            "credit" : "¿¿¿"
            },
    "bg_music" : {
        "dreams" : {
            "source" : "dreams.ogg",
            "name" : "Dreams",
            "credit" : "??"
            },
        "calm-my-mind" : {
            "source" : "please-calm-my-mind.ogg",
            "name" : "Please Calm My Mind",
            "credit" : "Lesfm"
            }
        }
    }
}
    m = Music(json_data)
    
    m.launche_bg_music()
    m.stop_bg_music()
    m.touch_sound()