"""Commentaire par Claude du code https://www.geeksforgeeks.org/conways-game-life-python-implementation/
"""

# Importation des bibliothèques nécessaires
import argparse  # Pour gérer les arguments en ligne de commande
import numpy as np  # Pour les calculs sur les tableaux
import matplotlib.pyplot as plt  # Pour l'affichage graphique
import matplotlib.animation as animation  # Pour l'animation

# Définition des constantes
ON = 255  # Cellule vivante (blanc)
OFF = 0   # Cellule morte (noir)
vals = [ON, OFF]

def randomGrid(N):
    """
    Crée une grille NxN avec des valeurs aléatoires
    20% de chance d'avoir une cellule vivante, 80% morte
    """
    return np.random.choice(vals, N*N, p=[0.2, 0.8]).reshape(N, N)

def addGlider(i, j, grid):
    """
    Ajoute un planeur (glider) à la position (i, j) dans la grille
    Le planeur est une structure qui se déplace en diagonale
    """
    glider = np.array([[0, 0, 255],
                    [255, 0, 255],
                    [0, 255, 255]])
    grid[i:i+3, j:j+3] = glider

def addGosperGliderGun(i, j, grid):
    """
    Ajoute un canon à planeurs de Gosper à la position (i, j)
    Cette structure produit périodiquement des planeurs
    """
    gun = np.zeros(11*38).reshape(11, 38)
    # Configuration du canon (1 = cellule vivante)
    # Les coordonnées sont définies pour créer la structure complexe du canon
    gun[5][1] = gun[5][2] = 255
    # ... (autres coordonnées)
    grid[i:i+11, j:j+38] = gun

def update(frameNum, img, grid, N):
    """
    Fonction de mise à jour de la grille pour l'animation
    Applique les règles du Jeu de la Vie de Conway
    """
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
            # Calcul de la somme des 8 voisins
            # Utilisation des conditions aux limites toroïdales (la grille s'enroule sur elle-même)
            total = int((grid[i, (j-1)%N] + grid[i, (j+1)%N] +
                        grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                        grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
                        grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N])/255)

            # Application des règles de Conway :
            # 1. Une cellule vivante avec moins de 2 ou plus de 3 voisins meurt
            # 2. Une cellule morte avec exactement 3 voisins devient vivante
            if grid[i, j] == ON:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = OFF
            else:
                if total == 3:
                    newGrid[i, j] = ON

    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,

def main():
    """
    Fonction principale qui initialise et lance la simulation
    """
    # Configuration du parser d'arguments
    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life simulation.")
    parser.add_argument('--grid-size', dest='N', required=False)
    parser.add_argument('--mov-file', dest='movfile', required=False)
    parser.add_argument('--interval', dest='interval', required=False)
    parser.add_argument('--glider', action='store_true', required=False)
    parser.add_argument('--gosper', action='store_true', required=False)
    args = parser.parse_args()

    # Configuration des paramètres
    N = 1000  # Taille par défaut de la grille
    if args.N and int(args.N) > 8:
        N = int(args.N)

    updateInterval = 50  # Intervalle de mise à jour par défaut
    if args.interval:
        updateInterval = int(args.interval)

    # Initialisation de la grille selon les arguments
    grid = np.array([])
    if args.glider:
        grid = np.zeros(N*N).reshape(N, N)
        addGlider(1, 1, grid)
    elif args.gosper:
        grid = np.zeros(N*N).reshape(N, N)
        addGosperGliderGun(10, 10, grid)
    else:
        pass
        #grid = randomGrid(N)

    # Configuration et lancement de l'animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N, ),
                                frames=10,
                                interval=updateInterval,
                                save_count=50)

    # Sauvegarde de l'animation si demandée
    if args.movfile:
        ani.save(args.movfile, fps=30, extra_args=['-vcodec', 'libx264'])

    plt.show()

# Point d'entrée du programme
if __name__ == '__main__':
    main()