import tkinter as tk

from matplot_Lib_GUI import GameOfLifePLT

class GameOfLifeTk:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x600")
        
        
        GLPLT = GameOfLifePLT()
        GLPLT.tkinter_integration(self.root)
        
        
        
        
        self.root.mainloop()
        
        



if __name__ == "__main__":
    g = GameOfLifeTk()