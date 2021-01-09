Intelligence Artificielle
Recherche Heuristique
(Informed Search)
Stephane Marchand-Maillet

Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Heuristiques - 1

Recherche aveugle: aléa
Dans la recherche aveugle, certaines opérations
sont “aléatoires”:
• Elles résultent de l’ordre dans lequel le
problème est présenté
– Utilisation du voisinage, des propriétés, …

• Un choix existe auquel on a répondu de facon
aléatoire, en l’absence de meilleure
alternative
– Direction d’exploration, …
Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Heuristiques - 3

Recherche en Profondeur (DFS) - Rappel
B

2

B

B

B

1

3

C

SI

4

6

5

0
10

8

C

C

B

7

C

C

SG
9

B

C

Voir aussi: https://visualgo.net/en/dfsbfs
Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Heuristiques - 4

Recherche aveugle: aléa
Exple: Navigation
• On utilise le BFS pour chercher le chemin
optimal d’un état (SI) à un autre (SG)
SG
SI

Zone d’exploration

Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Heuristiques - 5

Recherche aveugle: aléa
Exple: Navigation
• On utilise le DFS pour chercher le chemin
optimal d’un état (SI) à un autre (SG)
SG
SI

Zone d’exploration

Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Heuristiques - 6

Recherche aveugle: aléa
Exple: Navigation
• On utilise xxx pour chercher le chemin optimal
d’un état (SI) à un autre (SG)

 Y aurait-il un choix plus judicieux qui fasse
converger plus vite l’algorithme (trouve la
solution plus rapidement)?
… quitte à quand même, au pire, explorer des
solutions inutiles
Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Heuristiques - 7

Recherche aveugle: aléa
Idée: navigation “orientée”
SG
SI

Toujours choisir l’état suivant le plus proche de SG

st+1 = argmin(dist(s- sG) t.q s voisin de st)
 C est une heuristique
Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Heuristiques - 8

Informed search
• On applique le principe de recherche de
solution en injectant de la connaissance a
priori (informed search)
• On applique un classement particulier
(heuristique, basée sur une connaissance a
priori) à la liste (catégorie B) pour piloter
l’exploration et la diriger vers la solution sG
plus rapidement
Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Heuristiques - 9

Heuristique: définition
Def: une heuristique est une fonction h
d’estimation de coût telle que:
h: V

R+

avec h(v)=0 si state(v)=sG

h(v) représente une estimation du coût du
chemin de l’état actuel à l’état final sG passant
par le nœud v (ayant v comme première étape)

Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Heuristiques - 10

Heuristique: exemples
• Problème du Sac à Dos: mettre les gros objets
d’abord
(on s’assure d’avoir de la place pour les gros objets)

• Problème du Sac à Dos: mettre un gros objet et à
chaque fois « compléter » par des petits
(on ne perd pas de place)
• Voyageur de commerce: faire un DFS et parcourir
cet arbre (2-OPT)
(heuristique prouvée)
Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Heuristiques - 11

Heuristique: exemples
Navigation:
SG
SI

Une heuristique ne doit pas changer la complétude
de l’algorithme: elle n’empêche pas l’algorithme de
trouver la solution si elle existe et si il la trouvait
sans heuristique
Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Heuristiques - 12

Heuristique: exemples
• Navigation: on essaie les directions aléatoirement
 On revient à la recherche aveugle
• Navigation: toujours aller dans la direction la plus
opposée au but
On trouvera le but après avoir exploré tout l’espace
L’heuristique est mauvaise mais n’empêche pas de
trouver la solution
La qualité d’une heuristique peut ne pas être garantie.
Elle dépend de la compréhension du problème et de la
variabilité des situations (heuristique efficace « en
moyenne »)
Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Heuristiques - 13

Fonction d’évaluation
Def: la fonction d’évaluation f fournit le coût
estimé d’une solution (chemin) passant par le
nœud v
On trie les nœuds v de la catégorie “B”
(nœuds dans la liste) par valeurs croissantes
de f(v)
La liste est un Tas-Min
On explore d’abord les solutions qu’on estime
être moins coûteuses (Best First Search)
Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Heuristiques - 14

Best First Search (moins coûteux d’abord)
liste  vide ; liste.push(sI)
repeat
scourant  liste.pop()
if (scourant == sG)
break
list.push(sortf(G(scourant)))
until liste.len() == 0

Recherche

if (scourant == sG)
backtrack solution
else
pas de solution

Explicitation
de la solution

 Tout est dans la stratégie de gestion de la liste et
l’expansion des noeuds (états)
Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Heuristiques - 15

Recherche en coût uniforme (RAPPEL)
Similaire à la recherche en Largueur
g(v): coût du chemin de la racine au nœud v

g(v) représente la somme des coûts de transition
entre les états c(s,s’) le long du chemin
Expansion du nœud le moins coûteux de la liste
La liste est un Tas-min des coûts
Analogue au plus court chemin de Dijkstra
Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Heuristiques - 16

Fonction d’évaluation f(v)
• C’est le cœur de l’algorithme Best First Search
• Peut prendre toutes les formes.
Exemples:
• f(v) = h(v) : heuristique pure
Greedy Best First Search

• f(v) = g(v) + h(v) : prise en compte de la
connaissance actuelle

Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Heuristiques - 17

Propriétés de Greedy Best First Search
• Complet: Préserve la complétude des algorithmes de
recherche (complet si l’espace de recherche est fini)
• Optimal: non

Complexité:
• Temps: O(bm) avec m profondeur maximale
• Espace: O(bm) conserve les nœuds pour f(v)
La complexité du «pire des cas» (worst case) ne
s’améliore pas en général (car elle considère l’heuristique
inefficace)
Il faut regarder la complexité empirique (en moyenne) qui
illustre mieux l’efficacité de l’heuristique à éviter le pire
des cas
Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Heuristiques - 18

Heuristique admissible
Def: Une heuristique est admissible si elle sousestime le coût du chemin vers la solution
Si h*(v) est le coût réel du nœud v à la solution
(heuristique idéale), alors si h est admissible:
0<= h(v) <= h*(v) pour tout nœud v

Une heuristique admissible est optimiste

Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Heuristiques - 19

Heuristique admissible: exemple
• Distance Euclidienne sur un espace de navigation
discrétisé: admissible

• Distance de Manhattan: pas admissible si les
mouvements diagonaux sont permis (cf
illustration)
Une heuristique admissible est une stratégie qui
ne prend pas en compte certaines contraintes
(obstacles) du problème
Une heuristique admissible ne rajoute pas de
contrainte
Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Heuristiques - 20

Heuristique admissible: exemple
SI

Heuristique admissible

SG
SI

Heuristique non-admissible
SG

Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Heuristiques - 21

Heuristique consistante
Si on veut éviter de répéter l’exploration d’un même état:
• On veut que le coût de ré-accéder à cet état soit au moins aussi élevé
que la première fois
• Sinon le coût d’accès aux états suivants devra être mis à jour en partant
de ce nouveau coût
Une heuristique qui maintient cet ordre est dite consistante:
Si il existe une transition de s à s’ de coût c(s,s’) alors

h(s) ≤ h(s’) + c(s,s’)
SG

h(s)
s

c(s,s’)

s’

h(s’)

Similaire à l’inégalité triangulaire
Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Heuristiques - 22

Preuve (par l’absurde)
• Supposons que les nœuds v and v’ correspondent au même
état (state(v)=state(v’)) avec g(v’) < g(v) mais v est atteint
en premier
• v’ ne pouvait être en catégorie B (frange) quand v a été
atteint car g(v’) < g(v), donc
g(v’) + h(v’) < g(v) + h(v)

• Donc v’ est l’enfant d’un autre nœud v’’ de la frange, après
que v soit étendu
g(v) + h(v) ≤ g(v’’) + h(v’’)

• En rassemblant, on a
g(v’) + h(v’) < g(v’’) + h(v’’)

ou
h(v’’) > h(v’) + c(v’’,v’)
 pas de consistance
Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Heuristiques - 23

Précision heuristique
La précision heuristique évalue la qualité d’une
heuristique:
Si h1 et h2 sont 2 heuristiques admissibles avec
h1(v) >= h2(v) pour tout nœud v
alors h2 est plus précise que h1 et on a
0 <= h1 <= h2 <= h*
(h2 est plus proche de h* que h1)
La précision d’une heuristique ne tient pas compte de sa
complexité
Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Heuristiques - 24

Best First Search (moins coûteux d’abord)
liste  vide ; liste.push(sI)
repeat
scourant  liste.pop()
if (scourant == sG)
break
list.push(sortf(G(scourant)))
until liste.len() == 0

Recherche

if (scourant == sG)
backtrack solution
else
pas de solution

Explicitation
de la solution

 Tout est dans la stratégie de gestion de la liste et
l’expansion des noeuds (états)
Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Heuristiques - 25

Approximation: Beam search
C est le Best First Search avec une limite de longueur pour
la liste:
• Consommation mémoire limitée
• Temps de recherché réduit
On limite à B>0 le nombre d’états suivants à explorer:
Au lieu de:
list.push(sortf(G(scourant)))
on a:
list.push(pruneB(sortf(G(scourant))))
On ne développe que les B états les plus prometteurs
Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Heuristiques - 26

Algorithme A* (A-star)
C’est l’algorithme Best First Search avec la
fonction d’évaluation:
f(v) = g(v) + h(v)
ou h est une heuristique admissible et
consistante, et
c(s,s’) >= e >0
pour tout s et s’
Sous ces conditions:
l’algorithme A* est complet et optimal
Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Heuristiques - 27

Complétude de A*
Sur un graphe fini:
• A* explore le graphe complètement au pire des
cas et donc trouvera la solution si elle existe
Sur un graphe infini avec:
• Un facteur de branchement fini
• Un cout par arête strictement positif
c(s,s’) ≥ e>0

l’algorithme trouve la solution en temps fini si elle
existe
Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Heuristiques - 28

Optimalité de A*
• Si l’heuristique est admissible, A* est optimal
– La solution trouvée est optimale

• Preuve (par l’absurde):
1. Supposons que l’on est sur le point d’étendre un nœud
solution v (state(v)=s=sG) sous-optimal (g(v)=c > c*, ou le
coût c* est optimal)
2. Soit v* un nœud solution optimal (à venir)
3. Il doit y avoir dans la frange un nœud v’ qui est sur le
chemin vers v*
4. Donc g(v) = c > c* = g(v*) ≥ g(v’) + h(v’)
5. Mais donc, v’ devrait être étendu en premier (si h est
admissible)  contradiction
Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Heuristiques - 29

Optimalité de A* (efficacité)
L’efficacité de A* est optimale
– Tout autre algorithme (utilisant la même heuristique h)
doit développer au moins autant de nœuds que A*

Preuve :
1. En dehors de la solution, A* étend tous (et
seulement) les nœuds v tels que g(v) + h(v) < c*
– Si il n’y a pas de nœud non-solution t.q g(v) + h(v) = c*

2. Tout autre algorithme (utilisant la même heuristique
h) doit aussi étendre ces nœuds (pour chercher une
solution)
Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Heuristiques - 30

Propriétés de A*
• Si h2 est plus précise que h1 alors tous les
nœuds produits par A* avec h2 (fonction f2)
seront produits par A* basé sur h1 (fonction f1),
sauf certains nœuds tels que f1(v) = f2(v) = f*(v)
(solutions optimales pour lesquelles h1 et h2
choisiront différents ex-aequo)
• A* peut explorer indéfiniment si il existe une
infinité de nœuds v tels que
f(v)<= f(v*) avec state(v*) = sG
A* les explorera avant de trouver v* (sG)
Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Heuristiques - 31

Stratégie IDA*

(Iterative deepening A*)

IDS limite la profondeur  évite que la recherche
en profondeur explore des chemins indéfiniment

Même principe: IDA* limite f(v)
 Ne pas approfondir des chemins de coût excessif
par rapport à:
• une connaissance à priori
• une contrainte de l’environnement (temps,
mémoire, budget,….)
• …
Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Heuristiques - 33

IDA*
Algorithme:
fmax = f(vI) (state(vI) = sI)
répéter
• expansion des nœuds v pour lesquels f(v)<=fmax
• fixer fmax = min(f(v) t.q v est une feuille)
jusqu’à solution
 alterne l’exploration par niveaux
Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Heuristiques - 34

Propriétés de IDA*
IDA* :
• Complet
• Optimal
• Utilise moins de mémoire que A*
• Ne nécessite pas de tri explicite de la liste (le tri
se fait par le choix du noeud suivant à
developper)

• Revisite des chemins hors du chemin courant
• N’offre pas une utilisation optimale de la
memoire (AIMA p 101-107)
Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Heuristiques - 36

SMA*
Simplified Memory-bounded A*
Idée simple:
• On fixe la limite mémoire
• si la limite est atteinte, on enlève le noeud le moins
interessant

Propriétés:
• Comme A* tant que la limite n’est pas atteinte
• Complet si la mémoire est suffisante
• Optimal si la mémoire est suffisante pour contenir le
chemin solution le moins profond
• Optimal dans les contraintes mémoire données
Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Heuristiques - 37

Génération d’heuristiques
Une stratégie de création d’heuristiques est la relaxation
du problème:
– On rend le problème plus simple
– On enlève des contraintes

Exemple:
• Le « nombre de pièces mal placées » relaxe le
problème en imaginant que les pièces peuvent se
déplacer librement (1 coup par pièce)
Un problème idéalement relaxé est:
• Simple a résoudre
• Bien moins couteux à résoudre que l’original
On peut générer des heuristiques automatiquement
Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Heuristiques - 38

Alternatives
Stratégies de recherche:
• Locale: pas d’arbre conservé, juste une
connaissance locale (seule la solution est
importante, pas le chemin)
• Steepest: on développe seulement le noeud de
coût minimal
Autres strategies:
• Monte Carlo
• Beam search
• Algorithmes génétiques
Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Heuristiques - 39

Quand utiliser la recherche?
• Quand l’espace d’états est de taille
“raisonnable” (pour une énumération
“systématique”)
• Quand il existe de bonnes heuristiques
• Quand on ne peut pas calculer de gradient
vers la solution (peut être vu comme une
heuristique pour améliorer la solution
courante)
Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Heuristiques - 40

Résumé
• Une heuristique permet d’exploiter l’aléa dans
les recherche (en le remplaçant par une
connaissance a priori)
• Une heuristique ne doit pas changer la
complétude
• Une heuristique peut être admissible et/ou
consistante
• L’algorithme A* donne des garanties
d’optimalité et de complétude
• On peut lui associer des variantes en fonction
des contraintes (temps et mémoire)
Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Heuristiques - 41

