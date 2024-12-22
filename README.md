# Game Of Life

## Projet de fin de 6e (2024-2025)
***20/11/2024*** : Le prof nous a dit de choisir un truc a faire et j'ai choisi le jeu de la vie. Le prof connaissait pas, il a beaucoup aimé le principe


## Idées
- Pour que la grille **soit zoomable** on peut faire en sorte qu'entre chaque generation il y ai un contrôle si une verification de si on a appuyer sur un bouton pour dézoomer.
    Si on a appuyer on met les generation en pose le temps d'ajouter des cases au tableau.

- Pour que les **calcul reste correcte** on peut par exemple crée 5 case au debut et ajouter +5 a tout les position pour les garder inchangé.

- Pour **optimiser les calcul**, au lieu de parcourir une liste quasi vide gigantesque. On pourrais garder en memoire toutes les positions des cellule vivante leurs voisines.

- Pour que l'utilisateur ne puisse **pas** mettre des **cellules aux bores**, on peut faire que la grille visuel (GUI) soit plus petites que la grille réel.

-  J'ai aussi pensé à faire un fichier pour les musiques et sons. Peut être en fonctionnel pour pouvoir utiliser les fonction sans avoir à crée un objet à chaque fois.

### Journal
- ***20-11*** : Claude m'a pendu 4 GUI fait avec Tkinter / Kivy / Qt / PyGame. Je vais d'abord me pencher sur **l'algo**.
- J'ai une fonction qui trouve les **cellule vivantes** et une qui calcule **les voisines** et met les points des **positions en mémoires**

- ***21-11*** : La fonction qui calcul les voisinages crash si il y a une cellule à la dernière ligne. (Problème N1). J'ai changer le code pour être en POO. J'ai fait une méthode pour agrandir "l’arène" mais il y a un problème (F1)

- ***24-11*** : J'ai créé une version json du fichier des constates et j'ai aussi créé un scripte pour les récupérer

- ***25-11*** : En classe : le prof m'a dit de tester un GUI avec Matplotlib, ça marche et on peut l'intégré dans une fenêtre Tkinter. J'ai fait un grillage et 2 boutons (agrandir et rétrécir la grille)

- ***26-11*** : J'ai fais quelques test sur les GUI Matplotlib (J'ai oublié lorsque j'avais déjà un script pour window alors je l'ai refait)

- ***27-11*** : J'ai refait **l'agrandissement de la grille**, au lieu d'agrandir la liste j'en créé une nouvelle a chaque extention en utilisant **numpy**. Et j'ai **supprimer les GUI exemple** (Kivy, PyGame,...)
- J'ai fait un fichier json pour sauvegarder les paternes.
- J'ai **connecter l’interface** et l'algo. Je peux choisir la configuration à partir du GUI !!!!
- J'ai 3 boutons qui gère la simulation :  Suivant ; Précédant ; Clear
- (L'interface est l'algo n'ont pas la même indexation : N2)(Bug sur la gauche de l’écran : F2)

- ***28-11*** : **Ça rame à mort !!!** Il faudrait utiliser ***numpy*** car il est +- 100 fois plus rapide car ***codé en C***. J'ai trouver un exemple du Jeu de la Vie (S1)

- ***16-12*** : J'ai crée une **nouvelle branche (Devlop).** J'essaye de refaire le code en utilisant numpy et en utilisant des animations Matplotlib. Peut être que je devrait plutôt utiliser PyGame ?

- ***17-12*** : J'ai séparé en 2 le script du GUI. D'un coté Matplotlib et de l'autre Tkinter. L'interface change au clic et le bouton "clear" nettoyé l'interface.

- ***19-12*** : J'ai fais un fichier Jupyter avec des test pour crée un script pour l'historique.

- ***20-12*** : J'ai créé un fichier "history" pour gérer l'historique des générations. 'history' utilise numpy. J'ai connecter tout les scripts au fichier json.
- J'ai créé un script pour gérer la musique. PyGame et Tkinter ne font pas bon mélange, donc GPT à modifier le code et a mis du multi-threading.

- ***21-12*** : GPT m'a pendu 2 méthode pour mettre à jour l'affichage de la grille, l'une est plus optimiser.
- J'ai imbriquer les scripts grace à **l'heritage** et j'ai connecter le clic sur la grille avec l'algo.

- ***22-22*** : Les cellules qui sont en x = 0 ou y = 0 meurs.

### Problèmes
#### Not fix
1. La Méthode qui calcul les voisinages crash à du mal à gérer les cellules des bores, de tous les coté.
2. L’indexation de l'interface sont inversé. Pour l'interface (0,0) et en bas à gauche alors que pour l'algo c'est en haut à gauche

#### Fix
1. Après la 2 extention du territoire, il y a un bug et des cellules meurs. à fixer (27-11 : Le problème est résolu. Au lieu d'agrandir la liste j'en créé une nouvelle a chaque extention en utilisant numpy)
2. Les cellules bug si elle sont trop proche de la gauche de l'écran.


### Source
1. https://www.geeksforgeeks.org/conways-game-life-python-implementation/