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
        self.grid_size = 9
        self.fig = plt.figure(figsize=(6, 6))  # Crée une figure carrée de 6x6 pouces
        self.ax = self.fig.add_subplot(111) # Crée une zone de tracé unique (1x1 grid, position 1)
        
        # Dictionnaire pour suivre l'état des cases
        self.cell_states = {}
        
        
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(side = 'bottom')
        # Créer et placer le bouton AVANT le canvas
        self.algo = AlgoGameOfLife(self.grid_size, self.mise_a_jour_progression, self.print_text)
        self.start_button = tk.Button(self.button_frame, text="Start", command=self.algo.generation_manager)
        self.start_button.pack(side = "left")
        
        self.save_button = tk.Button(self.button_frame, text="Save", command=self.save_stage)
        self.save_button.pack(side = "right")
        
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
                rect = plt.Rectangle((j, i), 1, 1, fill=False, edgecolor='black')
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
    
    
    def toggle_cell(self, x, y):
        """Passe la case de <<vivante>> à <<morte>>"""
        # Coordonnées pour identifier la case
        cell_id = (x, y)
        
        # Inverse l'état de la case
        is_black = not self.cell_states.get(cell_id, False)
        self.cell_states[cell_id] = is_black
        
        # Dessiner le rectangle avec la nouvelle couleur
        color = 'black' if is_black else 'white'
        rect = plt.Rectangle((x, y), 1, 1, fill=True, facecolor=color, edgecolor='black')
        self.ax.add_patch(rect)
        self.canvas.draw()
        
        if self.print_text:
            # Afficher les coordonnées dans la console
            print(f"Case cliquée: ({x}, {y})")
    
    
    def on_click(self, event):
        """Recupere la position du clic et daclanche une action"""
        if event.inaxes == self.ax:
            x = int(event.xdata)
            y = int(event.ydata)
            if 0 <= x < self.grid_size and 0 <= y < self.grid_size:
                self.toggle_cell(x, y)
                self.algo.cell_in_life.append([x,y])
    
    def _update_gui(self,new_cell,old_cell):
        """Recupere l'ancienne et la nouvelle generation et met à jour l'interface
        """
        for i in old_cell:
            self.toggle_cell(i[0],i[1])
        for i in new_cell:
            self.toggle_cell(i[0],i[1])
        
        self.actual_stage = new_cell
        self.history.append(old_cell)
        if len(self.history) > 34:
            del self.history[-1]
        
        if self.print_text:
            print(f"\n{new_cell}\n")
            print(old_cell)
    
    
    def mise_a_jour_progression(self, progression, resultat_final=None):
        """Cette fonction sera appelée par ll'algo"""
        # On utilise after pour être thread-safe
        self.root.after(0, self._update_gui, progression, resultat_final)
    
    def save_stage(self):
        print(self.actual_stage)




if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("650x650")
    app = WindowGameOfLife(root, False)
    root.mainloop()