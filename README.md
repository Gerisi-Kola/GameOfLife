# Game Of Life

## Projet de fin de 6e (2024-2025)
20/11/2024 : Le prof nous a dit de choisir un truc a faire et j'ai choisi le jeu de la vie. Le prof connaissait pas, il a beaucoup aimée le principe


## Idées
- Pour que la grille **soit zoomable** on peut faire en sorte qu'entre chaque generation il y ai un controle si une verification de si on a appuiyer sur un bouton pour dezoomer.
    Si on a appuiyer on met les generation en pose le temps d'ajouter des cases au tableau.
- Pour que les **calcul reste correcte** on peut par exemple cree 5 case au debut et ajouter +5 a tout les position pour les garder inchanger.
- Pour **otimiser les calcul**, au lieu de parcourir une liste casi vide gigantesque. On pourrais garder en memoire toutes les positions des cellule vivante leurs voisines.
- Pour que l'utilisateur ne puisse **pas** mettre des **cellules aux bores**, on peut faire que la grille visuel (GUI) soit plus petites que la grille réel.

### Jounal
- ***20-11*** : Claude m'a pendu 4 GUI fait avec tkinter / kivy / Qt / pygame. Je vais d'abord me pencher sur **l'algo**.
- J'ai une fonction qui trouve les **cellule vivantes** et une qui calcule **les voisines** et met les points des **positions en memoires**

- ***21-11*** : La fonction qui calcul les voisinages crash si il y a une cellule à la dernière ligne. (Problème N1). J'ai changer le code pour être en POO. J'ai fait une méthode pour agrandir "l'aréne" mais il y a un problème (F1)

- ***24-11*** : J'ai créé une version json du fichier des constates et j'ai aussi créé un scripte pour les récupérer

- ***25-11*** : En classe : le prof m'a dit de tester un GUI avec matplotlib, ça marche et on peut l'intégré dans une fenétre tkinter. J'ai fait un grillage et 2 boutons (agrandir et retrecir la grille)

- ***26-11*** : J'ai fais quelques test sur les GUI matplotlib (J'ai oublié lque j'avais déjà un script pour window alors je l'ai refait)

- ***27-11*** : J'ai refait **l'agrandissement de la grille**, au lieu d'agrandir la liste j'en créé une nouvelle a chaque extention en utilisant **numpy**. Et j'ai **supprimer les GUI exemple** (kivy, pygame,...)


### Problèmes
#### Not fix
1. La Méthode qui calcul les voisinages crash à du mal à gérer les cellules des bors, de tous les coté.

#### Fix
1. Aprés la 2 extention du territoire, il y a un bug et des cellules meur. à fixer (27-11 : Le probleme est résolu. Au lieu d'agrandir la liste j'en créé une nouvelle a chaque extention en utilisant numpy)


