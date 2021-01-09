Intelligence Artificielle
Satisfaction et Propagation de
Contraintes
Stéphane Marchand-Maillet

Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Contraintes - 1

Contenu
• Types de problèmes
• Représentation de contraintes
• Problèmes de Satisfaction de Contraintes
• Algorithmes de résolution

Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Contraintes - 2

Problème des k-reines
Problème:
Placer un maximum de reines (d’échec) sur
un échiquier de taille kxk sans qu’elles
s’attaquent entre elles

On peut en placer au maximum une seule par
colonne/ligne/diagonale  k-reines
R

Stephane.Marchand-Maillet – Université de Genève

X

R

X X

R

X

R

X

X

X

k=4

X
X
Intelligence Artificielle

AI Contraintes - 3

Problème de recherche (1)
• Etats S:
– Configurations de 0…k
reines sur l’échiquier

R

R
R

R
R

R

R

• Transitions G:
– s’∈G(s) si s’ affecte une reine de plus que s

• Etat initial sI:
– Echiquier vide

• Etat final sG:
– k reines sans attaque mutuelle

 k2!/(k2-k)! états
Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Contraintes - 4

Problème de recherche (2)
• Etats S:

R

– Configurations valides de
0…k reines sur l’échiquier

R
R

• Transitions G:

R

R

– s’∈G(s) si s’ affecte une reine de plus que s

• Etat initial sI:

– Echiquier vide

• Etat final sG:

– k reines sans attaque mutuelle

Beaucoup moins d’états
mais comment atteindre les états valides?
Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Contraintes - 5

Discussion
• On a des contraintes mutuelles:
– La position d’une reine contraint la position des
autres
– On veut satisfaire toutes les contraintes

• On va utiliser la propagation de contraintes:
– Pour réduire l’espace de recherche
– Déduire les états non-valides

• On peut utiliser des heuristiques:
– Pour favoriser les états valides
– Pour accélérer la recherche
Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Contraintes - 6

Représentation de contraintes
Un problème de satisfaction de contraintes (PSC)
est représenté par:
• Un ensemble de variables
X=(x1,…, xN)

chaque variable xi ayant un domaine de valeurs
admissibles Di (en général discret et fini)
• Un ensemble de contraintes sur les variables:
C = (c1,…, cM)

chaque contrainte cj est une proposition logique
(égalité, inégalité, …) qui s’applique sur les variables X
Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Contraintes - 7

Résolution de PSC
Solution: on cherche:
X* tel que xi* ∈ Di et True(cj) pour tout i, j
Un affectation valide est une affectation de certaines
variables dans leurs domaines et satisfaisant les contraintes
Une solution est une affectation valide affectant toutes les
variables
On va explorer (par recherche) l’espace des affectations
pour construire une solution au PSC
On doit définir une stratégie de recherche
Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Contraintes - 8

Exemple de PSC

R
R

k-reines:
• X=(xij)i,j=1..k valeurs binaires des k2 cases

• Domaines : Dij = {0,1} pour chaque i,j = 1…k

• Contraintes:
xij = 1 ⇒ xim = 0 for all m≠j
xij = 1 ⇒ xmj = 0 for all m≠i
xij = 1 ⇒ diagonales = 0
Σ xij = k
Stephane.Marchand-Maillet – Université de Genève

(contraintes binaires)
(contraintes binaires)
(contraintes binaires)
(contrainte multiple)
Intelligence Artificielle

AI Contraintes - 9

Exemple de PSC

R
R

k-reines (autre formulation) :
• X=(xi)i=1..k valeurs de ligne pour les k colonnes

1

2

3

4

• Domaines : Di = {1,…,k} pour chaque i = 1…k

• Contraintes:
xi = m ⇒ xj ≠m for all j≠i
(contrainte binaire)
De même pour les diagonales (contrainte binaire)

Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Contraintes - 10

Exemple (à construire)
Modéliser (Enigme d’Einstein):
On a 14 indices. Il y a cinq maisons, cinq hommes de nationalité et de professions différentes habitent avec leur
animal préféré cinq maisons de couleurs différentes où ils boivent leur boisson préférée.
1.
2.
3.
4.
5.
6.
7.
8.
9.
10.
11.
12.
13.
14.

L’Anglais habite la maison rouge.
L’Espagnol adore son chien.
L’Islandais est ingénieur.
On boit du café dans la maison verte.
La maison verte est située immédiatement à gauche de la maison blanche.
Le sculpteur possède un âne.
Le diplomate habite la maison jaune.
Le Norvégien habite la première maison à gauche.
Le médecin habite la maison voisine de celle où demeure le propriétaire du renard.
La maison du diplomate est voisine de celle où il y a un cheval.
On boit du lait dans la maison du milieu.
Le Slovène boit du thé.
Le violoniste boit du jus d’orange.
Le Norvégien demeure à côté de la maison bleue.

Questions:
•
•

Qui boit de l’eau ?
Qui élève le zèbre ?
Source: http://enigmesetdevinettes.com/enigme/enigme-einstein/

Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Contraintes - 11

Modélisation

• Variables?
• Domaines?
• Contraintes?
Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Contraintes - 12

Classification des PSC
• Le domaine de chaque variable est discret et
fini:
– Le PSC est fini
– La solution peut se trouver par recherche
• pire des cas: énumération

• Le domaine de certaines variables est infini:
– On ne peut pas énumérer les affectations
– Résolution similaire à la programmation linéaire

Dans ce cours, on ne traite que des PSC finis
Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Contraintes - 13

Rappel: Programmation linéaire
X=(xi)i=1..k , Di = ℝ pour chaque i = 1…k
cj : Σ aijxi + bj = 0
cj : Σ aijxi + bj ≤ 0

cj
cj

x2

solution

Stephane.Marchand-Maillet – Université de Genève

x1

Intelligence Artificielle

AI Contraintes - 14

Analogie
X=(xi)i=1..k , Di = {(discret fini)} pour chaque i = 1…k
cj : Σ𝑖 aijxi + bj = 0
cj : Σ𝑖 aijxi + bj ≤ 0

cj
cj

x2

solution

Stephane.Marchand-Maillet – Université de Genève

x1

Intelligence Artificielle

Photo non contractuelle (illustration)

AI Contraintes - 15

Graphe de contraintes
Si les contraintes sont binaires, les variables sont
liées 2 à 2:
On crée le graphe
G=(V,E)=(“variables”, “contraintes”)
• Les composantes connexes de ce graphe
représentent des groupes de variables liées
 On peut les traiter indépendamment
• On peut utiliser ce graphe pour suivre la
propagation de contraintes
Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Contraintes - 16

Exemple trivial
Coloration de graphe:
Etant donné un graphe, colorier les nœuds sans
que 2 nœuds voisins soient de la même couleur
• PSC: variables? domaines?
• Par définition un PSC binaire (couleurs de nœuds
différentes 2 à 2)
• Par définition soutenu par un graphe
• Si le graphe a des composantes connexes, on
peut les traiter indépendamment
Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Contraintes - 17

Coloration de graphe
A
E
C
B
G

F

D

Applications: coloration de carte, cooccurences, …, contraintes exclusives
Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Contraintes - 18

Recherche de solution
Espace d’états:
• Espace des affectations valides
Transition:
• Affecter une nouvelle variable en satisfaisant
les contraintes
Etat initial sI:
• Affectation vide (aucune variable affectée)
Etat final sG:
• Une solution
Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Contraintes - 19

Arbre de recherche (PSC)
Racine: Affectation vide (sI)

…
Affectation valide de m variables

N variables avec domaines de taille moyenne L:
 Facteur de branchement: b = (N-m).L

Affectation valide de m+1 variables
Affectation de la variable Affectation de la variable
xp à ses différentes
xp’ à ses différentes
valeurs admissibles
valeurs admissibles
comme m+1ème variable comme m+1ème variable

…

On obtient un facteur de branchement ingérable

Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Contraintes - 20

Commutativité des affectations
Remarque:
Une affectation valide ne dépend pas de
l’ordre dans lequel elle a été construite
Transition:
• Choix de une variable xp à affecter
• Affectation de xp à ses valeurs admissibles (Dp)
 Réduction du facteur de branchement
Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Contraintes - 21

Arbre de recherche (PSC)
Racine: Affectation vide (sI)

…
Affectation valide de m variables

Choix de la variable
xp à affecter

Affectation valide de m+1 variables
Affectation de la variable
xp à ses différentes
valeurs admissibles
comme m+1ème variable

On ne considère plus ces alternatives
(variables autres que xp) en parallèle

N variables avec domaines de taille moyenne L:
 Facteur de branchement: b = L
Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Contraintes - 22

Algorithme de Backtracking
PSC_BACKTRACKING(A: affectation)
1. Si A = sG alors retourner A
2. Sélectionner une variable xp non affectée
3. Pour chaque valeur vpi de Dp faire:

– Ajouter xp <- vpi dans A
– Si A est valide alors retourner PSC_BACKTRACKING(A)
sinon retourner “echec”

Appel: A <- PSC_BACKTRACKING(sI)
Note: 3. : on suppose un ordre sur les domaines Dp
Exercice: Ecrire la version itérative
Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Contraintes - 23

Exemple (3 variables)
{} = sI
x2 (D2 ={v21,v22,v23})
{x2=v21}
x1 (D1 ={v11,v12,v13})

On remonte (backtrack) pour changer
l’affectation de la variable précédente

{x1=v11, x2=v21}
x3 (D3 ={v31,v32,v33})
“Echec”: Pas d’affectation valide

Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Contraintes - 24

Exemple (3 variables)
{} = sI
x2 (D2 ={v21,v22,v23})
{x2=v21}
x1 (D1 ={v11,v12,v13})

{x1=v12, x2=v21}
x3 (D3 ={v31,v32,v33})
“Echec”

Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Contraintes - 25

Exemple (3 variables)
{} = sI
x2 (D2 ={v21,v22,v23})
{x2=v22}
x1

x3 (D3 ={v31,v32,v33})
{x2=v22, x3=v32}

x3

x1 (D1 ={v11,v12,v13})
{x1=v11, x2=v22, x3=v32} = sG

Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Contraintes - 26

Algorithme de Backtracking
PSC_BACKTRACKING(A: affectation)
1. Si A = sG alors retourner A
2. Sélectionner une variable xp non affectée
3. Pour chaque valeur vpi de Dp faire:

– Ajouter xp <- vpi dans A
– Si A est valide alors retourner PSC_BACKTRACKING(A)
sinon retourner “échec”

Aléa:
• Ordre d’affectation des variables (etape 2.)
• Ordre d’affectation des valeurs (etape 3.)
Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Contraintes - 27

Forward checking

X

• Affecter une valeur à une variable rend
invalides d’autres affectations (par les
contraintes)
On peut prédire les valeurs des variables
contraintes et éviter ces affectations
Exemple: (4-reines)
X

x1

x2

x3

x4

D

1234

1234

1234

1234

1

1234

1234

1234

1

4

1234

1234

1

4

2

1234

Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

R

X

X

X

X
X
x1=2

X

R
R

X
X

R

X

AI Contraintes - 28

Forward checking
• Lors de l’affectation d’une variable, on regarde
(en fonction des contraintes) l’impact sur les
domaines valides des autres variables nonaffectées
• On maintient les domaines valides de
l’affectation
• Cela permet de ne pas tester des affectations
invalides (boucle 3.)
 La vérification de validité de l’affectation est
faite a priori plutôt qu’a posteriori
Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Contraintes - 29

Backtracking adapté
PSC_BACKTRACKING(A: affectation, D: domaines)
1. Si A = sG alors retourner A
2. Sélectionner une variable xp non affectée
3. Pour chaque valeur vpi de Dp faire:
–
–
–

Ajouter xp <- vpi dans A
D  FORWARD_CHECKING(A, D)
Si aucun domaine de D n’est vide:
alors retourner PSC_BACKTRACKING(A, D)
sinon retourner “échec”

Appel: A <- PSC_BACKTRACKING(sI, D)
Note: 3. : on suppose un ordre sur les domaines Dp
Exercice: Ecrire la version itérative
Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Contraintes - 30

Heuristiques
On a toujours les aléas:
• Ordre d’affectation des variables (étape 2.)
– On diminue le facteur de branchement:
– Heuristique de la variable la plus contrainte…
• Variable ayant le plus petit domaine

…et la plus contraignante
• Variable apparaissant dans le plus grand nombre de
contraintes

• Ordre d’affectation des valeurs (étape 3.)
– Heuristique de la valeur la moins contraignante
• Valeur qui élimine le moins de valeurs aux autres
• Demande un forward-checking pour toutes les valeurs
Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Contraintes - 31

Heuristiques
Heuristique de la variable la plus contrainte et la
plus contraignante
Heuristique de la variable la moins contraignante
A

E

X
R

X

X

X
C

X
R

B

X

Nouvelle affectation
(variable la plus contrainte)

Stephane.Marchand-Maillet – Université de Genève

Nouvelle affectation
(valeur la moins contraignante)

Intelligence Artificielle

F
D

AI Contraintes - 32

Backtracking adapté (2)
PSC-BACKTRACKING(A: affectation, D: domaines)
1. Si A = sG alors retourner A
2. Sélectionner une variable xp non affectée
(heuristique sur les variables)
3. Pour chaque valeur vpi de Dp faire:
(heuristique sur la valeur)
– Ajouter xp <- vpi dans A
– D  FORWARD_CHECKING(A, D)
– Si aucun domaine de D n’est vide:
alors retourner PSC-BACKTRACKING(A, D)
sinon retourner “échec”

Appel: A <- PSC-BACKTRACKING(sI, D)
Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Contraintes - 33

Propagation de contraintes

B
C

Myopie du Forward Checking
A
F
X

A

B

C

D

E

F

D

rvb

rvb

rvb

rvb

rvb

rvb

v

rvb

rvb

rvb

rvb

rvb

v

rvb

b

rvb

rvb

rvb

v

r

b

rvb

rvb

rvb

D
E

Contradiction: B et F sont connectés et ont le même domaine
Echec au prochain pas
Le Forward Checking ne le détecte pas
On doit introduire une autre stratégie:
La propagation de contraintes
Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Contraintes - 34

Consistance
• Anticipation de 1 niveau: pour chaque variable xi
non-affectée dans A on élimine de Di toute valeur
v rendant l’ajout de (xi <- v) dans A inconsistante
avec C: 1-consistance (consistance de nœud)
• Anticipation de 2 niveaux: pour chaque variable xi
non-affectée dans A on élimine de Di toute valeur
v telle que pour (xi<-v), il existe une variable xj
non affectée pour laquelle aucune affectation
(xj<-w) ne serait 1-consistante : 2-consistance
(consistance d’arc)
• Anticipation de 3 niveaux: … 3-consistance
(consistance de chemin)
• …
Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Contraintes - 35

Algorithme AC3 (Arc Consistency, 1977)
C contient des contraintes binaires
AC3(D)
pour tout xp de X faire:
Q <- {xq t.q xp et xq sont liées par une contrainte de C}
répéter:
xq<- Q.pop()
// voisin de xp
si ELIMINER(xp,xq)
// garde les paires (vp, vq) admissibles
si Dp est non vide
// alors on propage sinon stop
alors ajouter dans Q tout xr diffèrent de xq et t.q xr et xq sont liées par
une contrainte de C
sinon retourner “échec”
Tant que Q est non-vide
retourner D
bool ELIMINER(x1,x2)
// maintien de la 2-consistance
changement <- faux
pour tout v1 de D1 faire:
chercher v2 de D2 pour satisfaire la contrainte sur x1 et x2

si cet ensemble est vide alors:
supprimer v1 de D1
changement <- vrai
retourner changement
Stephane.Marchand-Maillet – Université de Genève

// on enlève de D1 les valeurs menant à une contradiction

Intelligence Artificielle

AI Contraintes - 36

Propriétés de AC3
Algorithme de propagation de contraintes binaires
Complexité (opérations): O(N. mmax.L3) avec:

– N variables
– mmax contraintes impliquant une variable donnée
– L: tailles moyenne des domaines

La généralisation de AC3 à des contraintes impliquant plus que 2
variables induit une combinatoire sur les variables:
“chercher v2 de D2 pour satisfaire la contrainte sur x1 et x2”
devient pour (x1, x2, x3):
“chercher v2 de D2 et v3 de D3 pour satisfaire toute contrainte
sur (x1, x2) et (x2, x3) et (x1, x3)”
Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Contraintes - 37

Backtracking adapté (3)
PSC-BACKTRACKING(A: affectation, D: domaines)
1. Si A = sG alors retourner A
2. D <- AC3(D)
3. Si une variable a un domaine vide alors echec
4. Sélectionner une variable xp non affectée
(heuristique sur les variables)
5. Pour chaque valeur vpi de Dp faire:
(heuristique sur la valeur)
–
–
–

Ajouter xp <- vpi dans A
D  FORWARD_CHECKING(A, D)
Si aucun domaine de D n’est vide:
alors retourner PSC-BACKTRACKING(A, D)
sinon retourner “échec”

Appel: A <- PSC-BACKTRACKING(sI, D)
Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Contraintes - 38

Simplification de problème
Quand une variable reçoit une valeur par
backtracking, on peut propager cette valeur et
enlever la variable du graphe:
(r,v)

A
E

(r,v)

(r,v)

A

(r,v)

E

(r,v)

C
B

F

C

(r,v)

F

b
D (r,v)

Cela peut simplifier le graphe:
chaîne, arbre, composantes,…
Stephane.Marchand-Maillet – Université de Genève

(r,v)

(r,v)

D (r,v)
chaine => alternance de couleurs

Intelligence Artificielle

AI Contraintes - 39

Exemples (à développer)
A
x1 <- 1
AC3 => change rien
FC
AC3 => x2 ≠3, x3 ≠2, x3 ≠4
D2 vide => backtrack x1 <- 2
FC
AC3 => x2=4, x3=1, x4=3

E
C
B

F
D

4-reines (1,2,3,4)

Coloration (r,v,b)

6
6
6
6

6

6

6

+
F

T

W

O

T

W

O

O

U

R

(0,1,2,3,4,5,6,7,8,9)

Carré magique (1,2,3)
Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Contraintes - 40

Cas particuliers
• Graphes à multiples composantes connexes
– Autant de problèmes indépendants

• Arbre de contraintes
– On ordonne les contraintes de racine aux feuilles,
on assigne une valeur à la racine et on propage
vers le bas

Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Contraintes - 41

Résumé
• Tous les problèmes ne se formulent pas
directement comme une recherche
• La propagation de contraintes permet de
diriger la recherché de solutions
• Les problèmes à contraintes binaires
correspondent à un graphe
– On peut y revenir via l’ajoût de variables

• Ces algorithmes fonctionnent bien si les
contraintes ne sont pas trop entremêlées
(concernent chacune peu de variables)
– Lien avec la faisabilité en programmation linéaire
Stephane.Marchand-Maillet – Université de Genève

Intelligence Artificielle

AI Contraintes - 42

