# Life

Le programme ci-dessous implémente une version multi-processus du jeu de la vie.
Dans ce jeu, les cellules d’un plateau à deux dimensions sont soit en vie soit morte. Le
status des cellules évolue au court du temps. Les régles qui détermine si une cellule
doit vivre ou mourir à l’étape suivante sont:

**1. Une cellule morte possédant exactement trois voisines vivantes devient vivante (elle naît).**  
**2. Une cellule vivante possédant deux ou trois voisines vivantes le reste, sinon elle meurt.**    

## 1. Combien de processus ce programme génère-t-il ? Décrire le rôle et les actions de chaque processus.
Ce programme génère 10x10=100 processus. Chaque processus est chargé de géré l'état d'une cellule (qu'elle soit vivante ou morte)

## 2. Dans le cas ou le processus principal (parent) meurt qu’arrive-t-il aux enfants de ce processus ?
Les processus fils deviennent orphelin et son ratachés au processus init (processus avec un pid= 1) qui devient leur nouveau parent.

## 3. Quelle est l’utilité de la fonction sched_yield (ligne 59) dans ce programme.
Cette fonction permet de soulager le CPU en laissant leur tour à d'autre threads. Cela permet aussi de réduire les différences de vitesse d'exécution entre les processus (chaque processus execute son code en tour par tour). (je ne suis pas totalement sûr de cette réponse).

## 4. Y-a-t-il des conflits dans les ressources utilisées par les différents processus ?  Expliquez.
Il y a pas vraiment de conflit de ressource. Chaque processus modifie sa propre cellule (mémoire addressé) et se contente de lire le contenu des autres cellules. Le processus parent ne fait que de lire le plateau (toutes les cellules en cours). Cependant, comme il n'y a pas de moyen de synchronisation, la lecture sur les cellules voisine ou la lecture du plateau peut être faussée (les threads n'ont pas tous la même vitesse et il se peut que les valeurs changent pendant une lecture).

## 5. Imaginons que ce programme tourne sur un processeur unique, que ce passerais- t-il si les lignes 85-87 n’étaient pas commentées.
Alors on aurrait un affichage lent et discontinue. Car on demande un ordonnancement des tâches en mode SCHED_FIFO (un processus, tournera dans le processeur sans interruption jusqu'à ce qu'il termine). De plus, on donne une faible priorité au processus parent (=1).

PS: Attention cette implémentation ne correspond pas sctrictement au jeux de la vie
