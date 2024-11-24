# Game Of Life

## Projet de fin de 6e (2024-2025)
20/11/2024 : Le prof nous a dit de choisir un truc a faire et j'ai choisi le jeu de la vie. Le prof connaissait pas, il a beaucoup aimée le principe


## Idées
- Pour que la grille **soit zoomable** on peut faire en sorte qu'entre chaque generation il y ai un controle si une verification de si on a appuiyer sur un bouton pour dezoomer.
    Si on a appuiyer on met les generation en pose le temps d'ajouter des cases au tableau.
- Pour que les **calcul reste correcte** on peut par exemple cree 5 case au debut et ajouter +5 a tout les position pour les garder inchanger.
- Pour **otimiser les calcul**, au lieu de parcourir une liste casi vide gigantesque. On pourrais garder en memoire toutes les positions des cellule vivante leurs voisines.

### Jounal
- ***20-11*** : Claude m'a pendu 4 GUI fait avec tkinter / kivy / Qt / pygame. Je vais d'abord me pencher sur l'algo.
- J'ai une fonction qui trouve les cellule vivantes et une qui calcule les voisines et met les points des positions en memoires
- ***21-11*** : La fonction qui calcul les voisinages crash si il y a une cellule à la dernière ligne. (Problème N1). J'ai changer le code pour être en POO. J'ai fait une méthode pour agrandir "l'aréne" mais il y a un problème (F1)
- 

### Problèmes
#### Not fix
1. La Méthode qui calcul les voisinages crash à du mal à gérer les cellules des bors, de tous les coté.

#### Fix
1. Aprés la 2 extention du territoire, il y a un bug et des cellules meur. à fixer


