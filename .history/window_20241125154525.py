import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Fonction pour créer la grille
def create_grid(grid_size):
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

# Création de la fenêtre Tkinter
root = tk.Tk()
root.title("Grille Paramétrable")

# Variables pour stocker la taille de la grille
grid_size = 5

# Figure Matplotlib initiale
fig, ax = create_grid(grid_size)

# Intégration de Matplotlib dans Tkinter
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack()

# Fonction pour mettre à jour la grille
def update_grid():
    # Effacer la figure précédente
    ax.clear()
    
    # Recréer la grille avec la nouvelle taille
    for i in range(grid_size):
        for j in range(grid_size):
            rect = plt.Rectangle((j, i), 1, 1, fill=False, edgecolor='black')
            ax.add_patch(rect)
    
    ax.set_xlim(0, grid_size)
    ax.set_ylim(0, grid_size)
    ax.set_aspect('equal')
    ax.set_xticks([])
    ax.set_yticks([])
    
    # Redessiner la toile
    canvas.draw()

# Boutons pour ajuster la taille
tk.Label(root, text="Taille de la grille :").pack()
"""tk.Scale(root, from_=1, to=20, orient=tk.HORIZONTAL, 
        variable=grid_size, command=lambda x: update_grid()).pack()"""
tk.Button()

# Bouton de fermeture
tk.Button(root, text="Fermer", command=root.quit).pack()

# Lancer l'interface
root.mainloop()
