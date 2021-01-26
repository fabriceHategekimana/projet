# L'hypercube
Cette topologie est utilisée dans la Connection Machine en particulier, mais est aussi une option importante pour les architectures MIMD. C’était sans doute le réseau le plus populaire dans les années 80.

Au sens mathématique, un hypercube désigne la généralisation d’un cube
dans des espaces de `dimension supérieure à 3`.
Dans notre contexte, ce terme suppose que les côtés sont de longueur 2.
Ainsi, dans un hypercube de `dimension k, on a exactement N = 2^k` processeurs, chacun de degré k (c’est-à-dire liés à k autres noeuds du réseau).

Construction d'un hypercube (`construction récursive à` partir de deux hypercubes k-1)
Un hypercube de dimension k est donc une grille de dimension k et d’arête
égale à 2.

Le diamètre = dimension car (k noeud pour relier les plus éloignés)

La largeur bisectionnelle vaut 2^k−1 = N/2, soit la taille d’un des deux sous-cube de dimension k − 1 utilisé pour la construction de l’hypercube de dimension k.

Le prix d’un réseau en hypercube est proportionnel à kN = N log 2 N car
k = log 2 N est le nombre de connexions par noeuds et N le nombre de noeuds.

l'hypercube n’est `pas véritablement scalable`. Le problème est qu’en
agrandissant un hypercube, on `augmente la connectivité` de chaque noeud, (processeurs avec peut de co)

`Solution`:
On peut éviter ce problème en plaçant en chaque noeud de l’hypercube une chaîne cyclique de k processeurs (cube connected cycles), plutôt qu’un processeur unique (utilisation d'anneaux pour processeurs 3 branches).

De cette manière, on garde la plupart des avantages de l’hypercube tout en assurant sa scalabilité. Dans ce qui suit, nous nous contenterons de discuter l’hypercube simple.

Avantage car avec une augmentation faible du nombre de connexions, on augmente de façon significative la taille du système. 
Deuxièmement, le nombre de chemins disponibles entre 2 noeuds augmente à mesure que l’hypercube s’agrandit, ce qui aide à une `congestion faible` du trafic des messages.

# Routage
Il existe une manière efficace de diriger un message à travers un réseau hypercubique.
Pour cela, on utilise tout d’abord une numérotation adéquate des noeuds. 
`Numérotation binaire` des nombres de 0 à 2 k − 1. 
Chaque noeud est représenté par `un nombre de k bits`. 
On choisit arbitrairement le noeud initial qui reçoit l’adresse 0. 
Ensuite, on applique l’algorithme suivant :
deux noeuds qui sont reliés le long de la dimension ℓ de l’hypercube ont
une adresse qui ne diffère que par le ℓ eme bit.

**obtention du chemin**
Le chemin que doit parcourir un message devant transiter entre deux noeuds
est obtenu par un `XOR (ou exclusif) des adresses respectives`.
Cette opération donne en effet un 1 dans chaque dimension à suivre pour atteindre la destination désirée.
