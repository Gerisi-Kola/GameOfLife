import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class GridApp:
    def __init__(self, root):
        self.root = root
        root.title("Grille Paramétrable")
        
        # Taille initiale de la grille
        self.grid_size = 5
        
        # Créer la figure et le canevas
        self.fig, self.ax = self.create_grid()
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()
        
        # Créer les boutons
        self.create_buttons()
    
    def create_grid(self):
        """Créer une nouvelle grille"""
        fig, ax = plt.subplots()
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                rect = plt.Rectangle((j, i), 1, 1, fill=False, edgecolor='black')
                ax.add_patch(rect)
        
        ax.set_xlim(0, self.grid_size)
        ax.set_ylim(0, self.grid_size)
        ax.set_aspect('equal')
        ax.set_xticks([])
        ax.set_yticks([])
        return fig, ax
    
    def update_grid(self):
        """Mettre à jour la grille existante"""
        # Effacer la figure précédente
        self.ax.clear()
        
        # Recréer la grille avec la nouvelle taille
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                rect = plt.Rectangle((j, i), 1, 1, fill=False, edgecolor='black')
                self.ax.add_patch(rect)
        
        self.ax.set_xlim(0, self.grid_size)
        self.ax.set_ylim(0, self.grid_size)
        self.ax.set_aspect('equal')
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        
        # Redessiner la toile
        self.canvas.draw()
    
    def expand_grid(self):
        """Augmenter la taille de la grille"""
        self.grid_size += 1
        self.update_grid()
    
    def shrink_grid(self):
        """Réduire la taille de la grille"""
        if self.grid_size > 1:
            self.grid_size -= 1
            self.update_grid()
    
    def create_buttons(self):
        """Créer les boutons de contrôle"""
        # Bouton d'agrandissement
        expand_button = tk.Button(
            self.root, 
            text="Agrandir", 
            command=self.expand_grid
        )
        expand_button.pack()
        
        # Bouton de rétrécissement
        shrink_button = tk.Button(
            self.root, 
            text="Rétrécir", 
            command=self.shrink_grid
        )
        shrink_button.pack()
        
        """# Bouton de fermeture
        close_button = tk.Button(
            self.root, 
            text="Fermer", 
            command=self.root.quit
        )
        close_button.pack()"""

# Créer et lancer l'application
root = tk.Tk()
app = GridApp(root)
root.mainloop()