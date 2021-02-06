# Qu’est-ce qu’un PSC ?
Un psc (problème de satisfaction de contraintes).
C'est un problème qui est composé par un nombre de contrainte établi.
Comparé au problèmes de recherche, on a pas d'état final explicitement définit (défini seulement par des règles)

# Quel est son modèle ?
Le psc est composée de:
- Un ensemble de variable X=(x1,...,xn) chaque xi ayant un domaine de valeurs admissible Di
- Un ensemble de contrainte sur les variables: C=(c1,...,cm)

# Comment le résout-on ?
On doit trouver un état X tel que toutes ses paramètres remplissent leur dommaine de définition et que toutes les contraintes son respectées

# En quoi consiste le graphe mis en jeu ?
On crée un graphe des contraintes
G=(V,E)=("variables","contraintes")
Permet de suivre la propagation des contraintes

# Décrivez les algorithmes et heuristiques associées.
On a comme par exemple l'algorithme de Backtracking (utilisant un forward checking seulement?)
Comme la sélection des variables est toujours "aléatoire" on peut y appliquer des heuristiques:
	- variable la plus contrainte
	- valeur la moins contraignante
Si les contrainte sont binaires, on peut aussi utilié l'algorithme AC3 (arc consistency). 
