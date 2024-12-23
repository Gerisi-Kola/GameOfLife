import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation

from algo import AlgoGameOfLife

class WindowGameOfLife():
    def __init__(self, root, print_text=True):
        self.root = root
        self.root.title("Game of Life")
        
        self.print_text = print_text
        self.history = []
        self.actual_stage = []
        self.edgecolor = 'black'
        
        # Configuration initiale
        self.grid_size = 15
        self.fig = plt.figure(figsize=(6, 6))  # Crée une figure carrée de 6x6 pouces
        self.ax = self.fig.add_subplot(111) # Crée une zone de tracé unique (1x1 grid, position 1)
        
        # Dictionnaire pour suivre l'état des cases
        self.cell_states = {}
        
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(side='bottom')
        
        # Créer et placer les boutons
        self.previous_button = tk.Button(self.button_frame, text="Previous", command=self.previous_stage)
        self.previous_button.pack(side="right")
        
        self.algo = AlgoGameOfLife(self.grid_size, self.mise_a_jour_progression, self.print_text)
        
        self.start_button = tk.Button(self.button_frame, text="Start", command=self.start_animation)
        self.start_button.pack(side="left")
        
        self.save_button = tk.Button(self.button_frame, text="Save", command=self.save_stage)
        self.save_button.pack(side="right")
        
        self.clear_button = tk.Button(self.button_frame, text="Clear", command=lambda x=True: self.clear_screen(x))
        self.clear_button.pack(side="right")
        
        # Créer le canvas
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Connecter l'événement de clic
        self.canvas.mpl_connect('button_press_event', self.on_click)
        
        # Dessiner la grille initiale
        self.draw_grid()

        # Initialiser les éléments pour l'animation
        self.anim = None
        self.frames = 0
    
    def draw_grid(self):
        """Dessine la grille de cellules"""
        self.ax.clear()
        self.rectangles = []
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                rect = plt.Rectangle((j, i), 1, 1, fill=False, edgecolor=self.edgecolor)
                self.rectangles.append(rect)
                self.ax.add_patch(rect)
        
        self.ax.set_xlim(0, self.grid_size)
        self.ax.set_ylim(0, self.grid_size)
        self.ax.set_aspect('equal')
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.canvas.draw()

    def toggle_cell_screen(self, x, y):
        """Change l'état d'une cellule (vivante/morte) sur l'écran"""
        cell_id = (x, y)
        is_black = not self.cell_states.get(cell_id, False)
        self.cell_states[cell_id] = is_black
        color = 'black' if is_black else 'white'
        self.rectangles[x + y * self.grid_size].set_facecolor(color)
    
    def clear_screen(self, restart=False):
        """Efface l'écran et réinitialise les cellules vivantes"""
        for rect in self.rectangles:
            rect.set_facecolor('white')
        self.cell_states.clear()
        self.actual_stage = []
        self.canvas.draw()
        
        if restart:
            self.algo.cell_in_life = []

    def write_on_screen(self):
        """Affiche les cellules vivantes sur la grille"""
        for x, y in self.actual_stage:
            self.toggle_cell_screen(x, y)

    def on_click(self, event):
        """Récupère la position du clic et modifie l'état de la cellule"""
        if event.inaxes == self.ax:
            x = int(event.xdata)
            y = int(event.ydata)
            if 0 <= x < self.grid_size and 0 <= y < self.grid_size:
                self.toggle_cell_screen(x, y)
                self.toggle_cell_life(x, y)
    
    def _update_gui(self, new_cell, old_cell):
        """Met à jour l'affichage avec la nouvelle génération"""
        self.actual_stage = new_cell
        self.write_on_screen()

    def toggle_cell_life(self, x, y):
        """Modifie l'état de la cellule vivante/morte"""
        if [x, y] not in self.algo.cell_in_life:
            self.algo.cell_in_life.append([x, y])
        else:
            self.algo.cell_in_life.remove([x, y])
        self.actual_stage = self.algo.cell_in_life.copy()

    def mise_a_jour_progression(self, new_cell, old_cell=None):
        """Mise à jour de l'interface avec la nouvelle génération"""
        self.root.after(0, self._update_gui, new_cell, old_cell)
    
    def save_stage(self):
        """Sauvegarde l'état actuel de la grille"""
        print(self.actual_stage)
    
    def previous_stage(self):
        """Reviens en arrière sur l'historique"""
        try:
            self.clear_screen(restart=True)
            self.actual_stage = self.history.pop(-1)
            self.algo.cell_in_life = self.actual_stage.copy()
            self.write_on_screen()
        except IndexError:
            print("History empty")
    
    def start_animation(self):
        """Lance l'animation"""
        self.frames = 0
        self.anim = FuncAnimation(self.fig, self.update_frame, frames=self.get_frames(), interval=200, repeat=False)
        self.canvas.draw()

    def get_frames(self):
        """Génère les étapes du jeu de la vie"""
        while True:
            self.frames += 1
            new_cell = self.algo.generation_manager()
            yield new_cell  # Fonctionne avec FuncAnimation

    def update_frame(self, new_cell):
        """Met à jour une seule génération du jeu"""
        self.clear_screen()
        self.actual_stage = new_cell
        self.write_on_screen()
        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("650x650")
    app = WindowGameOfLife(root, False)
    root.mainloop()
