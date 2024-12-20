import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class GameOfLifePLT:
    def __init__(self,json_data):
        # Créer la figure
        self.fig = plt.figure()
        self.ax = self.fig.add_axes([0.1, 0.1, 0.8, 0.8])
        
        # Taille de la grille
        self.grid_size = json_data["grid_size"]
        self.grid_data = np.zeros((self.grid_size, self.grid_size))  # 0 pour blanc, 1 pour noir
        
        # Créer les carrés de la grille
        self.squares = {}  # Changé en dictionnaire pour accès facile
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                square = plt.Rectangle((i, j), 1, 1, facecolor='white', edgecolor='black')
                self.ax.add_patch(square)
                self.squares[(i,j)] = square
        
        # Configurer les axes
        self.ax.set_aspect('equal')
        self.ax.set_xlim(-0.1, self.grid_size + 0.1)
        self.ax.set_ylim(-0.1, self.grid_size + 0.1)
        
        # Connecter l'événement de clic
        self.fig.canvas.mpl_connect('button_press_event', self.on_click)
    
    
    def on_click(self, event):
        if event.inaxes == self.ax:
            # Convertir les coordonnées du clic en indices de grille
            i = int(event.xdata)
            j = int(event.ydata)
            
            # Vérifier si le clic est dans la grille
            if 0 <= i < self.grid_size and 0 <= j < self.grid_size:
                square = self.squares[(i,j)]
                current_color = square.get_facecolor()
                new_color = 'black' if current_color[0] == 1 else 'white'
                square.set_facecolor(new_color)
                self.fig.canvas.draw_idle()  # Rafraîchir l'affichage
    
    
    def reset_grid(self):
        # Parcourir toutes les cases et les réinitialiser à la couleur blanche
        for square in self.squares.values():
            square.set_facecolor('white')
        
        # Rafraîchir l'affichage pour appliquer les changements
        self.fig.canvas.draw_idle()
    
    
    def tkinter_integration(self, root):
        canvas = FigureCanvasTkAgg(self.fig, master=root)
        canvas.get_tk_widget().pack(fill='both', expand=True)
        canvas.draw()
        
        return self.fig

if __name__ == "__main__":
    from json_controler import get_constant_and_limit
    json_data = get_constant_and_limit()
    g = GameOfLifePLT(json_data)
    plt.show()