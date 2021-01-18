# En quoi consiste la recherche adverse et en quoi diffère-t-elle de la recherche classique ?
La recherche adverse part du principe qu'il y a maintenant un adversaire qui joue contre nous (en tour par tour souvent).
De ce fait notre système ne peut pas être vu comme un graphe simple (car les possibilités augmentent).

# Quel est son modèle ?
On part du principe que l'adversaire a une stratégie de jeu.
Son modèle est très similaire aux algorithmes de recherche habituel.

- état initial
- état final
- fonction de transition (fonction d'utilité)
- espace des états 

La fonction d'utilité va chercher à maximiser les points qu'on gagne en jouant un coup à un moment donné.

 # Qu’est-ce qu’une fonction d’évaluation ?
 La fonction d'évaluation est une heuristique qui va nous permettre de choisir le meilleur coup à jouer.
 Dans notre cas, on cherche à maximiser f alors que l'adversaire cherche à miniser f.
 
 # Décrivez l’algorithme MINIMAX et ses variantes.
 On ne remonte pas simplement les valeurs le long
du chemin, on doit prendre en compte le fait que
l’on joue contre un adversaire:
• MAX cherche à maximiser la fonction d’évaluation
-Il fera le choix du coup menant au maximum des
valeurs
• MIN cherche à minimiser la fonction d’évaluation
-Il fera le choix du coup menant au minimum des
valeurs
-On rétro-propage selon cette logique

On a aussi l'algorithme d'elagage alpha-beta
Principe: ne plus développer les branches de l’arbre
correspondant aux coups sans intérêt (au sens MiniMax)
- Algorithme exact: trouve la même solution
On affecte:
• Une valeur a aux nœuds MAX (où MAX doit jouer)
• Une valeur b aux nœuds MIN (où MIN doit jouer)
On maintient:
• a = valeur du meilleur successeur jusqu’ici (-∞ au départ)
• b = valeur du plus faible successeur jusqu’ici (+∞ au départ)
Donc:
• a = max  ne peut que croître, ne peut pas décroître
– borne inférieure de la valeur finale
• b = min  ne peut que décroître, ne peut pas croître
– borne supérieure de la valeur finale

On a aussi les algo NegaMax et ExpectMiniMax (aussi alphaGO)

