import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class MatplotTk():
    def __init__(self) -> None:
        
        # Création de la fenêtre Tkinter
        self.root = tk.Tk()
        self.root.title("Grille Paramétrable")
        
        # Variables pour stocker la taille de la grille
        self.grid_size = 5 #tk.IntVar(value=5)
        
        # Figure Matplotlib initiale
        self.fig, self.ax = self.create_grid(self.grid_size)
        
        # Intégration de Matplotlib dans Tkinter
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()
        
        
        
        # Boutons pour ajuster la taille
        tk.Label(self.root, text="Taille de la grille :").pack()
        """tk.Scale(root, from_=1, to=20, orient=tk.HORIZONTAL, 
                variable=grid_size, command=lambda x: update_grid()).pack()"""
        tk.Button(self.root, text = "++", command = self.grid_plus).pack()
        tk.Button(self.root, text = "--", command = self.grid_moins).pack()
        
        # Bouton de fermeture
        #tk.Button(self.root, text="Fermer", command=self.root.quit).pack()
        
        # Lancer l'interface
        self.root.mainloop()
    
    
    # Fonction pour créer la grille
    def create_grid(self, grid_size):
        fig, ax = plt.subplots()
        for i in range(grid_size):
            for j in range(grid_size):
                rect = plt.Rectangle((j, i), 1, 1, fill=False, edgecolor='black')
                ax.add_patch(rect)
        
        ax.set_xlim(0, grid_size)
        ax.set_ylim(0, grid_size)
        ax.set_aspect('equal')
        ax.set_xticks([])
        ax.set_yticks([])
        return fig, ax
    
    
    # Fonction pour mettre à jour la grille
    def update_grid(self):
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
    
    
    def grid_plus(self):
        self.grid_size += 2
        print(self.grid_size)
        self.update_grid()
    
    
    def grid_moins(self):
        if self.grid_size > 2:
            self.grid_size -= 2
        print(self.grid_size)
        self.update_grid()


if __name__ == "__main__":
    m = MatplotTk()
