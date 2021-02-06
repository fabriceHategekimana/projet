# Rappelez le principe des méthodes de recherche. 
- problématique
- réunir définitions/concepts/principes
- Solution formelle
- mise en oeuvre (exemples)

# Qu’est que la profondeur limitée et en quoi est-ce utile ?
La profondeur limité est une borne qu'on met à la profondeur de recherche d'un graphe. Cela peut être utile lorsque la taille du graphe est infini ou juste très grande. Cela permet comme par exemple d'optimaliser la recherche en profondeur en la transformant en (IDS).

# Comment est définie une heuristique et quelles sont ses propriétés ?
Définition:
Une heuristique est une fonction h d'estimation de côut telle que 
h:V->R+ avec h(v)=0 si state(v)=Sg

# A quoi sert une heuristique ?
 Une heuristique est une sorte de classement des choix possible basée sur une connaissance a priori (B), pour converger plus rapidement vers la solution.
 
# Expliquez en particulier l’algorithme A* et ses propriétés. Citez des exemples d’application.
C’est l’algorithme Best First Search avec la
fonction d’évaluation:
f(v) = g(v) + h(v)
ou h est une heuristique admissible et
consistante, et
c(s,s’) >= e >0
pour tout s et s’
Sous ces conditions:
l’algorithme A * est complet et optimal
Stephane.Marchand-Maillet – Université de Genève
Intelligence Artificielle
AI Heuristiques

Trouver des exemple d'application
