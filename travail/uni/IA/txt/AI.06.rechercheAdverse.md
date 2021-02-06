Intelligence Artificielle
Recherche Adverse
(Jeux)
Stephane Marchand-Maillet

Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Adverse-1

Contenu
• Contexte: recherche adverse
• Algorithme MIN-MAX
• Elagage a-b

Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Adverse-2

Jeux
• Prototype de l’Intelligence:
Savoir jouer contre/battre un adversaire (intelligent)
• ont toujours été un support au développement de l’IA
– Cohérents avec le Test de Turing

• Premier article sur l’IA (1950):
Programming a Computer for Playing Chess.
CLAUDE E. SHANNON Philosophical Magazine,
Ser.7, Vol. 41, No. 314 – March 1950

https://vision.unipv.it/IA1/aa2009-2010/ProgrammingaComputerforPlayingChess.pdf
Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Adverse-3

Historique

1997: Deep Blue vs Kasparov
Stephane Marchand-Maillet – University of Geneva – Computer Science

2016: AlphaGo vs Lee Sedol
AI Adverse-4

Exemple
Reversi (Othello)

But: placer le plus de pions de sa couleur
Jeu: encadrer des pions adverses pour les
« renverser »
Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Adverse-5

Analyse de l’exemple
Catégorisation:
• 2 joueurs
– Ne dépend pas seulement de nos actions

• But bien défini
– Gagner la partie

• Actions «discrètes»
– Possibilités énumérables (dénombrables)

• Actions
– Certaines: contexte déterministe (prédictible)
– Incertaines (adversaire)
Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Adverse-6

Autres exemples
• Morpion
• Jeux de plateau
– Othello
– Dames (Chinook)
– Echecs (DeepBlue)
– Go (AlphaGO)

• …

Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Adverse-7

Adversaire
On résout l’incertitude sur les choix de
l’adversaire en lui attribuant une stratégie de jeu
On fait les hypothèses :
• L’adversaire peut observer les mêmes états
que nous (pas d’information supplémentaire)
• L’adversaire joue en alternance avec nous
• L’adversaire veut gagner la partie (pire des cas)
• L’adversaire est cohérent dans sa stratégie
Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Adverse-8

Formulation: Jeux
On formule le problème comme une exploration
de l’espace des configurations
• Etats: Configurations de jeu
• Transition: choix d’une nouvelle configuration
contraint par les règles du jeu
• Etat initial: Configuration de départ et joueur
initial
• Etat final: égalité ou victoire d’un des joueurs
Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Adverse-9

Fonction d’utilité et recherche
Jeux à somme nulle:
• La fonction d’utilité mesure le résultat du jeu
– Gagnant +1
– Egalité: 0
– Perdant: -1

La recherche estime le meilleur coup à jouer (au
tour de notre joueur) pour maximiser l’utilité

Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Adverse-10

Exemple
Jeu du Morpion:
• Symboles X et O placés alternativement
• But: aligner 3 symboles identiques en ligne,
colonne ou diagonale
X

X

O

X

O

O

X

O

X

O

X

0

X

X

X

O
O

1

Stephane Marchand-Maillet – University of Geneva – Computer Science

X

O

O
O

X

-1

X

X

X

O

O

X

O

O

1

AI Adverse-11

Arbre de jeu (incomplet)

Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Adverse-12

Arbre de jeu (incomplet)
X

X

X

Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Adverse-13

Arbre de jeu (incomplet)
X

X

X

X

O

X
O

X O

Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Adverse-14

Arbre de jeu (incomplet)
X
X
X

X

O

O

X
X

X

X
O

X
O
X

X O

O

X

Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Adverse-15

Arbre de jeu (incomplet)
X X O
X

O
X

X

X

X
O

O

X

X
O

X
X

X
O

X
O

X

X

O
O

X

X O

O

O

X

Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Adverse-16

Arbre de jeu (incomplet)
X X O

X

X O

O

X

O

X
X
X

X

X
O

O

X

X
O

X
X

O

X

X

X

O

X

O

O

+1

X
O

O

X

X O

O

X

X
O

X

X

X

O

O

X

Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Adverse-17

Arbre de jeu (incomplet)
X X O

X

X O

O

X

O

X
X
X

X

X

O

X

X

X
O

X

X

X

O

X

X

O

O

+1

X
O

O

X

X O

O

X
O

X

X

-1
O

X

X O

O

X
O

O

X

X

O

O

X

Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Adverse-18

Arbre de jeu (incomplet)
X X O

X

X O

O

X

O

X
X
X

X

X

O

X

X

X
O

X

X

X

O

X

X

O

O

+1

O

X
O

O

X

X O

O

X
O

X

X

-1
O

X

X O

O

X
O

O

X

X

O

X

X

O

O

O

X

X

X

O

0

X

Impossible à développer en entier pour des jeux
non triviaux
Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Adverse-19

Fonction d’évaluation
Permet de guider notre stratégie pour le choix des
coups à jouer:
f(v): V  ℝ
 Estimation (numérique) du potentiel d’une
configuration (état) s=state(v) à mener à la
victoire (relativement aux autres états)
En général, une fonction des caractéristiques du jeu
(valeurs des pièces, nombres, position, …)
On cherche à MAXimiser f
Joueurs: MAX vs MIN
L’adversaire à MINimiser f
On peut ne pas développer l’arbre jusqu’à la
conclusion du jeu
Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Adverse-20

Exemple
Jeu du Morpion:

0

5

-1

1

-1

Fonction d’évaluation:
f(v) = (# lignes/colonnes/diagonales ouvertes pour MAX)
- (# lignes/colonnes/diagonales ouvertes pour MIN)

Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Adverse-21

Recherche avec horizon
On développe l’arbre avec un horizon de
profondeur limité (profondeur M):
Pour satisfaire des contraintes de mémoire,
ou de temps de recherche
Les feuilles de l’arbre ne sont pas décisives
(gagnant/perdant/égalité)
On calcule leur fonction d’évaluation f(v) et on
propage ces valeurs vers le haut
Algorithme MiniMax
Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Adverse-22

Algorithme MiniMax
On ne remonte pas simplement les valeurs le long
du chemin, on doit prendre en compte le fait que
l’on joue contre un adversaire:
• MAX cherche à maximiser la fonction d’évaluation
Il fera le choix du coup menant au maximum des
valeurs

• MIN cherche à minimiser la fonction d’évaluation
Il fera le choix du coup menant au minimum des
valeurs

On rétro-propage selon cette logique
Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Adverse-23

Exemple

(modulo symétries)

M=2

1
MAX joue
-1
1
MIN joue

-1

1

1
0

-2

1

2

1
-1

-1
0
-2
Stephane Marchand-Maillet – University of Geneva – Computer Science

0
AI Adverse-24

Algorithme MiniMax
En partant d’un nœud où MAX doit jouer:
1. Développer l’arbre jusqu’à la profondeur fixée
2. Evaluer f(v) pour toutes les feuilles v de cet arbre
3. Rétro-propager ces valeurs selon:
a. Un nœud où MAX doit jouer reçoit le maximum des
valeurs de ses enfants
b. Un nœud où MIN doit jouer reçoit le minimum des
valeurs de ses enfants

4. Jouer selon le chemin de la valeur remontée
Si f est une bonne estimation, on maximise nos chances
de victoire
On itère jusque ce qu’un nœud terminal (décisif) soit
accessible avec la profondeur fixée
Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Adverse-25

Propriétés
• Complet: oui si l’arbre de jeu est fini
• Optimal: oui si l’adversaire est aussi optimal
• Complexité en temps: O(bM)
– branchement moyen b
– Profondeur maximale M

• Complexité en espace: O(b.M)
– Recherche en profondeur

Exemple: Echecs
• b=35, novice: M=4, expert M=8
• Fonction d’évaluation complexe à déterminer
 On veut M=20 => 2.1030 coups à développer
 On doit réduire l’expansion de l’arbre
Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Adverse-26

Elagage a-b
Principe: ne plus développer les branches de l’arbre
correspondant aux coups sans intérêt (au sens MiniMax)
 Algorithme exact: trouve la même solution
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
Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Adverse-27

Elagage a-b
Principe: ne plus développer les branches de l’arbre correspondant aux
coups sans intérêt (au sens MiniMax)
 Algorithme exact: trouve la même solution
• a = max  ne peut que croître, ne peut pas décroître
– borne inférieure de la valeur finale

• b = min  ne peut que décroître, ne peut pas croître
– borne supérieure de la valeur finale
Max

a
Min

b

On interrompt la recherche au-dessous de v si:
• a(v)≥b(v’) avec v nœud MAX et v’ ancêtre de v
• b(v)≤a(v’) avec v nœud MIN et v’ ancêtre de v

Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Adverse-28

Exemple
MAX

a=-∞
MAX joue

MIN

MIN

b=+∞

1
MIN joue

-1

1

1
0

MIN

-2

1

2

1
-1

-1
0
-2
Stephane Marchand-Maillet – University of Geneva – Computer Science

0
AI Adverse-29

Exemple
MAX

a=-1
MAX joue

MIN

MIN

b=-1

1
MIN joue

-1

1

1
0

MIN

-2

1

2

1
-1

-1
0
-2
Stephane Marchand-Maillet – University of Geneva – Computer Science

0
AI Adverse-30

Exemple
MAX

a=-1
MAX joue

MIN

MIN

b=-1

1
MIN joue

-1

1

1
0

MIN

b=+∞

1

2

1
-1

-1
0
-2
Stephane Marchand-Maillet – University of Geneva – Computer Science

0
AI Adverse-31

Exemple
MAX

a=-1
MAX joue

MIN

MIN

b=-1

1
MIN joue

-1

1

1
0

MIN

b=-1

1

2

1
-1

-1
0
-2
Stephane Marchand-Maillet – University of Geneva – Computer Science

0
AI Adverse-32

Exemple
MAX

a=-1
MAX joue

MIN

MIN

b=-1

1
MIN joue

-1

1

1
0

MIN

b=-2

1

2

1
-1
On peut interrompre la
recherche pour ce nœud
car b ≤a et ne croîtra plus

-1
0
-2
Stephane Marchand-Maillet – University of Geneva – Computer Science

0
AI Adverse-33

Exemple
MAX

a=1
MAX joue

MIN

MIN

b=-1

b=1
MIN joue

-1

1

1
0

MIN

b=-2

1

2

1
-1

-1
0
-2
Stephane Marchand-Maillet – University of Geneva – Computer Science

0
AI Adverse-34

Exemple
MAX

a=1
MAX joue

MIN

MIN

b=-1

b=1
MIN joue

-1

1

1
0

MIN

b=-2

1

2

1
-1

-1
0
-2
Stephane Marchand-Maillet – University of Geneva – Computer Science

0
AI Adverse-35

Elagage a-b

Exercice: Marquer l’élagage (slide suivant)

On interrompt la recherche au-dessous de v si:
• a(v)≥b(v’) avec v nœud MAX et v’ ancêtre de v
• b(v)≤a(v’) avec v nœud MIN et v’ ancêtre de v
Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Adverse-36

Elagage a-b

On interrompt la recherche au-dessous de v si:
• a(v)≥b(v’) avec v nœud MAX et v’ ancêtre de v
• b(v)≤a(v’) avec v nœud MIN et v’ ancêtre de v
Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Adverse-37

Propriétés de l’élagage
Algorithme exact: on trouve la même solution que si on
developpait l’arbre complet
Le gain est maximum pour l’élagage a-b quand:
• Les enfants d’un nœud MAX sont ordonnés selon leur
valeurs décroissantes
• Les enfants d’un nœud MIN sont ordonnés selon leur
valeurs croissantes
Dans ce cas on a une complexité en temps O(bM/2) et un
facteur de branchement √b
Si l’ordre est quelconque on a un gain moyen et une
complexité O(b3M/4)
 Permet d’augmenter M: si MiniMax est faisable pour M=10
alors l’élagage permet M=13
Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Adverse-38

Alternatives & évolutions
• NegaMax: pas d’alternance des fonctions min
et max. Simplement une fonction évaluée à un
niveau dont on prend l’opposé au niveau
suivant

• ExpectMiniMax: permet de modéliser les jeux
dans lesquels un aléa est présent (exple:
backgammon)

Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Adverse-39

AlphaGO (b=360)
Stratégie différente: Reinforcement Learning
• Apprentissage d’une stratégie (Policy) qui lie
les actions a (coups à jouer) en fonction de
l’état s (configuration de jeu courante)
Pas d’exploration systématique
Modélisation locale du contexte a=f(s)

• Utilise des réseaux de neurones entraînés sur
des parties jouées contre un humain et contre
lui-même
Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Adverse-40

Résumé
• Jeu à 2 joueurs à somme nulle
Recherche adverse
Prise en compte de la stratégie adverse
Algorithme MiniMax
Elagage a-b
• Autres contextes pour la prise en compte de
l’aléa
• Alternative actuelles par apprentissage
Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Adverse-41

