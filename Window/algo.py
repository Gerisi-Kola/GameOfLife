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
    def __init__(self, json_data, print_text=True):
        
        self.print_text = print_text
        
        self.grid_size = json_data["grid_size"]
        
        self.cell_edge = np.zeros((self.grid_size, self.grid_size), dtype=int)
        print(f"{self.cell_edge}\n")
        
        self.reload_life()
    
    
    def reload_life(self):
        self.cell_in_life = np.array([[2,2],[3,3],[4,1],[4,2],[4,3]])
            #self.old_stage = []
        for i in self.cell_in_life:
            self.cell_edge[i[0],i[1]] = 10
        
        print(f"{self.cell_edge}\n")
    
    
    
    def scan_space(self):
        """Repere les celule vivante et les inscrits dans une liste"""
        #self.cell_in_life = self.cell_in_life.reshape(0,0)
        
        print(self.cell_in_life)
        print()
        x,y = np.where(self.cell_edge == 10)
        
        print(x,y)
        print()
        
        self.cell_in_life = np.append(self.cell_in_life, np.column_stack((x, y)),axis=0)
        print(self.cell_in_life)
    
    
    def on_clic_set_game_of_life_algo(self,i,j):
        #print(i,j)
        #j,i = i,j
        if self.cell_edge[i,j]  == 0:
            self.cell_edge[i,j] = 10
        else:
            self.cell_edge[i,j] = 0
        print(self.cell_edge)
    
    
    def cell_edge_calcul(self):
        """Calcul les voisinages"""
        print(" ------ cell_edge_calcul ---------")
        print(self.cell_edge)
        x,y = np.where(self.cell_edge == 10)
        array_len = self.cell_edge.shape
        print(array_len)
        print(np.column_stack((x, y)))
        for i,j in np.column_stack((x, y)):
            #print(i,j)
            
            if i != 0 and j != 0:
                self.cell_edge[i-1:i+2,j-1:j+2] += 1
                self.cell_edge[i,j] -= 1
            else:
                print("error")
            #self.cell_edge[i,j] += 1
            
            #print(i-1,j-1)
            #print(i,j)
            #print(i+2,j+2)
            #print()
            
        
        #print(self.cell_edge)
    
    
    def clear_cell(self):
        self.cell_edge *= 0
    
    def born_and_die(self):
        print(" ------ cell_edge_calcul ---------")
        print(self.cell_edge)
        """Procéde aux naissances et aux morts"""
        
        x,y = np.where(   (self.cell_edge == 3)
                        | (self.cell_edge == 12)
                        | (self.cell_edge == 13))
        
        #on met toutes les valeur à 0
        self.cell_edge *= 0
        # on met à 10 toutes les cellules vivantes
        self.cell_edge[x,y] = 10
        
        #print(" born_and_die \n",self.cell_edge)
        #print(x,y)
    
    def generation_manager(self):
        #self.scan_space()
        #self.plus_plus()
        #print(self.cell_in_life)
        self.cell_edge_calcul() # calcul le voisinage
        self.born_and_die() # defini les celules vivantes et mortes
        #self.check_rim() # verifie si il y a des celules qui s'approche du bore
        
        if self.print_text:
            print(" ------ new gen ---------")
        
        print(self.cell_edge)
        return self.cell_edge
    
if __name__ == "__main__":
    from json_controler import get_constant_and_limit
    json_data = get_constant_and_limit()
    g = AlgoGameOfLife(json_data)
    #g.scan_space()
    """g.cell_edge_calcul()
    g.born_and_die()"""
    for i in range(10):
        g.generation_manager()
    #g.generation_manager(5)