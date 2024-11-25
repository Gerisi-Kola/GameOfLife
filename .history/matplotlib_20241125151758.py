import matplotlib.pyplot as plt
import numpy as np

# Créer une figure et un axe
fig, ax = plt.subplots()

# Paramètres de la grille
grid_size = 5  # Nombre de carrés par ligne et colonne
square_size = 1  # Taille de chaque carré

# Générer la grille de carrés
for i in range(grid_size):
    for j in range(grid_size):
        # Dessiner un carré à chaque position
        rect = plt.Rectangle((j, i), square_size, square_size, 
                             fill=False, edgecolor='black')
        ax.add_patch(rect)

# Configurer les limites des axes
ax.set_xlim(0, grid_size)
ax.set_ylim(0, grid_size)

# Rendre les axes égaux
ax.set_aspect('equal')

# Masquer les graduations
ax.set_xticks([])
ax.set_yticks([])

# Afficher la grille
plt.show()import matplotlib.pyplot as plt
import numpy as np

# Créer une figure et un axe
fig, ax = plt.subplots()

# Paramètres de la grille
grid_size = 5  # Nombre de carrés par ligne et colonne
square_size = 1  # Taille de chaque carré

# Générer la grille de carrés
for i in range(grid_size):
    for j in range(grid_size):
        # Dessiner un carré à chaque position
        rect = plt.Rectangle((j, i), square_size, square_size, 
                             fill=False, edgecolor='black')
        ax.add_patch(rect)

# Configurer les limites des axes
ax.set_xlim(0, grid_size)
ax.set_ylim(0, grid_size)

# Rendre les axes égaux
ax.set_aspect('equal')

# Masquer les graduations
ax.set_xticks([])
ax.set_yticks([])

# Afficher la grille
plt.show()