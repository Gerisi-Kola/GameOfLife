"""
L'interface est à l'envers, le point (0,0) est en bas à gauche alors que pour l'algo c'est en haut à gauche
"""
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from algo import AlgoGameOfLife

class WindowGameOfLife():
    def __init__(self, root, print_text=True):
        self.root = root
        self.root.title("Game of Life")
        
        self.print_text = print_text
        self.history = []
        self.actual_stage = []
        
        # Configuration initiale
        self.grid_size = 15
        self.fig = plt.figure(figsize=(6, 6))  # Crée une figure carrée de 6x6 pouces
        self.ax = self.fig.add_subplot(111) # Crée une zone de tracé unique (1x1 grid, position 1)
        
        # Dictionnaire pour suivre l'état des cases
        self.cell_states = {}
        
        
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(side = 'bottom')
        # Créer et placer le bouton AVANT le canvas
        self.previous_button = tk.Button(self.button_frame, text="Previous", command=self.previous_stage)
        self.previous_button.pack(side = "right")
        
        self.algo = AlgoGameOfLife(self.grid_size, self.mise_a_jour_progression, self.print_text)
        self.start_button = tk.Button(self.button_frame, text="Start", command=self.next_gen)
        self.start_button.pack(side = "left")
        
        self.save_button = tk.Button(self.button_frame, text="Save", command=self.save_stage)
        self.save_button.pack(side = "right")
        
        self.clear_button = tk.Button(self.button_frame, text="Clear", command=lambda x=True: self.clear_screen(x))
        self.clear_button.pack(side = "right")
        
        # Créer le canvas APRÈS le bouton
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Connecter l'événement de clic
        self.canvas.mpl_connect('button_press_event', self.on_click)
        
        # Dessiner la grille initiale
        self.draw_grid()
    
    
    def draw_grid(self):
        self.ax.clear()
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                rect = plt.Rectangle((j, i), 1, 1, fill=False, edgecolor='red')
                # (j, i) : position du coin inférieur gauche du rectangle
                # 1, 1   : largeur et hauteur du rectangle
                # fill=False : rectangle non rempli
                # edgecolor='black' : bordure noire
                
                self.ax.add_patch(rect)  # Ajoute le rectangle à la zone de tracé
        
        self.ax.set_xlim(0, self.grid_size)  # Définit les limites de l'axe X
        self.ax.set_ylim(0, self.grid_size)  # Définit les limites de l'axe Y
        self.ax.set_aspect('equal')          # Force un ratio 1:1 pour avoir des carrés parfaits
        self.ax.set_xticks([])               # Supprime les graduations sur l'axe X
        self.ax.set_yticks([])               # Supprime les graduations sur l'axe Y
        self.canvas.draw()                   # Rafraîchit l'affichage pour montrer les modifications
    
    
    def toggle_cell_screen(self, x, y):
        """Passe la case de <<vivante>> à <<morte>>"""
        # Coordonnées pour identifier la case
        cell_id = (x, y)
        
        # Inverse l'état de la case
        is_black = not self.cell_states.get(cell_id, False)
        self.cell_states[cell_id] = is_black
        
        # Dessiner le rectangle avec la nouvelle couleur
        color = 'black' if is_black else 'white'
        if color == 'white':
            edgecolor = 'white'
        rect = plt.Rectangle((x, y), 1, 1, fill=True, facecolor=color, edgecolor='black')
        self.ax.add_patch(rect)
        self.canvas.draw()
    
    
    def clear_screen(self, restart=False):
        if self.print_text:
            print(f"clear {self.actual_stage}")
        for i in self.actual_stage:
            self.toggle_cell_screen(i[0],i[1])
        
        self.actual_stage = []
        
        if restart:
            self.algo.cell_in_life = []
    
    
    def write_on_screen(self):
        """On affiche les cellules vivante"""
        for i in self.actual_stage:
            self.toggle_cell_screen(i[0],i[1])
    
    
    
    
    def on_click(self, event):
        """Recupere la position du clic et daclanche une action"""
        if event.inaxes == self.ax:
            x = int(event.xdata)
            y = int(event.ydata)
            if 0 <= x < self.grid_size and 0 <= y < self.grid_size:
                if self.print_text:
                    # Afficher les coordonnées dans la console
                    print(f"Case cliquée: ({x}, {y})")
                self.toggle_cell_screen(x, y)
                self.toggle_cell_life(x,y)
    
    
    def _update_gui(self,new_cell,old_cell):
        """Recupere l'ancienne et la nouvelle generation et met à jour l'interface
        """
        
        #on supprime les ancienne celulles
        self.clear_screen()
        
        self.actual_stage = new_cell
        
        self.write_on_screen()
        
        try:
            if old_cell != new_cell:
                self.history.append(old_cell.copy())
        except:
            self.history.append(old_cell.copy())
        if len(self.history) > 64:
            print("History full")
            print(self.history)
            del self.history[0]
        
        if self.print_text:
            print(f"\n{new_cell}\n")
            print(old_cell)
    
    
    def toggle_cell_life(self,x,y):
        """Modifie les cellules vivantes/mortes à chaque clic"""
        
        if [x,y] not in self.algo.cell_in_life:
            self.algo.cell_in_life.append([x,y])
        else:
            self.algo.cell_in_life.remove([x,y])
        
        self.actual_stage = self.algo.cell_in_life.copy()
        #print(self.algo.cell_in_life)
    
    
    def mise_a_jour_progression(self, new_cell, old_cell=None):
        """Cette fonction sera appelée par ll'algo"""
        # On utilise after pour être thread-safe
        self.root.after(0, self._update_gui, new_cell, old_cell)
    
    
    def save_stage(self):
        print(self.actual_stage)
    
    
    def previous_stage(self):
        """Reviens en arrière sur l'historique"""
        #print("")
        #print(self.history)
        #(f" 0 = {self.history[0]}  /  -1 = {self.history[-1]}")
        #if self.history != [] and self.history != [[]]:
        try:
            self.clear_screen(restart = True)
            self.actual_stage = self.history.pop(-1)
            print(self.actual_stage)
            self.algo.cell_in_life = self.actual_stage.copy()
            self.write_on_screen()
        except IndexError:
            print("History empty")
        #else:
        #    print(self.history)
    
    def next_gen(self):
        for i in range (1):
            self.root.after(0,self.algo.generation_manager())
            #print(i)
        #print("finidh")



if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("650x650")
    app = WindowGameOfLife(root, False)
    root.mainloop()
