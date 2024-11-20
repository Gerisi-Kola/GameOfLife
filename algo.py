"""
Je pense partir sur une grille avec des valeur
0 : vide / par defaut
+10 : vivant
+1 : pour chaque etre vivant à coté

mort : >11 et <14
stase : 12 et 13
né : <3
"""

cell_in_life = []
cell_edge = [[0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]]
"""[[0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0]]"""

space =    [[0,0,0,0],
            [0,10,10,0],
            [0,0,10,0],
            [0,0,0,0]]
"""[[0,0,0],
            [0,10,0],
            [0,10,0]]"""

def scan_space():
    for i in range(len(space)):
        for j in range(len(space[i])):
            if space[i][j] >= 10:
                #print(i,j)
                cell_in_life.append([i,j])
    print(f"cell_in_life = {cell_in_life}")

def cell_edge_calcul():
    for item in cell_in_life:
        
        #Ca c'est pour que la celule vivante soit à 10 apres les calcul
        cell_edge[item[0]][item[1]] += 9
        
        print("item = ",item)
        i,j = item #On récupere les positions
        
        #on verifie la position des ranger pour de pas sortir de l'index
        if i > 0:
            i_range = (i-1,i+2)
        elif i <= len(cell_in_life):
            i_range = (i+1,i+2)
        else:
            i_range = (i-1,i+1)
        
        # on fait le calcul des valeurs voisine
        for it in range(i_range[0],i_range[1]):
            print(f"i_range = {i_range} ,i = {i}, j = {j}")
            cell_edge[it][j-1] += 1
            cell_edge[it][j] += 1
            try:
                cell_edge[it][j+1] += 1
            except:
                pass
    
    print(f"cell_edge = {cell_edge}")



#print(cell_in_life)

if __name__ == "__main__":
    scan_space()
    cell_edge_calcul()

