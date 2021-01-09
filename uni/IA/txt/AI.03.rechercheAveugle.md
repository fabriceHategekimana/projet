Intelligence Artificielle
Recherche Aveugle
(Uninformed Search)
Stephane Marchand-Maillet

Stephane.Marchand-Maillet – Université de Geneve

Intelligence Artificielle

AI Aveugle - 1

Contenu
Algorithmes de recherche:
• Largeur
• Profondeur
• Profondeur Limitée
• Approfondissement itératif (IDS)
• Bidirectionnelle
• Coût uniforme
 principes, complexité
Stephane.Marchand-Maillet – Université de Geneve

Intelligence Artificielle

AI Aveugle - 2

Introduction
• On applique le principe de recherche de
solution sans utiliser de connaissance a priori
(aveugle – uninformed search)
• Essentiellement, cela revient à prendre la
fonction de voisinage (les successeurs d’un
état donné) ou la liste (catégorie B) sans ordre
particulier
• L’alternative est la recherche heuristique
(informed search) – prochain chapitre
Stephane.Marchand-Maillet – Université de Geneve

Intelligence Artificielle

AI Aveugle - 3

Instance

Graphe G

Formalisation
Le graphe d’états donne une formalisation pour
la résolution de problèmes. Un problème
s’énonce formellement par:
• L’espace des états S
• Une fonction de transition G (avec ou sans
cout)
• Un état initial sI
• Un état final sG
 Une solution est un chemin de sI à sG dans G
Stephane.Marchand-Maillet – Université de Geneve

Intelligence Artificielle

AI Aveugle - 4

Algorithme general de recherche
liste  vide ; liste.push(sI)
repeat
scourant  liste.pop()
if (scourant == sG)
break
list.push(G(scourant))  expansion de scourant
until liste.len() == 0
if (scourant == sG)
backtrack solution
else
pas de solution

Recherche

Explicitation
de la solution

 Tout est dans la stratégie de gestion de la liste et
l’expansion des noeuds (états)
Stephane.Marchand-Maillet – Université de Geneve

Intelligence Artificielle

AI Aveugle - 5

Algorithme general de recherche
• Categorie A: Noeuds deja visités
– sortis de la liste

• Catégorie B: Noeuds pas encore visités avec
voisins visités (en A)
– Noeuds dans la liste

• Catégorie C: noeuds pas encore visités (ni en B)
– Noeuds jamais passés dans la liste

Un état fera le trajet C-B-A
Stephane.Marchand-Maillet – Université de Geneve

Intelligence Artificielle

AI Aveugle - 6

Recherche en Largeur
• La liste est une file FIFO (type file d’attente)
• On progresse en explorant toutes les stratégies à
la fois
 Expansion du nœud le moins profond de la liste
Facteurs de complexité:
• Nombre maximum (moyen) de successeurs d’un
etat: b = facteur de branchement
• Profondeur de la solution dans l’arbre : d
Stephane.Marchand-Maillet – Université de Geneve

Intelligence Artificielle

AI Aveugle - 7

Recherche en Largeur
• Complet: garantit de trouver la solution
• Optimal: trouve la solution la plus simple (en
nombre d’actions)
Nombre de nœuds de l’arbre produits:
N=b0+ b1+ b2+…+ bd= (b(d+1)-1)/(b-1) = O(bd)
Complexité:
• Temps: O(bd)
• Espace: O(bd)
Stephane.Marchand-Maillet – Université de Geneve

Intelligence Artificielle

AI Aveugle - 8

Recherche en Largeur (BFS)
c

a

d

b

s

m

o

SI

r

g

t

q

e
f

l
k

u

n

p
SG

h

i

j

Graphe d’états
Stephane.Marchand-Maillet – Université de Geneve

Intelligence Artificielle

AI Aveugle - 9

Recherche en Largeur (BFS)
2

2

1

1

B

2

B

SI

C

2

B
C

0
1

2

1

B

B

C

SG
2

Progression du BFS
Stephane.Marchand-Maillet – Université de Geneve

2

2

Voir aussi: https://visualgo.net/en/dfsbfs
Intelligence Artificielle

AI Aveugle - 10

Recherche en Largeur (BFS)
c

a

d

b

s

m

o

SI

r

g

t

q

e
f

l
k

u

n

p
SG

h

i

j

Transitions sélectionnées dans le graphe d’états
Stephane.Marchand-Maillet – Université de Geneve

Intelligence Artificielle

AI Aveugle - 11

Recherche en Largeur (BFS)

SI = e
e

d

c

m

b

a

k

l

i

Nœud v
State(v) = f
Parent(v) = racine
d=1

f

j

g

h

Arbre de recherche correspondant
Stephane.Marchand-Maillet – Université de Geneve

Intelligence Artificielle

AI Aveugle - 12

Remarque sur la complétude
• En cas de cycle dans le graphe, l’algorithme
d’exploration court le risque de re-visiter des
états déjà visités et donc ne pas se terminer
• L’exploration peut elle-même contenir un
mécanisme pour éviter les re-visites
(organisation de la catégorie « B »)
• Sinon on s’assurera de maintenir une liste
globale (exple: hash-table) des nœuds visités
(marquage de la catégorie « A »)
Stephane.Marchand-Maillet – Université de Geneve

Intelligence Artificielle

AI Aveugle - 13

Recherche en Profondeur
• La liste est une file LIFO (type Pile)
• On explore chaque stratégie jusqu’au bout

 Expansion du nœud le plus profond de la liste
Facteurs de complexité:
• Nombre maximum (moyen) de successeurs
d’un état: b = facteur de branchement
• Profondeur de la solution dans l’arbre: d
• Profondeur maximum d’une feuille: m
Stephane.Marchand-Maillet – Université de Geneve

Intelligence Artificielle

AI Aveugle - 14

Recherche en Profondeur
• Complet si l’arbre est fini
• Non optimal (en général)

Complexité:
• Temps: b0+ b1+…+ bm= O(bm)
(m peut être >> d)

• Espace: O(b.m)
Lineaire !
m est le facteur clé
Stephane.Marchand-Maillet – Université de Geneve

Intelligence Artificielle

AI Aveugle - 15

Recherche en Profondeur (DFS)
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
Stephane.Marchand-Maillet – Université de Geneve

Intelligence Artificielle

AI Aveugle - 16

Recherche en Profondeur Limitée
Comme m est un facteur de complexité, on
borne m par M (donné)
• Complet si d<=M
• Pas de garantie d’optimalité
Complexité:
• Temps: b0+ b1+…+ bM= O(bM)
• Espace: O(b.M)
Stephane.Marchand-Maillet – Université de Geneve

Intelligence Artificielle

AI Aveugle - 17

Recherche en Profondeur Limitée
M=4

2
4

B

2

5
3
3
5

4

X

4

4
B

1
1
4
6

5
X

1
3
10

B
0
0
SI

8

C

C

B

C

C

SG

2
9

C

B

C

Exercice: Completer l’exploration avec M=4
Stephane.Marchand-Maillet – Université de Geneve

Intelligence Artificielle

AI Aveugle - 18

Approfondissement itératif (IDS)
Recherche en profondeur Limitée:
• Fournit une solution approximée
– Solution si d<=M
– Indécidable si d>M

On itère sur M: approfondissement itératif:
(IDS: Iterative Depth Search)

Stephane.Marchand-Maillet – Université de Geneve

Intelligence Artificielle

AI Aveugle - 19

Recherche en Profondeur Limitée
M=4

2
4

B

2

5
3
3
5

1
1

4

X

4
SG
4
B

4
6

5
X

1
3
10

B

0
0
SI

8

C

C

C
B

C

C

2
9

Stephane.Marchand-Maillet – Université de Geneve

B

C

Intelligence Artificielle

AI Aveugle - 20

Recherche en Profondeur Limitée
M=4

2
4

B

2

5
3
3
5

1
1

4

X

4
SG
4
B

4
6

5
X

1
3
10

B

0
0
SI

8

C

C

C
B

C

C

2
9

B

C

Note: Il semblerait que cette solution ne soit pas trouvée, mais en fait
elle serait trouvée à l’étape M=3 (cf slide suivant)
Stephane.Marchand-Maillet – Université de Geneve

Intelligence Artificielle

AI Aveugle - 21

Recherche en Profondeur Limitée
M=3

2
4

B

2

X
3
3

1
1

4
C

X

2
4

3
5

B
0
0
SI

SG
B

C

C

C

C

B

B

C

C

C

C

C

SG est atteint  l’algorithme s’arrête
Stephane.Marchand-Maillet – Université de Geneve

Intelligence Artificielle

AI Aveugle - 22

Approfondissement itératif (IDS)
• Complet: car on explore éventuellement
toutes les solutions
• Optimal: car on trouve la solution la plus
simple (profondeur d) avant les autres

Complexité:
• Temps: (d+1)b0+ db1 + (d-1)b2 +…+ bd= O(bd)
• Espace: O(b.d)

Stephane.Marchand-Maillet – Université de Geneve

Intelligence Artificielle

AI Aveugle - 23

Approfondissement itératif (IDS)
• Les recherches répétées sont celles des
niveaux inférieurs (0, 1,…, d-1), que l’on répète
de moins en moins ((d+1) fois, d fois, (d-1)
fois,…etc)
• La croissance exponentielle
a0b0+ a1b1 + a2b2 +…+ adbd
rend la somme niveaux inferieurs aussi chère
que le niveau lui-même:
b0+ b1+…+ bj = O(bj+1)
Stephane.Marchand-Maillet – Université de Geneve

Intelligence Artificielle

AI Aveugle - 24

Approfondissement itératif (IDS)
Exemple: b=10
Profondeur d’abord:
nDFS = b0+ b1+…+ bd
IDS:
nIDS = (d+1)b0+ db1 + (d-1)b2 +…+ bd
D

5

8

10

15

nDFS

11’111

11’111’111

1x1011

1x1016

nIDS

23’456

23’456’789

2x1011

2x1016

Stephane.Marchand-Maillet – Université de Geneve

Intelligence Artificielle

AI Aveugle - 25

Recherche Bidirectionnelle
On exploite le fait que
bd/2<< bd
On développe des chemins par la recherche en
largeur à partir de sI et sG
À leur intersection, on joint le chemin qui mène
de sI à sG
Condition: existence de G-1

On doit connaitre explicitement G-1 pour
développer le chemin à partir de sG
Stephane.Marchand-Maillet – Université de Geneve

Intelligence Artificielle

AI Aveugle - 26

Recherche Bidirectionnelle

SI

SG

Adapted rom AIMA: Section 3.4 – page 91

Stephane.Marchand-Maillet – Université de Geneve

Intelligence Artificielle

AI Aveugle - 27

Recherche Bidirectionnelle
• Complet: car les recherches se rejoignent si
une solution existe
• Optimal: car on trouve la solution la plus
simple à la jointure des chemins

Complexité (recherche en Largeur pour d/2):
• Temps: O(bd/2)
• Espace: O(bd/2)

Stephane.Marchand-Maillet – Université de Geneve

Intelligence Artificielle

AI Aveugle - 28

Recherche en coût uniforme
Similaire à la recherche en Largueur
g(v): coût du chemin de la racine au nœud v

g(v) représente la somme des coûts de transition
entre les états c(s,s’) le long du chemin
Expansion du nœud le moins coûteux de la liste
La liste est un Tas-min des coûts
Analogue au plus court chemin de Dijkstra
Stephane.Marchand-Maillet – Université de Geneve

Intelligence Artificielle

AI Aveugle - 29

Recherche en coût uniforme
• Complet: garantit de trouver la solution
• Optimal: trouve la solution la moins coûteuse

Complexité:
• Temps: O(bd)
• Espace: O(bd)

Stephane.Marchand-Maillet – Université de Geneve

Intelligence Artificielle

AI Aveugle - 30

Recherche en Coût Uniforme

Exercice: Attribuez des coûts et développez l’algorithme
Stephane.Marchand-Maillet – Université de Geneve

Intelligence Artificielle

AI Aveugle - 31

Recherche en Coût Uniforme

2

2

1

1

3

2
1

2

1

2
2

2

SI

1

2
3

0

3

1

3

2
1

1
1

SG

1

Voir aussi: https://visualgo.net/en/sssp
Stephane.Marchand-Maillet – Université de Geneve

Intelligence Artificielle

AI Aveugle - 32

Résumé

AIMA: Section 3.4 – page 91
Stephane.Marchand-Maillet – Université de Geneve

Intelligence Artificielle

AI Aveugle - 33

