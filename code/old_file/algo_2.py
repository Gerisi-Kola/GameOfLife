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
    def __init__(self, grid_size=9, print_text=True):
        
        self.print_text = print_text
        
        self.grid_size = grid_size
        self.cell_in_life = np.array([[2,2],[3,2],[3,3]])
        #self.old_stage = []
        self.cell_edge = np.zeros((self.grid_size, self.grid_size), dtype=int)
        print(f"{self.cell_edge}\n")
    
        """for i in self.cell_in_life:
            self.cell_edge[i[0],i[1]] = 10
        
        print(f"{self.cell_edge}\n")"""
    
    
    
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
        
        """self.cell_in_life = np.array([])
        for i in range(self.cell_edge.shape[0]):
            for j in range(self.cell_edge.shape[0]):
                if self.cell_edge[i][j] >= 10:
                    #print(i,j)
                    self.cell_in_life.aself.cell_edgeend([i,j])"""
    
    
    
    
    def cell_edge_calcul(self):
        """Calcul les voisinages"""
        for i,j in self.cell_in_life:
            #print(i,j)
            self.cell_edge[i-1:i+2,j-1:j+2] += 1
        
        #print(self.cell_edge)
    
    
    def born_and_die(self):
        """Procéde aux naissances et aux morts"""
        print(" born_and_die \n",self.cell_edge)
        
        x,y = np.where(   (self.cell_edge == 3)
                        | (self.cell_edge ==12)
                        | (self.cell_edge ==13))
        
        print(x,y)
    
    def generation_manager(self, num_of_gen=1):
        #self.scan_space()
        for _ in range(num_of_gen):
            self.plus_plus()
            #print(self.cell_in_life)
            self.cell_edge_calcul() # calcul le voisinage
            self.born_and_die() # defini les celules vivantes et mortes
            self.check_rim() # verifie si il y a des celules qui s'approche du bore
            #self.list_adapte_to_grid()
            """try:
                self.callback(self.cell_in_life.copy(),self.old_stage.copy()) # ca renvoie la grille au fichier parent
            except:
                pass"""
            if self.print_text:
                print(" ------ new gen ---------")
    
if __name__ == "__main__":
    g = AlgoGameOfLife()
    #g.scan_space()
    g.cell_edge_calcul()
    g.born_and_die()
    #g.generation_manager(5)