import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class GridApp:
    def __init__(self, master):
        self.master = master
        master.title("Grille Interactive")
        
        # Configuration initiale
        self.grid_size = 5
        self.fig = plt.figure(figsize=(6, 6))
        self.ax = self.fig.add_subplot(111)
        
        # Dictionnaire pour suivre l'état des cases (True = noir, False = blanc)
        self.cell_states = {}
        
        # Créer le canvas
        self.canvas = FigureCanvasTkAgg(self.fig, master=master)
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
                self.ax.add_patch(rect)
        
        self.ax.set_xlim(0, self.grid_size)
        self.ax.set_ylim(0, self.grid_size)
        self.ax.set_aspect('equal')
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.canvas.draw()

    def toggle_cell(self, x, y):
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
        if event.inaxes == self.ax:
            x = int(event.xdata)
            y = int(event.ydata)
            if 0 <= x < self.grid_size and 0 <= y < self.grid_size:
                self.toggle_cell(x, y)

# Créer et lancer l'application
root = tk.Tk()
root.geometry("500x500")
app = GridApp(root)
root.mainloop()