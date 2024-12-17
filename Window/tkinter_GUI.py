import tkinter as tk

from matplot_Lib_GUI import GameOfLifePLT

class GameOfLifeTk:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x600")
        
        
        self.GLPLT = GameOfLifePLT()
        self.GLPLT.tkinter_integration(self.root)
        self.algo = None
        
        
        
        #    ------------    Button   ------------
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(side='bottom')
        
        # Créer et placer les boutons
        self.previous_button = tk.Button(self.button_frame, text="Previous", command=None)
        self.previous_button.pack(side="right")
        
        self.start_button = tk.Button(self.button_frame, text="Start", command=None)
        self.start_button.pack(side="left")
        
        self.save_button = tk.Button(self.button_frame, text="Save", command=None)
        self.save_button.pack(side="right")
        
        self.clear_button = tk.Button(self.button_frame, text="Clear", command=self.clear)#=lambda x=True: self.clear_screen(x))
        self.clear_button.pack(side="right")
        
        
        self.root.mainloop()
    
    
    
    def clear(self):
        """Reinitialise la grille et le ndarray"""
        self.GLPLT.reset_grid()



if __name__ == "__main__":
    g = GameOfLifeTk()