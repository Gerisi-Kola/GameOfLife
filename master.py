from music import Music
from json_controler import get_constant_and_limit
from tkinter_GUI import GameOfLifeTk


json_data = get_constant_and_limit()
g = GameOfLifeTk(json_data)


music = Music(json_data)
music.launch_bg_music()