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
né : <3
"""

cell_in_life = []
cell_edge =[[0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0]]
""" [[0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]]"""


space =    [[0,10,10,10,0],
            [0,10,10,10,0],
            [0,10,10,10,0],
            [0,0,0,0,10],
            [0,0,0,0,0]]


print("\ninitial")
for i in range(len(space)):
    print(space[i])
print("")


def scan_space():
    """Repere les celule vivante et les inscrits dans une liste"""
    for i in range(len(space)):
        for j in range(len(space[i])):
            if space[i][j] >= 10:
                #print(i,j)
                cell_in_life.append([i,j])
    #print(f"cell_in_life = {cell_in_life}")


def cell_edge_calcul():
    for item in cell_in_life:
        
        #Ca c'est pour que la celule vivante soit à 10 après les calculs
        cell_edge[item[0]][item[1]] += 9
        
        #print("item = ",item)
        i,j = item #On récupere les positions
        
        #on verifie la position des ranger pour de pas sortir de l'index
        #      ___     ___    ___     ___ Problème 1   ___     ___       ___     ___ 
        if i > 0:
            i_range = (i-1,i+2)
        elif i < len(cell_in_life): # < ou <= ??
            i_range = (i+1,i+2)
        else:
            i_range = (i-1,i+1)
        
        # on fait le calcul des valeurs voisine
        for it in range(i_range[0],i_range[1]):
            #print(f"i_range = {i_range} ,i = {i}, j = {j}")
            print(it,j)
            if j-1 != -1:
                cell_edge[it][j-1] += 1
            cell_edge[it][j] += 1
            try:
                cell_edge[it][j+1] += 1
            except:
                pass
        print(" \n ")
    
    print("\ncell_edge")
    for i in range(len(cell_edge)):
        print(cell_edge[i])
    print("")



def born_and_die():
    for i in range(len(cell_edge)):
        for j in range(len(cell_edge)):
            # Sur/sous population = mort (10 à 11 / +14)
            if  14 <= cell_edge[i][j] or 10 <= cell_edge[i][j] <= 11 :
                cell_edge[i][j] = 0
            
            # Voisinage = naissance (3 à 9)
            # voisinage correcte = Survie (12 et 13)
            elif 3 <= cell_edge[i][j] <= 9 or 12 <= cell_edge[i][j] <=13:
                cell_edge[i][j] = 10
            
            # Voisinage insufisant = 0 (1 et 2)
            elif cell_edge[i][j] <= 2 :
                cell_edge[i][j] = 0
    
    print("\nborn and die")
    for i in range(len(cell_edge)):
        print(cell_edge[i])
    print("")


if __name__ == "__main__":
    scan_space()
    cell_edge_calcul()
    born_and_die()

