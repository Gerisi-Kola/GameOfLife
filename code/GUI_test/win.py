import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from algo import AlgoGameOfLife


class WindowGameOfLife():
    def __init__(self, root):
        self.root = root
        self.root.title("Game of Life")
        
        
        self.grid_frame = tk.Frame(root)
        self.grid_frame.pack(fill=tk.BOTH, expand=True)
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(fill=tk.BOTH, expand=True)
        
        
        # Configuration initiale
        self.grid_size = 9
        self.fig = plt.figure(figsize=(6, 6))  # Crée une figure carrée de 6x6 pouces
        self.ax = self.fig.add_subplot(111) # Crée une zone de tracé unique (1x1 grid, position 1)
        
        # Dictionnaire pour suivre l'état des cases (True = noir, False = blanc)
        self.cell_states = {}
        
        # Créer le canvas
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.grid_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Connecter l'événement de clic
        self.canvas.mpl_connect('button_press_event', self.on_click)
        
        # Dessiner la grille initiale
        self.draw_grid()
        
        algo = AlgoGameOfLife(self.grid_size)
        
        start_button = tk.Button(self.button_frame, text = "Start", command=algo.generation_manager)
        start_button.pack()
        
    
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
        
        # Afficher les coordonnées dans la console
        print(f"Case cliquée: ({x}, {y})")

    def on_click(self, event):
        """Recupere la position du clic et daclanche une action"""
        if event.inaxes == self.ax:
            x = int(event.xdata)
            y = int(event.ydata)
            if 0 <= x < self.grid_size and 0 <= y < self.grid_size:
                self.toggle_cell(x, y)



if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x500")
    app = WindowGameOfLife(root)
    root.mainloop()