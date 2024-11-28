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
    def __init__(self,gride_size=9, callback=None, print_text=True):
        self.callback = callback
        
        self.print_text = print_text # ca permet de bloquer tous les <<print>> d'une traite
        
        self.gride_size = gride_size
        self.number_of_grid_expand = 0
        self.cell_in_life = []#[2,2],[2,3],[3,2],[3,3]]
        self.old_stage = []
        self.cell_edge = np.zeros((self.gride_size, self.gride_size), dtype=int) 
        self.plus_plus()
        
        if self.print_text:
            print("\norigin")
            for i in range(len(self.cell_edge)):
                print(self.cell_edge[i])
            print("")
        
    
    
    
    def scan_space(self):
        """Repere les celule vivante et les inscrits dans une liste"""
        self.cell_in_life = []
        for i in range(len(self.cell_edge)):
            for j in range(len(self.cell_edge[i])):
                if self.cell_edge[i][j] >= 10:
                    #print(i,j)
                    self.cell_in_life.aself.cell_edgeend([i,j])
    
    
    
    def cell_edge_calcul(self):
        """Calcul les voisinages"""
        for i,j in self.cell_in_life:
            
            # on fait le calcul des valeurs voisine
            if i > 0:
                for it in range(i-1,i+2):
                    self.cell_edge[it][j-1] += 1
                    if it != i:
                        self.cell_edge[it][j] += 1
                    try:
                        self.cell_edge[it][j+1] += 1
                    except:
                        print("exhec")
                        pass
        if self.print_text:
            print("\ncell_edge")
            for i in range(len(self.cell_edge)):
                print(self.cell_edge[i])
            print("")
    
    
    
    def born_and_die(self):
        """Procéde aux naissances et aux morts"""
        self.old_stage = self.cell_in_life.copy()
        self.cell_in_life = []
        for i in range(len(self.cell_edge)):
            for j in range(len(self.cell_edge)):
                # Sur/sous population = mort (1 à 2 / 4 à 11 / +14)
                if  self.cell_edge[i][j] <= 2 or\
                                4 <= self.cell_edge[i][j] <= 11 or\
                                14 <= self.cell_edge[i][j]:
                                #10 <= self.cell_edge[i][j] <= 11 or\
                    
                    self.cell_edge[i][j] = 0
                
                # Survie/naissance (3 /12 / 13)
                elif 3 == self.cell_edge[i][j] or 12 <= self.cell_edge[i][j] <=13:
                    self.cell_edge[i][j] = 10
                    self.cell_in_life.append([i,j])
        if self.print_text:
            print(self.cell_in_life)
            print("\nborn and die")
            for i in range(len(self.cell_edge)):
                print(self.cell_edge[i])
            print(f"{len(self.cell_edge)}x{len(self.cell_edge[0])}")
    
    
    
    def check_rim(self):
        """Verifiesi les cell s'aself.cell_edgeroche des bores de <<l'arene>>"""
        col_right = len(self.cell_edge) -2
        col_left = 1
        raw_top = 1
        raw_down = len(self.cell_edge) -2
        rim = False
        
        
        for i in range(0,len(self.cell_in_life)):
            for j in range(0,len(self.cell_in_life[0])):
                if self.cell_in_life[i][j] == raw_down or\
                            self.cell_in_life[i][j] == raw_top or\
                            self.cell_in_life[i][j] == col_left or\
                            self.cell_in_life[i][j] == col_right:
                    rim = True
        if rim:
            self.protection_from_rim()
            #self.cell_in_life_correction()
                    #pass
    
    
    
    def cell_in_life_correction(self):
        """Adapte les emplacement des celule dans cell_in_life pour que les madification de 
            <<l'arrene>> ne pose pas probleme"""
        
        # on copie la liste pour pouvoir la modifier dans la boucle
        cell_in_life_copy = self.cell_in_life.copy()
        for i in range(len(self.cell_in_life)):
                cell_in_life_copy[i][0] += 1
                cell_in_life_copy[i][1] += 1
        self.cell_in_life = cell_in_life_copy
    
    
    
    def protection_from_rim(self):
        """Ajoute une colone en haut et en bas 
            + Ajoute une ligne à gauche et à droite """
        
        self.gride_size += 1
        self.number_of_grid_expand += 1
        
        self.cell_edge = np.zeros((self.gride_size, self.gride_size), dtype=int) 
        self.cell_in_life_correction()
        self.plus_plus()
        
        if self.print_text:
            print("\nadd")
            for i in range(len(self.cell_edge)):
                print(self.cell_edge[i])
            print(f"{len(self.cell_edge)}x{len(self.cell_edge[0])}")
            print("")
    
    
    
    def plus_plus(self):
        for i in self.cell_in_life:
            self.cell_edge[i[0]][i[1]] = 10
    
    
    def list_adapte_to_grid(self):
        cell = self.cell_in_life.copy()
        for i in range(len(self.cell_in_life)):
            cell[i][0] += self.number_of_grid_expand
            #cell[i][1] += 2
        old_cell = self.old_stage.copy()
        for i in range(len(self.old_stage)):
            old_cell[i][0] += self.number_of_grid_expand
            #old_cell[i][1] += 2
        
        print(f"new cell = {self.cell_in_life} and adapt = {cell} \nold_cell = {self.old_stage} and adapt = {old_cell}")
    
    
    def generation_manager(self, num_of_gen=1):
        #self.scan_space()
        for _ in range(num_of_gen):
            self.plus_plus()
            #print(self.cell_in_life)
            self.cell_edge_calcul() # calcul le voisinage
            self.born_and_die() # defini les celules vivantes et mortes
            self.check_rim() # verifie si il y a des celules qui s'approche du bore
            #self.list_adapte_to_grid()
            try:
                self.callback(self.cell_in_life.copy(),self.old_stage.copy()) # ca renvoie la grille au fichier parent
            except:
                pass
            if self.print_text:
                print(" ------ new gen ---------")



if __name__ == "__main__":
    def none_fonction():
        print("a")
    g = AlgoGameOfLife(callback=none_fonction())
    g.generation_manager(5)