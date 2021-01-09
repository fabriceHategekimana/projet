Intelligence Artificielle
Méthodes de Recherche
Stéphane Marchand-Maillet

Stephane.Marchand-Maillet@unige.ch – University of Geneva – Computer Science – AI Recherche 1

Contenu
• Problèmes de recherche
• Etats et Transitions
• Graphe d’Etats
• Parcours du Graphe

Stephane.Marchand-Maillet@unige.ch – University of Geneva – Computer Science – AI Recherche 2

Problèmes de Recherche
But: résoudre un problème donné
Méthode: par étapes, selon «ce qui est possible»
Exemple: Jeu du Taquin
But: remettre les pièces dans l’ordre en les
déplaçant (gauche-droite, haut-bas)
2
1

3

1

2

3

Taquin-15

Source: wikipedia

Stephane.Marchand-Maillet@unige.ch – University of Geneva – Computer Science – AI Recherche 3

Analyse de l’exemple
2

3

1

1

2
1

3

2
3

1

1

3

???

2

2

1

3

3

1

2

2

3

Pas de solution (exercice)
Stephane.Marchand-Maillet@unige.ch – University of Geneva – Computer Science – AI Recherche 4

Formalisation
Comment formaliser:
• Le problème (ou classe de problèmes)
• Le fait de chercher une solution
• La «difficulté» du problème
• La solution elle-même
• Le fait qu’il y ait (ou pas) de solution

?
Stephane.Marchand-Maillet@unige.ch – University of Geneva – Computer Science – AI Recherche 5

Formalisation
Comment formaliser:
• Le problème (ou classe de problèmes)
– Modèle, catégorie

• Le fait de chercher une solution
– Algorithme

• La «difficulté» du problème
– Complexité

• La solution elle-même
– Convergence

• Le fait qu’il y ait (ou pas) de solution
– Propriétés: existence, unicité, optimalité
Stephane.Marchand-Maillet@unige.ch – University of Geneva – Computer Science – AI Recherche 6

Analyse de l’exemple
1

Catégorisation:
• 1 seul joueur/acteur
• But bien défini
• Actions «discrètes»
• Actions certaines

2

3

Stephane.Marchand-Maillet@unige.ch – University of Geneva – Computer Science – AI Recherche 7

Analyse de l’exemple
1

Catégorisation:
• 1 seul joueur/acteur

2

3

– Dépend seulement de nos actions

• But bien défini
– Test de convergence exact

• Actions «discrètes»
– Possibilités énumérables (dénombrables)

• Actions certaines
– Contexte déterministe (prédictible)
Stephane.Marchand-Maillet@unige.ch – University of Geneva – Computer Science – AI Recherche 8

Formalisation: Etats
On définit la notion d’état du système:
Def: Un état s (state) est une configuration d’un
système.
Un état peut être observable ou non.
Exemples:
2

1

3

2

3

1

Un état si

Un état sj

3

1

1
Ceci n est pas un état

Stephane.Marchand-Maillet@unige.ch – University of Geneva – Computer Science – AI Recherche 9

Notion d’état
Un état est un ensemble de valeurs des
paramètres d’un système.
On parle de vecteur d’état
Exple: Véhicule: position, vitesse, direction,…
Dans notre cas:
• Paramètres: x,y,z,w
• Valeurs: permutations de {1,2,3,«»}

x

z

y

w

système

Stephane.Marchand-Maillet@unige.ch – University of Geneva – Computer Science – AI Recherche 10

Espace d’états
Def: L’espace d’états (state space) S d’un
système est l’ensemble de tous les états
possibles du système.
C’est la couverture de toutes les valeurs
possibles de chaque paramètre

Dans notre cas: S = P({1,2,3,«»})

3

1

1
Ceci n est pas un état
Stephane.Marchand-Maillet@unige.ch – University of Geneva – Computer Science – AI Recherche 11

Taille de l’espace d’états
Dans le cas discret (notre cas), on compte
(énumère) les états, en général en utilisant la
combinatoire du problème.

La taille de S peut être une mesure de la complexité
du problème
Dans notre cas:
• 4 choix pour la 1ere case
• 3 choix pour la 2eme case
• 2 choix pour la 3eme case
• 1 choix pour la 4eme case
4! = 24 états possibles =|P({1,2,3,«»})|
Stephane.Marchand-Maillet@unige.ch – University of Geneva – Computer Science – AI Recherche 12

Note: espace d’états infini
On peut distinguer la notion d’espace d’états
continu ou dénombrables
Espace continu: position d’un véhicule

Espace dénombrable: «infini, non borné mais
discret», «labelisable»

Stephane.Marchand-Maillet@unige.ch – University of Geneva – Computer Science – AI Recherche 13

Espace d’états infini
Conjecture (AIMA 3.2.1 p 73):
A partir de la valeur 4 et étant donné un entier n, on
peut générer une séquence d’opérations factorielles et de
racines carrées pour obtenir une valeur dont la partie
entière est n.

Symboliquement, il existe a,b t.q qquesoit n:
n = int(sqrta(factb(4)))

(la puissance sur les opérateurs indique la composition)
Stephane.Marchand-Maillet@unige.ch – University of Geneva – Computer Science – AI Recherche 14

Espace d’états infini
n = int(sqrta(factb(4)))
Un état est une paire (a,b), on va organiser
l’énumération de ces états.
Il n’y a pas forcément de limite sur a et b. On
doit donc explorer toutes les paires (a,b), ce qui
crée un espace d’état infini.
 On est donc jamais sûrs qu’une solution
n’existe pas, même si la recherche reste
infructueuse
Stephane.Marchand-Maillet@unige.ch – University of Geneva – Computer Science – AI Recherche 15

Formalisation: instanciation
Pour définir un problème on doit définir:
• Un état initial: sI
• Un état final: sG
Dans notre cas:
2

3

1

1

2

3

sI

sG

Les états initiaux ou finaux sont décrits de façon
explicite (exacte) ou implicite (règle)
Exemple: “le 3 doit être en dessous du 1”
Stephane.Marchand-Maillet@unige.ch – University of Geneva – Computer Science – AI Recherche 16

Transition entre états
L’espace d’états rassemble tous les états. Mais
les états sont liés entre eux par des actions
permettant de passer d’un état à un autre (state
transition).
Pour définir un problème on doit aussi définir
les actions possibles
Exple: Action = déplacer une case vers la droite
2

2

1

3
si

1

3
sj

Stephane.Marchand-Maillet@unige.ch – University of Geneva – Computer Science – AI Recherche 17

Transition entre états
Dans notre cas, un état ne dépendra jamais de
son passé. Il est indépendant des transitions
(actions) qui ont mené a lui
2
2
1

2
3

1

3
=

1

2
3

1

2
1

3

Stephane.Marchand-Maillet@unige.ch – University of Geneva – Computer Science – AI Recherche 18

Transitions
Dans notre contexte, les actions possibles sur un
état dépendent de cet état
Exple:
2

2

1

3

2

1

3

2

3

=
2
1

3
3

Note: plutôt que de symboliser
le déplacement d’une case
particulière (1,2,3), on peut
visualiser le déplacement de la
case vide

1

Actions = {2D,3H} = {G,B}
Stephane.Marchand-Maillet@unige.ch – University of Geneva – Computer Science – AI Recherche 19

Transitions
• Actions discrètes: transitions dénombrables, états
dénombrables
• Une transition peut avoir un coût (positif)
– Sinon on considère son coût égal a 1 (on compte les
transitions)

• Plus tard (contexte probabiliste):
G(s’,a,s) = P(s’|s,a)
ici (actions déterministes):
T(s’,s) = matrice de transition (binaire)
(en fait, liste d’adjacence G)
Stephane.Marchand-Maillet@unige.ch – University of Geneva – Computer Science – AI Recherche 20

Graphe d’états
On définit donc le graphe d’états à partir de la
fonction de transition:
• Les nœuds du graphe sont les états
• Les arêtes du graphe sont les transitions

Exple:

z

y

w

etc

2
1

x

etc

2

2
3

2

1

1

3

1
Pourquoi cette illustration est-elle erronée?
Exercice: déployez le graphe du Taquin 2x2

2
3

etc

Stephane.Marchand-Maillet@unige.ch – University of Geneva – Computer Science – AI Recherche 21

Graphe d’états
Les propriétés du graphe d'états sont autant d’indicateurs
sur la complexité du problème:
• Degré, degré moyen
• Connexité
Dans notre cas, le graphe d’états est fixe dans le temps
(les règles ne changent pas)
Plutôt que de l’expliciter (le développer), on le représente
(localement) par la fonction multivoque de voisinage
(fonction successeur):
G: S
P(S)
qui peut aussi invoquer un coût c(s,s’) par arête (s,s’)
Stephane.Marchand-Maillet@unige.ch – University of Geneva – Computer Science – AI Recherche 22

Structures de Données

Application multivoque
 vj est le successeur de vi dans G si il existe
el = (vi, vi)
alors vi est le prédécesseur de vj dans G
 l'ensemble des successeurs d'un sommet vi dans G est
noté NG+ (vi)
 l'ensemble des prédécesseurs d'un sommet vi dans G est
noté NG- (vi)
 L'application G qui à tout sommet de V fait correspondre
l'ensemble de ses successeurs est une application
multivoque. On a:

G:

V  P (V )

G

v i  N (v i )

G 1 :

V  P (V )
v i  NG (v i )

donc, G-1 est l'application qui a tout sommet de V fait
correspondre l'ensemble de ses prédécesseurs
marchand@cui.unige.ch - Université de Genève

Structures de Données – Rappels Graphes

23

Formalisation
Le graphe d’états donne une formalisation
pour la résolution de problèmes. Un
problème s’énonce formellement par:
• L’espace des états S
• Une fonction de transition G (avec ou sans
cout)
• Un état initial sI
• Un état final sG

Stephane.Marchand-Maillet@unige.ch – University of Geneva – Computer Science – AI Recherche 24

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
Stephane.Marchand-Maillet@unige.ch – University of Geneva – Computer Science – AI Recherche 25

Un mot sur l’observabilité
• Notion liée formellement à la théorie des
Systèmes Dynamiques
• Essentiellement liée à la réversibilité de la
fonction de transition

• Ici on considère un contexte observable
• On a une vue globale du système
– Cf aussi plus tard (Partially Observable…)

Stephane.Marchand-Maillet@unige.ch – University of Geneva – Computer Science – AI Recherche 26

Exemples de problèmes
•
•
•
•
•
•
•
•

Taquin NxN
Rubik’s cube
Reines sur échiquier
Actions d’un robot
Déplacement de véhicule (path planning)
Plus court chemin
Voyageur de Commerce
…
Stephane.Marchand-Maillet@unige.ch – University of Geneva – Computer Science – AI Recherche 27

Types de problèmes
Taquin, Rubik’s cube: on cherche à minimiser le
nombre de coups (déplacements) pour arriver à
un but explicite (image finie, nombres classés)
• Le chemin vers la solution est important

Reines sur l’échiquier: on cherche à construire
une solution dont on est pas sûr qu’elle existe
• La solution elle-même est importante
(nombre maximum pour une taille d’échiquier
donnée)
Stephane.Marchand-Maillet@unige.ch – University of Geneva – Computer Science – AI Recherche 28

Résolution
Une solution est un chemin de l’état initial sI à
l’état final sG dans le graphe d’états G
L’existence de la solution est liée à la connexité
du graphe
L’optimalité de la solution est liée à son coût

Stephane.Marchand-Maillet@unige.ch – University of Geneva – Computer Science – AI Recherche 29

Connexité du graphe d’etats
1

2

3

1

2

3

2
3

1

1

2

3

2

1

3

1
3

2

1
2

3

2

2

3

1

1

3

1

1

3

2

3

2

2
3

1

2

3

1

1
3

2

1

3

2

2

3

2

2

3

1

1

3

1

1

3
2

3

3

1

2

2

3
1

3
2

1

1

2

3
1

2

Stephane.Marchand-Maillet@unige.ch – University of Geneva – Computer Science – AI Recherche 30

Connexité du graphe d’etats
Taquin 3x3: 32! = 9! = 362’880 états. Impossible
de déployer le graphe
Taquin NxN: on voudrait étudier le problème en
general
• Dans ce cas on peut…

Stephane.Marchand-Maillet@unige.ch – University of Geneva – Computer Science – AI Recherche 31

Taquin NxN: connexité
On se donne une mesure de la qualité d’un état
(comme fonction de la distance à l’état
solution):
– On lit les valeurs en séquence et on compte le
nombre d’inversions
1

2

4
8

3
6

7

5

(6-5), (8-7), (8,5), (7-5)
=4

1

2

4

6

8

7

3

5

On remarque qu’un mouvement horizontal
ne change pas le résultat
Stephane.Marchand-Maillet@unige.ch – University of Geneva – Computer Science – AI Recherche 32

Taquin NxN: connexité
• On peut identifier le taquin avec l’espace des
permutations P({1,…,N2-1})
• La mesure est liée à la signature des
permutations
• Les mouvements ne changent pas la parité de
la mesure (resp. la signature)
2 composantes connexes (pair/impair - +1/-1)

(cf document annexe sur Moodle
pour preuve formelle)
Stephane.Marchand-Maillet@unige.ch – University of Geneva – Computer Science – AI Recherche 33

Résolution
On représente le graphe par une matrice
d’adjacence T (cf Transitions)
On sait que (Id-T)-1 nous liste les chemins entre
chaque noeud du graphe
Sauf que: c est impraticable, souvent le nombre
d’états croît exponentiellement avec la taille du
problème
Nombre d’états du taquin NxN = (N2!)
N

2

3

4

Etats

24

362’880

~21 x 1012

…

7
~6 x 1062

Stephane.Marchand-Maillet@unige.ch – University of Geneva – Computer Science – AI Recherche 34

Résolution
On contre la croissance exponentielle des
parametres par des definitions et actions
implicites (recursives, de proche en proche):
• Algorithme de recherche de chemin dans un
graphe: BFS, DFS,…
– exploration de proche en proche

Construction d’un arbre de recherche
- Depend de la stratégie de recherche
Stephane.Marchand-Maillet@unige.ch – University of Geneva – Computer Science – AI Recherche 35

Arbre de recherche
But: Explorer le graphe à partir de sI
Trace de la stratégie d’exploration
Nœuds: contiennent les états visités
Racine: correspond a l’état initial sI
Définition récursive:
Les enfants(v) sont construits à partir de G(state(v))

Cycle  arbre infini (même si graphe fini)
Stratégie de construction: exploration type DFS, BFS..
Stephane.Marchand-Maillet@unige.ch – University of Geneva – Computer Science – AI Recherche 36

Structures de Données

Méthode générale de parcours de graphe
 Méthode générale de parcours de graphe
 Généralise le DFS aussi bien que le BFS.

 Cette méthode consiste à classer les sommets en 3
catégories:
 La catégorie A des sommets déjà visités (ceux qui apparaissent
dans l’arbre de parcours)
 La catégorie B des sommets adjacents à ceux de la catégorie A
mais pas encore visités (sommets qui peuvent être atteints)
 La catégorie C des sommets invisibles qui n’ont pas encore été
rencontrés du tout (qui ne peuvent pas être atteints depuis un
sommet déjà visité)

Structures de Données – Cours graphes 1ere annee

37

Parcours de graphe
B

B

C
C

C

C

C

A

C

B
C

B

Les nœuds A et B forment toujours une composante connexe
B

A

B
C

B

C

C

A

C

B
C

B

Stephane.Marchand-Maillet@unige.ch – University of Geneva – Computer Science – AI Recherche 38

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
Stephane.Marchand-Maillet@unige.ch – University of Geneva – Computer Science – AI Recherche 39

Algorithme general de recherche
• Catégorie A: Nœuds déjà visités
– sortis de la liste
– «ensemble connexe dominant la frange»

• Catégorie B: Nœuds pas encore visités avec
voisins visités (en A)
– Nœuds dans la liste, «frange»

• Catégorie C: nœuds pas encore visités (ni en B)
– Nœuds jamais passés dans la liste

Un état fera le trajet C-B-A
Stephane.Marchand-Maillet@unige.ch – University of Geneva – Computer Science – AI Recherche 40

Noeud et expansion
Un nœud v de l’arbre contient:
• L’état s correspondant (nœud du graphe)
 state(v)=s

• Le parent dans l’arbre (backtracking)
• La profondeur dans l’arbre
• Eventuellement:
– les enfants
– le coût du chemin jusqu’à lui (g(v))

Expansion d’un nœud v :
• C’est l’application de la fonction G(s) sur l’état
s=state(v) correspondant à v (modulo la gestion de
cycles)
Stephane.Marchand-Maillet@unige.ch – University of Geneva – Computer Science – AI Recherche 41

Nœuds du graphe / nœuds de l’arbre
Graphe: nœud s
L’état s est unique
pour chaque
nœud
S
état courant

Arbre: nœud v
S
p

d
i

Pointeurs vers les nœuds contenant un
état s’ vers lequel la transition est possible

 Le graphe peut être représenté par sa
matrice de transition ou par G

s = state(v): état courant (éventuellement
pointeur vers le nœud du graphe).
p: parent du nœud dans l arbre
d: profondeur du nœud dans l’arbre
i: informations complémentaires
• Coût jusqu’à v = g(v)
• Enfants de v dans l’arbre

Stephane.Marchand-Maillet@unige.ch – University of Geneva – Computer Science – AI Recherche 42

Propriétés d’un algorithme de recherche
Complétude:
• Un algorithme est complet si il trouve la solution
du problème (en temps fini) si elle existe
Contre-exemple: reste pris dans un cycle

Optimalité (de la solution):
• Un algorithme est optimal si il trouve la meilleure
solution (cout minimal) quand il y en a plusieurs
Exemple: plus court chemin
Stephane.Marchand-Maillet@unige.ch – University of Geneva – Computer Science – AI Recherche 43

Indicateurs de complexité
•
•
•
•
•

Nombre d’états (taille du graphe)
Degré moyen du graphe
Distribution des états solution
Espace mémoire / état
Temps d’exécution de la fonction G

On verra d’autres indicateurs particuliers à
chaque technique de recherché

Stephane.Marchand-Maillet@unige.ch – University of Geneva – Computer Science – AI Recherche 44

Mise en pratique
• Recherche aveugle
– Uninformed search

• Recherche heuristique
– Informed search
– Heuristic-based search

Stephane.Marchand-Maillet@unige.ch – University of Geneva – Computer Science – AI Recherche 45

Résumé
Certains problèmes peuvent se formaliser sous
forme de recherche de chemin dans un graphe
d’état
– Notion d’état + action / transition = graphe d’état
– Chemin = solution
– Le chemin est trouvé par un algorithme de
recherche

(!) Pas tous les problèmes de recherche se
résolvent de cette façon
Stephane.Marchand-Maillet@unige.ch – University of Geneva – Computer Science – AI Recherche 46

