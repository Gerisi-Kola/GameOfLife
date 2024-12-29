import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Window:
    def __init__(self):
        self.grid_size = 5
        self.grid = np.zeros((self.grid_size, self.grid_size), dtype=int)
        self.grid[:3,:3] = 1
        
        fig,ax = plt.subplots(figsize=(8,8))
        
        print(self.grid,"\n")
        self.grid.fill(0)
        print(self.grid)
        
        
        plt.show()





if __name__ == "__main__":
    w = Window()
    