from music import Music
from json_controler import get_constant_and_limit
from tkinter_GUI import GameOfLifeTk


json_data = get_constant_and_limit()

music_is_found = False

try:
    music = Music(json_data)
    music.launch_bg_music()
    music_is_found = True
except:
    print("No music")

def clic_sound_caller():
    if music_is_found:
        music.touch_sound("grid")
        #print("aaaaaaaaa")

def button_sound():
    if music_is_found:
        music.touch_sound("button")
        #(print("ok")

game = GameOfLifeTk(json_data,clic_sound_caller,button_sound)