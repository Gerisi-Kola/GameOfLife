import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


class GameOfLife:
    def __init__(self):
        
        # Créer la figure
        self.fig = plt.figure()
        self.ax = self.fig.add_axes([0.1, 0.1, 0.8, 0.8])
        
        # Taille de la grille
        n = 4
        self.grid_data = np.zeros((n, n))  # 0 pour blanc, 1 pour noir
        
        # Créer les carrés de la grille
        self.squares = []
        for i in range(n):
            for j in range(n):
                square = plt.Rectangle((i, j), 1, 1, facecolor='white', edgecolor='black')
                self.ax.add_patch(square)
                self.squares.append(square)
        
        # Configurer les axes
        self.ax.set_aspect('equal')
        self.ax.set_xlim(-0.1, n + 0.1)
        self.ax.set_ylim(-0.1, n + 0.1)
        
        
        # Créer l'animation
        anim = animation.FuncAnimation( self.fig,
                                        update,
                                        #frames=n*n*2,  # nombre total de frames
                                        #interval=500,  # intervalle en millisecondes
                                        #blit=True,     # ???????????????????????
                                        #repeat=True
                                        )
        
        plt.show()
    
    
    
    def update(frame):
            # Choisir aléatoirement un carré à changer
            square = self.squares[frame % len(self.squares)]
            # Alterner entre noir et blanc
            current_color = square.get_facecolor()
            new_color = 'black' if current_color[0] == 1 else 'white'
            square.set_facecolor(new_color)
            return self.squares


if __name__ == "__main__":
    g = GameOfLife()
    