"""
L'interface est à l'envers, le point (0,0) est en bas à gauche alors que pour l'algo c'est en haut à gauche
"""
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
        
        # Configuration initiale
        self.grid_size = 15
        self.fig = plt.figure(figsize=(6, 6))  # Crée une figure carrée de 6x6 pouces
        self.ax = self.fig.add_subplot(111) # Crée une zone de tracé unique (1x1 grid, position 1)
        
        
        # Dictionnaire pour suivre l'état des cases
        self.cell_states = {}
        
        
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(side = 'bottom')
        
        """# Créer et placer le bouton AVANT le canvas
        self.previous_button = tk.Button(self.button_frame, text="Previous", command=self.previous_stage)
        self.previous_button.pack(side = "right")"""
        
        self.algo = AlgoGameOfLife(self.grid_size, self.print_text)
        """self.start_button = tk.Button(self.button_frame, text="Start", command=self.next_gen)
        self.start_button.pack(side = "left")
        
        self.save_button = tk.Button(self.button_frame, text="Save", command=self.save_stage)
        self.save_button.pack(side = "right")
        
        self.clear_button = tk.Button(self.button_frame, text="Clear", command=lambda x=True: self.clear_screen(x))
        self.clear_button.pack(side = "right")"""
        
        # Créer le canvas APRÈS le bouton
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Connecter l'événement de clic
        self.canvas.mpl_connect('button_press_event', self.on_click)
        
        # Dessiner la grille initiale
        self.draw_grid()
    
    
    
    def on_click(self, event):
        """Recupere la position du clic et daclanche une action"""
        if event.inaxes == self.ax:
            x = int(event.xdata)
            y = int(event.ydata)
            if 0 <= x < self.grid_size and 0 <= y < self.grid_size:
                print(f"Case cliquée: ({x}, {y})")
                #self.toggle_cell_screen(x, y)
                self.toggle_cell_life(x,y)
                print(self.algo.cell_in_life)
    
    
    def toggle_cell_life(self,x,y):
        """Modifie les cellules vivantes/mortes à chaque clic"""
        
        if [x,y] not in self.algo.cell_in_life:
            self.algo.cell_in_life.append([x,y])
        else:
            self.algo.cell_in_life.remove([x,y])
        
        self.actual_stage = self.algo.cell_in_life.copy()
        #print(self.algo.cell_in_life)
    
    
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
    
    
    
    
    def next_gen(self):
        anim = FuncAnimation(self.fig, self.mise_a_jour_progression,
                    init_func=self.init,
                    #frames=200, # ca sert a definir la temps avec la reibitialisation
                    interval=10,  # Intervalle en millisecondes
                    blit=True)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("650x650")
    app = WindowGameOfLife(root, True)
    root.mainloop()