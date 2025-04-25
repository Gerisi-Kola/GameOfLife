import tkinter as tk
from tkinter import ttk

class Menu_GameOfLife:
    def __init__(self,root):
        self.root = root
        
        self.win_rule = False
        
        self.barre_menu = tk.Menu(self.root)
        self.root.config(menu=self.barre_menu)
        menu_fichier = tk.Menu(self.barre_menu, tearoff=0)
        menu_fichier.add_command(label="Enregistrer l'état", command=None)
        menu_fichier.add_command(label="Charger une structure", command=None)
        self.barre_menu.add_cascade(label="File", menu=menu_fichier)
        
        menu_fichier = tk.Menu(self.barre_menu, tearoff=0)
        menu_fichier.add_command(label="Règles du jeu", command=self.rule_of_game)
        self.barre_menu.add_cascade(label="Help", menu=menu_fichier)
        
    
    def rule_of_game(self):
        if not self.win_rule:
            self.win_rule = None
            self.win_rule = tk.Toplevel(self.root)
            self.win_rule.geometry("400x400")
            self.win_rule.title("Rule of Game")
            
        else:
            self.win_rule.destroy()
            self.win_rule = False
    
    



if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x650")
    
    m = Menu_GameOfLife(root)
    m.root.mainloop()