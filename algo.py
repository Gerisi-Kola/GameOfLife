"""
attention : 
- un case entourer de celule vivante est egale a 8
- la valeur maximale est egale a 18



Je pense partir sur une grille avec des valeur
0 : vide / par defaut
+10 : vivant
+1 : pour chaque etre vivant à coté

mort : >11 et <14
stase : 12 et 13
né : 3 !!!
"""
#first_call = True
class AlgoGameOfLife():
    def __init__(self):
        self.cell_in_life = []
        self.cell_edge =[[0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0],
                        [0,0,10,10,0,0,0],
                        [0,10,0,0,10,0,0],
                        [0,10,0,0,10,0,0],
                        [0,0,10,10,0,0,0],
                        [0,0,0,0,0,0,0]]
        
        
        self.space =    [[0,0,0,0,0,0],
                        [0,0,0,0,0,0],
                        [0,0,10,0,0,0],
                        [0,0,0,0,0,0],
                        [0,0,0,0,0,0],
                        [0,0,0,0,0,0]]
        """[[10,10,10,0,10,10],
                    [0,10,10,0,10,0],
                    [0,10,10,0,10,0],
                    [0,0,0,0,0,10],
                    [10,0,0,0,10,10],
                    [0,0,0,0,0,0]]"""
        
        #self.cell_edge = self.space
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
        for i in range(len(self.cell_edge)):
            for j in range(len(self.cell_edge[i])):
                if self.cell_edge[i][j] >= 10:
                    #print(i,j)
                    self.cell_in_life.append([i,j])
        #print(f"scan = {self.cell_in_life}")
        #print(f"self.cell_in_life = {self.cell_in_life}")
    
    def cell_edge_calcul(self):
        for item in self.cell_in_life:
            
            
            #print("item = ",item)
            i,j = item #On récupere les positions
            
            #on verifie la position des ranger pour de pas sortir de l'index
            #      ___     ___    ___     ___ Problème 1   ___     ___       ___     ___ 
            """if i > 0:
                i_range = (i-1,i+2)
            elif i < len(self.cell_in_life): # < ou <= ??
                i_range = (i+1,i+2)
            else:
                i_range = (i-1,i+1)"""
            i_range = (i-1,i+2)
            
            # on fait le calcul des valeurs voisine
            for it in range(i_range[0],i_range[1]):
                #print(f"i_range = {i_range} ,i = {i}, j = {j}")
                #print(it,j)
                #if j-1 != -1:
                self.cell_edge[it][j-1] += 1
                
                if it != i:
                    self.cell_edge[it][j] += 1
                try:
                    self.cell_edge[it][j+1] += 1
                except:
                    #print("exhec")
                    pass
            
            #print(" \n ")
        
        self.cell_in_life = []
        
        print("\ncell_edge")
        for i in range(len(self.cell_edge)):
            print(self.cell_edge[i])
        print("")
    
    
    def born_and_die(self):
        for i in range(len(self.cell_edge)):
            for j in range(len(self.cell_edge)):
                # Sur/sous population = mort (10 à 11 / +14 / 4 à 9)
                if  14 <= self.cell_edge[i][j] or 10 <= self.cell_edge[i][j] <= 11 or 4 <= self.cell_edge[i][j] <= 9:
                    self.cell_edge[i][j] = 0
                
                # Voisinage = naissance (3)
                # voisinage correcte = Survie (12 et 13)
                elif 3 == self.cell_edge[i][j] or 12 <= self.cell_edge[i][j] <=13:
                    self.cell_edge[i][j] = 10
                
                # Voisinage insufisant = 0 (1 et 2)
                elif self.cell_edge[i][j] <= 2 :
                    self.cell_edge[i][j] = 0
                
                """elif 4 <= self.cell_edge[i][j] <= 9:
                    self.cell_edge[i][j] = 0"""
        
        print("\nborn and die")
        for i in range(len(self.cell_edge)):
            print(self.cell_edge[i])
        print("")



    def first_cell_borne(self):
        for item in self.cell_in_life:
            #Ca c'est pour que la celule vivante soit à 10 après les calculs
            self.cell_edge[item[0]][item[1]] += 9


if __name__ == "__main__":
    g = AlgoGameOfLife()
    g.scan_space()
    #g.first_cell_borne()
    g.cell_edge_calcul()
    g.born_and_die()
    
    g.scan_space()
    g.cell_edge_calcul()
    g.born_and_die()
    
    g.scan_space()
    g.cell_edge_calcul()
    g.born_and_die()
    
    g.scan_space()
    g.cell_edge_calcul()
    g.born_and_die()
    
    g.scan_space()
    g.cell_edge_calcul()
    g.born_and_die()
    
    g.scan_space()
    g.cell_edge_calcul()
    g.born_and_die()