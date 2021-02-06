Intelligence Artificielle
Modèles de graphes pour les probabilités
Probabilistic Graphical Models
Stéphane Marchand-Maillet

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI PGM 1

Contenu
Rappel: notions fondamentales
Probabilistic Graphical Models (dirigés/discrets)
Indépendance conditionnelle
Flot d information

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI PGM 2

Rappel: Notions fondamentales
• Probabilité jointe:

P(A∩B)=P(A,B)
P((X=x)ꓥ(Y=y))=P(x,y)
P(A,B)
• Probabilité conditionnelle:
P BA =
P(A)
P((X=r)|(Y=u1))=P(r|u1)
• Règle de produit:
• Règle de la somme:
• Indépendance:

P(X,Y)=P(X|Y)P(Y)
P(X)=Sy P(X,Y=y) (marginalisation)
P(A,B)=P(A)P(B)
P((X=x)ꓥ(Y=y)) = P(X=x)P(Y=y)

– On note X⊥Y (en fait X Y)
– Contre exemple: P((X=r)ꓥ(Y=u1)) ≠ P(X=r)P(Y=u1)
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI PGM 4

(Probabilistic) Graphical Models
Principe général: on utilise les graphes pour organiser les
relations
Ici: on modélise les relations de dépendances
(indépendance) probabiliste entre variables aléatoires
Exemple: soient 2 variables aléatoires X et Y non
temporalité
indépendantes:
P(X,Y)=P(Y)P(X|Y)
On notera:

Y

X
« temporalité »
flot d’information

Note: on peut aussi avoir des relations non-dirigées
(pas/peu abordé dans ce cours)
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI PGM 5

(Probabilistic) Graphical Model
Sur cette idée on peut définir un Probabilistic Graph Model
(PGM):
Soit un ensemble de variables aléatoires V={X1,…,XN}
Soit G=(V,G) un graphe construit sur V, où G(Xi)⊆V contient
les variables dépendantes de Xi
alors la probabilité jointe P(X1,…,XN) se factorise selon G si
elle s’exprime selon le produit:
N

P X 1 … X N = ෑ P X i X γi

∀Xi ∈ V

i=1

avec Xgi=G-1(Xi), les parents de Xi dans G
Les termes P Xi Xγi sont les modèles probabilistes
« locaux » correspondant aux distributions de probabilités
conditionnelles (Conditional Probability Distribution, CPD)
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI PGM 6

Exemple
V={X1,X2}
X1 = « Choix d’une urne (u1,u2) »
X2 = « Tirage d’une balle (r,b) »

G(X1)= {X2}
G(X2)= Ø

G-1(X1)= Ø =Xg1
G-1(X2)={X1}=Xg2

X1

X2

2

P X 1 , X 2 = ෑ P X i X γi
i=1

= P X 1 X γ1 P X 2 X γ2
⇒ P X1 , X2 = P(X1 )P X 2 X1
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI PGM 7

Modèles locaux / CPD
X1

X2

X1

X1

u1

u2

P(X1)

0.6

0.4

P(X2|X1)

X2=r

X2=b

X1=u1

0.6

0.4

X1=u2

0.6

0.4

ou

ou
Variable binaires:
On a des tables de taille 2k+1
avec k le nombre de parents
d’une variable

X2
P(X3|X1,X2)

X1=T

X3

Stephane Marchand-Maillet – University of Geneva

X1=F

X2=T

X2=F

X2=T

0.5

0.5

X2=F

0.6

0.4

X2=T

0.7

0.3

X2=F

0.1

0.9

ou

Intelligence Artificielle

AI PGM 8

Notation complémentaire
• Si on observe une variable aléatoire (p.ex si
elle fait partie de l’ensemble d’entrainement),
elle devient fixe (déterministe)
Noeud grisé
X

• Si une variable est composée de variables
(composantes) indépendantes
Y

Y

Y

X=(X1,…XK)
(indépendantes)

X

X1

X2

…

XK

Xi
i=1…K

Plate Notation
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI PGM 9

(Probabilistic) Graphical Model
PGM:
• Si on détecte des indépendances entre les variables (ce
qui est en général le cas), on réduit k (le degré maximal
du graphe) et donc la complexité (volume) des calculs
et représentations.
• Le PGM rend lisible le modèle en affichant les
indépendances et une forme de temporalité (flot
d’information) entre les variables (représentant les
paramètres ou concepts du problème)
 Le PGM introduit/capture une sémantique dans la
modélisation et permet une meilleure
abstraction/compréhension (voire simplification) de ces
modèles
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI PGM 10

Exemple

”Graphical model of Senate voting 2004-2006”
https://people.eecs.berkeley.edu/~elghaoui/StatNews/ex_senate.html

(non-orienté)
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI PGM 11

Exemple

*
*student admission test

(orienté, DAG = réseau Bayésien)
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI PGM 12

« Contre » exemple
Graphe complet:
Par l’application successive de la règle du produit on a:
P(W,X,Y,Z) = P(W).P(X,Y,Z|W) = P(W).P(X|W).P(Y,Z|X,W)
P(W,X,Y,Z)= P(W).P(X|W).P(Y|X,W).P(Z|W,X,Y)
Table 2(N-1)+1=2N
W

X

W

X

=
Y

Z

Y

P(W,X,Y,Z)
Stephane Marchand-Maillet – University of Geneva

W

X

Y

Z

Z
P(W).P(X|W).P(Y|X,W).P(Z|W,X,Y)
Intelligence Artificielle

AI PGM 13

Attention: Arbre de décision
Un arbre de décision représente une séquence de décisions et leurs
branchements possibles
A

B
P(B,A)

P(¬B,A)
Ceci est une énumération!!
(donc different)
P(B, ¬A)

P(¬B, ¬A)

• La probabilité d’un nœud est le produit des probabilités le long du
chemin
• L’arbre n’est pas forcément binaire
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI PGM 14

Configuration
Chaine de Markov (head-to-tail)
X

Y

Z

P(X,Y,Z)=P(X)P(Y|X)P(Z|Y)
P X, Y, Z
P X P Y X P(Z|Y)
⟹ P(Z|X,Y)=
=
P X, Y
P X P(Y|X)
P(Z|X,Y)=P(Z|Y)
 Z est indépendant de X sachant Y
(X ꓕ Z)|Y mais pas (X ꓕ Z)|Ø
 indépendance conditionnelle

 La variable observée «bloque» l’information entre X et Z
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI PGM 15

Independence conditionnelle
X

Dans le cas général:
P(X,Y,Z)=P(X)P(Y|X)P(Z|X,Y)
ou:
P(X,Y,Z)=P(Y)P(X|Y)P(Z|X,Y)

Y

Z
X

Y

Z

Si on observe X (par exemple)
X
Y

P(X,Y,Z)=P(X)P(Y|X)P(Z|X)

X
Z

Stephane Marchand-Maillet – University of Geneva

Y

Z

Intelligence Artificielle

(Y ꓕ Z)|X

AI PGM 16

Configuration
Chaine de Markov (head-to-tail)
X

Y

Z

P(X,Y,Z)=P(X)P(Y|X)P(Z|Y)
P(X,Z)= SyP(X,Y,Z) = SyP(X)P(Y|X)P(Z|Y) ≠ P X P(Z)
Rappel: P(X,Z|Y) = P(X|Y) P(Z|Y)
 Z n’est indépendant de X en général (si Y n’est pas observé)
(X ꓕ Z)|Y mais pas (X ꓕ Z)|Ø
(la présence d’un «chemin» indique une dépendance)
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI PGM 17

Configuration
« Cause commune » (tail-to-tail)
Variable latente/cachée

Z
X

Y

P(X,Y,Z)=P(Z)P(X|Z)P(Y|Z)

P(X,Y) = SzP(X,Y,Z) = SzP(Z)P(X|Z)P(Y|Z) ≠ P X P(Y)
 X n’est pas indépendant de Y en général
(X ꓕ Y)|Ø
(on trouve un «chemin» entre X et Y)
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI PGM 18

Configuration
« Cause commune » (tail-to-tail)

Variable latente/cachée

Z
X

Y

P(X,Y,Z)=P(X|Z)P(Y|Z)
P X, Y, Z
P Z P X Z P(Y|Z)
⟹ P(X,Y|Z)=
=
P Z
P Z
P(X,Y|Z)=P(X|Z) P(Y|Z)

 X est indépendant de Y sachant Z
(X ꓕ Y)|Z mais pas (X ꓕ Y)|Ø
indépendance conditionnelle
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI PGM 19

Configuration
« Structure en V» (head-to-head)
X

Y
Z

P(X,Y,Z)=P(X)P(Y)P(Z|X,Y)
=1

⟹ P(X,Y)=SzP(X)P(Y)P(Z|X,Y) = P X P(Y) SzP(Z|X,Y)
⟹ P(X,Y)=P X P(Y)
 X est indépendant de Y : (X ꓕ Y)|Ø
(malgré le «chemin» entre X et Y!!)
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI PGM 20

Configuration
« Structure en V» (head-to-head)
X

Y
Z

P(X,Y,Z)=P(X)P(Y)P(Z|X,Y)
P X, Y, Z
P X P(Y)P(Z|X, Y)
⟹ P(X,Y|Z)=
=
P Z
P Z
⇒ P(X,Y|Z) ≠ P(X|Z) P(Y|Z)
 X n’est pas indépendant de Y sachant Z : (X ꓕ Y)|Z
(idem si on observe un descendant de Z – à prouver)
 Notion de couverture Markovienne (Markov blanket)
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI PGM 21

Exemple
pieces
X

p

f

p

f

Y

p

f

f

p

Z

V

F

F

F

X

Y
Z

pile/face

pile/face

2x pile?
vrai/faux

Les 2 pieces sont indépendantes (en general – en ignorant Z)
Supposons Z connu/observé (Z = Faux par exemple):

Z=F 

P(X=p) = 1/3
P(Y=p) = 1/3
On observe X:
Z=F
X=p  P(Y=p)=0
X=f
 P(Y=p)=1/2
Stephane Marchand-Maillet – University of Geneva

X a complètement expliqué Y
“X explained away Y”
 Y devient inutile (déterministe)
Intelligence Artificielle

AI PGM 22

Flot d’information (D-separation)
X

Y

Z

X

Y

(X ꓕ Z)|Ø

(X ꓕ Z)|Y

Z

Z

X

Y

X

Y
(X ꓕ Y)|Z

(X ꓕ Y)|Ø
X

Z

Y

X

Y

Z

Z

(X ꓕ Y)|Ø

(X ꓕ Y)|Z

X

Y
Z
W

 Théorie de la D-separation (direct separation)
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

(X ꓕ Y)|W
AI PGM 23

Markov blanket
Def: La couverture Markovienne de X est le plus
petit sous-graphe contenant X tel que X est
conditionnellement indépendant des autres
variables si on observe les nœuds de ce sousgraphe
Enfants de X
X
Y
Z
X
X

Z

Y
X

Y

Z

Parents de X
Autres parents des enfants de X

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI PGM 24

Moral graph (“fermeture probabiliste”)
C’est le graphe G=(V,E’) tel que:
X,Y ∈E ′ ⟺ X est dans la couverture
Markovienne de Y

Le moral graph est utilisé pour l’inférence
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI PGM 25

Application: Naive Bayes

Y

Y

Y

X=(X1,…XK)
(indépendantes)

X

X1

X2

…

XK

Xi
i=1…K

P(X,Y) = P(Y)P(X|Y) = P(Y) PkP(Xk|Y)

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI PGM 26

Résumé
Les modèles de graphes pour les probabilités permettent de
modéliser l’indépendance
(C’est l’absence de relation qui donne l’indépendance – pas la
réciproque)
L’indépendance conditionnelle n’est pas l’indépendance en
général
L’indépendance conditionnelle est garantie pour tout nœud hors
de la couverture Markovienne d’une autre nœud (par définition)
 Simplifie les calculs d’inférence
 Application (directe) aux Réseaux Bayésiens
Les GPM peuvent ne pas être orientés (HMM, CRF,…)
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI PGM 27

