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
    def __init__(self):
        
        self.a = 7
        
        self.cell_in_life = [[1,3],[2,2],[3,2],[3,3],[3,4]]  #[[3,2],[3,3],[3,4]]
        self.cell_edge = np.zeros((self.a, self.a), dtype=int) 
        self.plus_plus()
        """self.cell_edge=[[0,0,0,0,0,0],
                        [0,0,0,0,0,0],
                        [0,0,0,0,0,0],
                        [0,0,0,0,0,0],
                        [0,0,0,0,0,0],
                        [0,0,0,0,0,0]]"""
        """[[0,0,0,0,0,0,0],
                        [0,0,10,0,0,0,0],
                        [0,10,0,0,0,0,0],
                        [0,10,10,10,0,0,0],
                        [0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0]]"""
        """[[0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0],
                        [0,0,0,10,0,0,0],
                        [0,0,10,0,0,0,0],
                        [0,0,10,10,10,0,0],
                        [0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0]]
        """
        
        """self.space =   [[0,0,0,0,0,0],
                        [0,0,0,0,0,0],
                        [0,0,0,0,0,0],
                        [0,0,0,0,0,0],
                        [0,0,0,0,0,0],
                        [0,0,0,0,0,0]]"""
        
        print("\norigin")
        for i in range(len(self.cell_edge)):
            print(self.cell_edge[i])
        print("")
        
        """print("\ninitial")
        for i in range(len(self.space)):
            print(self.space[i])
        print("")"""
    
    
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
        for item in self.cell_in_life:
            i,j = item #On récupere les positions
            
            #on verifie la position des ranger pour de pas sortir de l'index
            #      ___     ___    ___     ___ Problème 1  ___     ___       ___     ___ 
            """if i > 1:
                i_range = (i-1,i+2)
            elif i < len(self.cell_in_life): # < ou <= ?? ------   Pk  self.cell_in_life ?????????????????????????????????????????????????????????????????????????
                i_range = (i+1,i+2)
            else:
                i_range = (i-1,i+1)"""
            #i_range = (i-1,i+2)
            
            # on fait le calcul des valeurs voisine
            if i > 0:
                for it in range(i-1,i+2):#i_range[0],i_range[1]):
                    #if j-1 != -1:
                    self.cell_edge[it][j-1] += 1
                    
                    if it != i:
                        self.cell_edge[it][j] += 1
                    try:
                        self.cell_edge[it][j+1] += 1
                    except:
                        print("exhec")
                        pass
        
        print("\ncell_edge")
        for i in range(len(self.cell_edge)):
            print(self.cell_edge[i])
        print("")
    
    
    def born_and_die(self):
        """Procéde aux naissances et aux morts"""
        
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
        
        """print(self.cell_in_life)
        print(len(self.cell_in_life))"""
        
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
                #cell_in_life_copy[i][0] += 1
                cell_in_life_copy[i][1] += 1
        self.cell_in_life = cell_in_life_copy
    
    
    """def vertical(self):
        len_list = [0 for i in range(len(self.cell_edge[0]))]
        self.cell_edge.insert(0,len_list)
        self.cell_edge.aself.cell_edgeend(len_list)
        
    def horizon(self):
        cell_edge_copy = self.cell_edge.copy()
        for i in range(len(cell_edge_copy)):
            self.cell_edge[i].insert(0,self.a)
            #self.cell_edge[i].aself.cell_edgeend(self.a)
            self.a += 1"""
    
    def protection_from_rim(self):
        """Ajoute une colone en haut et en bas 
            + Ajoute une ligne à gauche et à droite """
        
        #self.vertical()
        #self.horizon()
        
        self.a += 1
        
        self.cell_edge = np.zeros((self.a, self.a), dtype=int) 
        self.cell_in_life_correction()
        self.plus_plus()
        
        print("\nadd")
        for i in range(len(self.cell_edge)):
            print(self.cell_edge[i])
        print(f"{len(self.cell_edge)}x{len(self.cell_edge[0])}")
        print("")
        
        
        """len_i = len(self.cell_edge)
        
        # on copie la liste pour pouvoir la modifier dans la boucle
        
        
        
        
        
        
        len_list = [0 for i in range(len(self.cell_edge[0]))]
        print(f"len(self.cell_edge) = {len(self.cell_edge)} \nlen_list = {len(len_list)}")
        
        cell_edge_copy = self.cell_edge.copy()
        
        
        self.cell_edge.insert(0,len_list)
        self.cell_edge.aself.cell_edgeend(len_list)
        
        for i in range(len(cell_edge_copy)):
            self.cell_edge[i].insert(0,self.a)
            #self.cell_edge[i].aself.cell_edgeend(self.a)
            self.a += 1
        
        
        print(len(self.cell_edge),len(self.cell_edge[0]))"""
        
        """print("\nadd")
        for i in range(len(self.cell_edge)):
            print(self.cell_edge[i])
        print("")"""
    
    
    
    def plus_plus(self):
        for i in self.cell_in_life:
            self.cell_edge[i[0]][i[1]] = 10
    
    
    def generation_manager(self, num_of_gen=1):
        #self.scan_space()
        for _ in range(num_of_gen):
            
            #print(self.cell_in_life)
            self.cell_edge_calcul() # calcul le voisinage
            self.born_and_die() # defini les celules vivantes et mortes
            self.check_rim() # verifie si il y a des celules qui s'aself.cell_edgeroche du bore
            #print(" ------ new gen ---------")
            #self.protection_from_rim()
            """for i in range(len(self.cell_edge)):
                print(self.cell_edge[i])
            print("")"""
            
        


if __name__ == "__main__":
    g = AlgoGameOfLife()
    g.generation_manager(5)