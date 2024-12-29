import numpy as np

def load_save(grid, save):
    """"""
    if grid.shape[0] >= save.shape[0] and grid.shape[1] >= save.shape[1]:
        
        row_start = int(grid.shape[0]/2 - save.shape[0]/2)
        row_end   = int(grid.shape[0]/2 + save.shape[0]/2)
        col_start = int(grid.shape[1]/2 - save.shape[1]/2)
        col_end   = int(grid.shape[1]/2 + save.shape[1]/2)
        
        grid[row_start:row_end, col_start:col_end] = save
        
        print(save,"\n\n",grid)
        return grid
    
    else:
        print("Size error ! The grid is too small !")
        return


def save(grid):
    
    array = grid
    
    # Afficher l'array original
    print("Original Array:")
    print(array)
    
    # Trouver les indices où les valeurs sont différentes de 0 (zone centrale)
    non_zero_indices = np.where(array != 0)
    
    # Déterminer les indices minimaux et maximaux sur chaque axe
    min_row, max_row = np.min(non_zero_indices[0]), np.max(non_zero_indices[0])
    min_col, max_col = np.min(non_zero_indices[1]), np.max(non_zero_indices[1])
    
    # Redimensionner l'array pour inclure uniquement la zone centrale
    array_resized = array[min_row:max_row+1, min_col:max_col+1]
    
    # Afficher l'array redimensionné
    print("Redimensionné Array:")
    print(array_resized)





if __name__ == "__main__":
    a = np.zeros((10,10),int)
    b = np.zeros((4,4),int) + 1
    c = load_save(a,b)
    print()
    save(c)