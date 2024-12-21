import tkinter as tk

from matplot_Lib_GUI import GameOfLifePLT
from music_gpt import Music

class GameOfLifeTk:
    def __init__(self,json_data):
        self.root = tk.Tk()
        self.root.geometry("600x600")
        
        #pygame.init()
        
        self.music = Music(json_data)
        self.music.launch_bg_music()
        
        self.GLPLT = GameOfLifePLT(json_data)
        self.GLPLT.tkinter_integration(self.root)
        self.algo = None
        
        
        
        #    ------------    Button   ------------
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(side='bottom')
        
        # Créer et placer les boutons
        self.previous_button = tk.Button(self.button_frame, text="Previous", command=None)
        self.previous_button.pack(side="right")
        
        self.start_button = tk.Button(self.button_frame, text="Start", command=self.start)
        self.start_button.pack(side="left")
        
        self.save_button = tk.Button(self.button_frame, text="Save", command=None)
        self.save_button.pack(side="right")
        
        self.clear_button = tk.Button(self.button_frame, text="Clear", command=self.clear)#=lambda x=True: self.clear_screen(x))
        self.clear_button.pack(side="right")
        
        
        self.root.mainloop()
    
    
    
    def clear(self):
        """Reinitialise la grille et le ndarray"""
        self.GLPLT.reset_grid()
        
        
    
    def start(self):
        import numpy as np
        n = np.zeros((10,10), int)
        #n[2:5,2:5] = 10
        #n[0,0] = 
        n[::2,::2] += 10
        #print(n)
        import time
        start1 = time.time()
        #self.GLPLT.update_grid_from_array(n)
        end1 = time.time()
        time.sleep(0.5)
        n +=10
        n[::2,::2] = 0
        start2 = time.time()
        self.GLPLT.update_grid_from_array2(n)
        end2 = time.time()
        
        print(start1-end1,"      ",start2-end2)



if __name__ == "__main__":
    from json_controler import get_constant_and_limit
    json_data = get_constant_and_limit()
    g = GameOfLifeTk(json_data)