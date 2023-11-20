**Quel était votre projet initial ?**

Notre but était de développer une simulation de jeu de bataille en Python avec recommandation de s’inspirer de le la page 132 du manuel (*cf. Numérique et sciences informatiques : 24 leçons avec exercices corrigés - Terminale*).
Par ailleurs, le minimum de cartes demandé était de 8 (une seule couleur, afin d'éviter les cas d’égalités).


**Le programme fonctionne-t-il ? L’avez-vous éventuellement enrichi ?**

Le programme est bel et bien fonctionnel, nous avons programmé une simulation de jeu de bataille en utilisant des listes, des dictionnaires et de la programmation objet et notamment la notion des piles/files étudiée dans le chapitre 7 (notion importante dans le programme).

Par ailleurs, nous avons enrichi le programme par l’ajout de toutes les couleurs (24 cartes supplémentaires, 32 au total) avec un système d’égalité dû au fait qu’il existe 4 fois les 8 mêmes valeurs mais avec des couleurs différentes.
En ce qui concerne l'esthétique de notre programme, nous nous sommes permis d’ajouter la fonction `sleep` afin de rendre la lecture des informations renvoyées par le programme plus facile mais aussi, le retour chariot qui permet une meilleure lisibilité du programme.
Enfin, l’ajout de `colored` qui permet d’afficher des textes colorés afin de mieux différencier les deux joueurs qui s’affrontent.


**Quelles difficultés avez-vous rencontré ?**

Nous avons rencontré trois problèmes majeurs. Le premier était lorsqu’une égalité était en jeu, le programme n’arrivait à différencier les couleurs et faisait toujours gagner le premier joueur qui a défilé la carte. Il avait aussi un problème avec les couleurs, le programme donnait une valeur à celle-ci ce qui pouvait donner lieu à ce genre de situation (ex: `9♦ vs 2♣ = 2♣ WIN`). Ces deux problèmes ont pu être réglés avec la création d’un dictionnaire pour ensuite définir une valeur à chaque carte afin que le programme ne leur en attribue pas une en fonction de leurs positions dans la liste. Le dernier problème était lorsqu’un joueur n'avait plus de cartes au moment d’une égalité, il a été réglé avec l'ajout d'une vérification pour savoir si le paquet est vide.
