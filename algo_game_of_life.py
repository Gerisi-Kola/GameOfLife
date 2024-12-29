"""
attention : 
- un case entourer de celule vivante est égale à 8
- la valeur maximale est égale à 18

Je pense partir sur une grille avec des valeur
0 : vide / par defaut
+10 : vivant
+1 : pour chaque être vivant à coté

mort : >11 et <14
stase : 12 et 13
né : 3 !!!
"""


import numpy as np

class AlgoGameOfLife():
    def __init__(self, json_data, print_text=False):
        
        self.print_text = print_text
        
        self.grid_size = json_data["grid_size"]
        
        self.cell_status = np.zeros((self.grid_size, self.grid_size), dtype=int)
        if self.print_text:
            print(f"{self.cell_status}\n")
        
    
    
    def reload_life(self):
        """ça charge un état prédéfini"""
        self.cell_in_life = np.array([[2,2],[3,3],[4,1],[4,2],[4,3]])
        for i in self.cell_in_life:
            self.cell_status[i[0],i[1]] = 10
        
        if self.print_text:
            print(f"{self.cell_status}\n")
        
        return self.cell_status
    
    
    
    def scan_space(self):
        """Repère les cellules vivantes et les inscrits dans une liste"""
        if self.print_text:
            print(self.cell_in_life)
            print()
        
        x,y = np.where(self.cell_status == 10)
        
        if self.print_text:
            print(x,y)
            print()
        
        self.cell_in_life = np.append(self.cell_in_life, np.column_stack((x, y)),axis=0)
        
        if self.print_text:
            print(self.cell_in_life)
    
    
    def on_clic_set_game_of_life_algo(self,i,j):
        if self.cell_status[i,j]  == 0:
            self.cell_status[i,j] = 10
        else:
            self.cell_status[i,j] = 0
        
        if self.print_text:
            print(self.cell_status)
    
    
    def cell_status_calcul(self):
        """Calcul les voisinages"""
        if self.print_text:
            print(" ------ cell_status_calcul ---------")
            print(self.cell_status)
        
        x,y = np.where(self.cell_status == 10)
        array_len = self.cell_status.shape
        
        if self.print_text:
            print(array_len)
            print(np.column_stack((x, y)))
            
        for i,j in np.column_stack((x, y)):
            if i != 0 and j != 0:
                self.cell_status[i-1:i+2,j-1:j+2] += 1
                self.cell_status[i,j] -= 1
            else:
                print("error ! x or y = 0")
    
    
    def clear_cell(self):
        self.cell_status *= 0
    
    def born_and_die(self):
        if self.print_text:
            print(" ------ cell_status_calcul ---------")
            print(self.cell_status)
        """Procède aux naissances et aux morts"""
        
        x,y = np.where(   (self.cell_status == 3)
                        | (self.cell_status == 12)
                        | (self.cell_status == 13))
        
        #on met toutes les valeur à 0
        self.cell_status *= 0
        # on met à 10 toutes les cellules vivantes
        self.cell_status[x,y] = 10
    
    
    def generation_manager(self):
        self.cell_status_calcul() # calcul le voisinage
        self.born_and_die() # defini les celules vivantes et mortes
        
        if self.print_text:
            print(" ------ new gen ---------")
        
            print(self.cell_status)
        return self.cell_status


if __name__ == "__main__":
    from json_controler import get_constant_and_limit
    json_data = get_constant_and_limit()
    g = AlgoGameOfLife(json_data)
    for i in range(10):
        g.generation_manager()