Intelligence Artificielle
Naive Bayes
Régression Logistique
Stephane Marchand-Maillet

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI NaiveBayes -1

Contenu
• Naive Bayes
• Régression logistique

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI NaiveBayes -2

Rappel: Protocole d apprentissage
Données
(labélisées)
Entraînement

Test
Entrainement
E

T

Validation

Test
Entrainement
E

V

Validation croisée (cross-validation): on itère V comme étant une partie de E

V

Entrainement
E
Entrainement
E

Stephane Marchand-Maillet – University of Geneva

V

Intelligence Artificielle

Test
T
Test
Test
T
Test
T

AI NaiveBayes -3

Formellement
Données
(labélisées)

(xi,yi) i=1…N ∝ variables (X,Y)

Holdout
xi  yi ?
E

xi = [xik] ∈ X ⊆ ℝK
yi ∈ Y = {1 … C}

T

:
:

Stephane Marchand-Maillet – University of Geneva

Réel

Attributs des données de dimension K
Label (classe)

Intelligence Artificielle

AI NaiveBayes -4

Classification
Etant donné un ensemble de données (X)
labellisées (Y), on cherche à définir un
classifieur:
fq : X
Y
xi
fq (xi) =yi
(q : paramètres)

Exemple: Classification de fruits
• Attributs continus: diamètre, poids
• Attributs discrets: nombre de feuilles, couleur, forme
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI NaiveBayes -5

Rappel: Théorème de Bayes
likelihood prior
P A B P(B)
P BA =
P(A)
posterior
evidence

…tout en ayant un apriori
sur la présence de la cause
(indépendamment de l’effet)…

On place nos observations
sous l’hypothèse de la cause…

P effet cause P(cause)
P cause effet =
P(effet)
On cherche à savoir si la cause
est probable étant données nos observations

Exemples:

P maladie sympôme =

P symptôme maladie P(maladie)
P(symptôme)

Stephane Marchand-Maillet – University of Geneva

…et un apriori
sur la présence de l’effet
(indépendamment de la cause)

P magic in the air joie =

Intelligence Artificielle

P joie magic P(magic)
P(joie)
AI NaiveBayes -6

Classification Bayésienne
On cherche à transformer la
vraisemblance d’une donnée
dans une classe (observée)…

likelihood prior
P A B P(B)
P BA =
P(A)
posterior
evidence

… normalisée par la vraisemblance
de la classe…

P donnée classe P(classe)
P classe donnée =
P(donnée)
… en la vraisemblance de la classe
indiquée par la donnée

Stephane Marchand-Maillet – University of Geneva

…tout en ayant un apriori sur la
vraisemblance de la donnée
(indépendamment de toute classe)

Intelligence Artificielle

AI NaiveBayes -7

Classification Bayesienne
La classe estimée y~ est la plus vraisemblable:
On calcule P classe donnée = P(y~|x) pour
toutes les classes et on choisit celle qui réalise
le max
Formellement:
y~= argmax P(y|x)
y∈Y
 C est un classifieur optimal au sens où on ne
peut pas réduire l’erreur de classification
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI NaiveBayes -8

Classification Bayesienne
Souris
(non-pertinent)

Chat
(pertinent)

Cette partie est réduite à 0

TP

TN

Souris
(non-pertinent)
FN
Negatif

FP

Positif

Taille

Chat
(pertinent)

Optimal

TP

TN
FN

FP

Taille
Negatif

Positif

Non-optimal
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI NaiveBayes -9

Classification Bayesienne
y~= argmax P(y|x)
y∈Y
Etant donné x on cherche P(y|x)
Idéalement, grâce à l’ensemble d’entrainement on a
une LUT: x  y
Mais x est complexe (multidimensionnel x ∈ ℝK ) on
ne l’a probablement jamais observé
Exemple: x=pixels d’une image de chat, on doit
avoir déjà vu EXACTEMENT cette image (impossible)
 On doit trouver un moyen de généraliser
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI NaiveBayes -10

Approche Bayésienne
Par le théorème de Bayes:
P x y P(y)
P yx =
P(x)
La probabilité P(x) de chaque donnée est indépendante
de la classe , de plus on cherche l’argmax, pas la valeur
On ignore le dénominateur dans la maximisation
P y x ∝ P x y P(y)
y~= argmax P x y P(y)
y∈Y
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI NaiveBayes -11

Remarque: données équiprobables
On considère souvent que chaque échantillon xi
est unique et « échantillonable » équitablement.
Ce n’est pas forcément le cas..
Contre exemples:
• Urne avec des balles de matériaux différents:
Les plus légères sont favorisées dans un tirage
par le haut
• Population: on néglige le fait de personnes
« identiques » (jumeaux, triplés,…)
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI NaiveBayes -12

Classifieur Naive Bayes
et

P y x ∝ P x y P(y)
P(x|y) = P(x1, x2, …, xK|y)

Telle que, P(x|y) serait trop complexe à estimer. On
a besoin d’estimer toutes les relations entre les
caractéristiques
Par la règle produit:
P(x|y) = P(x1, x2, …, xK|y)
= P(x2, …, xK|x1,y) P(x1|y)
= P(xK|xK-1,…,x1,y) … P(x1|y)
= ςk P(xk|xk−1,…,x1,y). P(x1|y)
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI NaiveBayes -13

Classifieur Naive Bayes
On accepte l’indépendance conditionnelle des
attributs

Hypothèse: P(xk|xk−1,…,x1,y) = P(xk|y)
Les attributs sont conditionnellement (à y)
indépendants entre eux, alors:
P(x|y) = ෑ P(xk|xk−1,…,x1,y). P(x1|y)
k


k|y)
P(x|y) =ςK
P(x
k=1

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI NaiveBayes -14

Classifieur Naive Bayes
On a donc:

K
y~= argmax P(y) ෑ P(xk|y)
y∈Y
k=1
L’appartenance à la classe P(y|x) est une agrégation (produit)
d’indications d’appartenance à la classe par les attributs
P(xk|y)
Chaque classe porte sa signature par l’importance de chaque
attribut dans les données de cette classe
 Chaque attribut apporte son information (indépendante –
complémentaire) sur la décision d’appartenance à une
classe
 On estime la distribution de chaque attribut. On ne cherche
pas à séparer les attributs de chaque donnée
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI NaiveBayes -15

Rappel: Naive Bayes comme PGM

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

AI NaiveBayes -16

Estimation: Probabilité conditionelle
P(X, Y)
P XY =
P(Y)

Y=y

X=x

Données avec le label y
Données avec la caractéristique x

#(X=x ∧ Y=y)
Pest(X|Y)=
#(Y=y)

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI NaiveBayes -18

Classifieur Naive Bayes (estimation)
Attributs discrets:
On peut estimer sur le Training set E par une approche
fréquentiste:
|{xi t.q yi = y}|
P(y) =
|{xi}|
Exemple:
P(Y=pomme) = proportion de pommes dans E

k=xk et y = y}|
|{x
t.q
x
i
i
i
P(xk|y) =
|{xi t.q yi = y}|

Exemple:
P(jaune|pomme) = proportion de fruits jaunes parmi
les pommes dans E
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI NaiveBayes -19

Classification par Naive Bayes
Exemple:
10 fruits:
P(Pomme)=?
P(Citron)=?
P(Vert|Citron)=?

Stephane Marchand-Maillet – University of Geneva

Couleur

Taille

Fruit

Jaune

Moyen

Pomme

Rouge

Moyen

Pomme

Jaune

Moyen

Citron

Vert

Moyen

pomme

Vert

Petit

citron

Jaune

Moyen

Pomme

Vert

Gros

Pomme

Rouge

Petit

Pomme

Jaune

Moyen

Citron

Vert

Moyen

pomme

Intelligence Artificielle

AI NaiveBayes -20

Naive Bayes: Modèle Gaussien
Attributs continus:
Au lieu de quantifier les attributs, on considère
un modèle gaussien pour la valeur de chaque
attribut xk dans la classe y

 On estime les paramètres (moyenne,
variance) de chaque attribut dans sa classe
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI NaiveBayes -21

Classification par Naive Bayes
Du fait de l’indépendance, les axes
principaux sont parallèles aux axes

Y=1

Y=0

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI NaiveBayes -22

Classification par Naive Bayes
Y=1

Y=0

On estime la distribution de chaque attribut.
On ne cherche pas à séparer les attributs de
chaque donnée
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI NaiveBayes -23

Classification par Naive Bayes
On cherche à classifier un objet x=[xk] dont on connait
(observe) les attributs.
On peut calculer P(xk|y) selon la valeur (ou la présence
binaire) de chaque attribut grâce au modèle entrainé
sur les données
On estime
𝐾

y~= argmax P(y) ෑ
P xk y
𝑘=1
y∈Y
En pratique on ne multiplie pas les probabilités:
𝐾

y~= argmax log P(y) + ෍ log P xk y
y∈Y
𝑘=1
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI NaiveBayes -24

Classification par Naive Bayes
D autres modèles sont possibles pour les
densités de probabilités des attributs selon leurs
caractéristiques (histogramme, multimomiale,…)
Chaque modèle donne des propriétés
particulières au classifieur Naive Bayes
Exemple: le classifieur est linéaire si les distributions
sont de la famille exponentielle (par ex.
Gaussiennes) – cf plus loin

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI NaiveBayes -25

Régression Logistique

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI NaiveBayes -26

Régression Logistique
Soit une variable binaire Y suivant une
distribution de Bernoulli et soit X une
caractéristique de prediction pour la variable Y,
P(Y=1|x) = p
P(Y=0|x) = 1-p
on collecte les données (xi,yi)
Y
1

0
Stephane Marchand-Maillet – University of Geneva

X
Intelligence Artificielle

AI NaiveBayes -27

Régression Logistique
Si X est un bon prédicteur de Y on peut espérer
“binariser” X avec le seuil x0 (seuil de
prédiction):
yi = (xi<x0)

Y=

1

(X<x0)

Y
1

0
Stephane Marchand-Maillet – University of Geneva

x0
Intelligence Artificielle

X
AI NaiveBayes -28

Régression Logistique
A cause du bruit (et de la qualité du prédicteur)
on a une zone de recouvrement (plus ou moins
importante) dans les labels des données

Y
1

0
Stephane Marchand-Maillet – University of Geneva

x0
Intelligence Artificielle

X
AI NaiveBayes -29

Régression Logistique
Avec suffisamment de données, on agrège les
statistiques

P(Y=1|x)
1

0
Stephane Marchand-Maillet – University of Geneva

x0
Intelligence Artificielle

X
AI NaiveBayes -30

Régression Logistique
On fait une régression avec une version lissée de la
fonction indicatrice: la fonction logistique
1
q=[a,x ]
P Y = 1|x = fq(x) =
1 + e−a(x−x0)
0

P(Y=1|x)
1

0
Stephane Marchand-Maillet – University of Geneva

x0
Intelligence Artificielle

X
AI NaiveBayes -31

Fonction logistique
1

fq(x) = 1+e−a(x−x0)

a

x0

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI NaiveBayes -32

Régression Logistique
On fait une régression avec une version lissée de la
fonction indicatrice: la fonction logistique
1
q=[a,x ]
P Y = 1|x = fq(x) =
1 + e−a(x−x0)
0

P(Y=1)
1
(ici a<0)

0.5

0
Stephane Marchand-Maillet – University of Geneva

x0
Intelligence Artificielle

X
AI NaiveBayes -33

Régression logistique
𝑃 𝑌 = 1 𝑥 = fq(x) =

1

1 + 𝑒 −𝑎(𝑥−𝑥0)

𝑃(𝑌 = 1|𝑥)
⇒ log
= 𝑎(𝑥 − 𝑥0 )
𝑃(𝑌 = 0|𝑥)
Preuve:
p=

1
1 + 𝑒 −𝑎(𝑥−𝑥0)

𝑒 𝑎(𝑥−𝑥0)
⇒ p = 𝑎(𝑥−𝑥 )
0 +1
𝑒

𝑝
𝑝
𝑎(𝑥−𝑥0 )
⇒
=𝑒
⇒ log
= 𝑎(𝑥 − 𝑥0 )
1−𝑝
1−𝑝
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI NaiveBayes -34

Soit une variable binaire Y suivant une
distribution de Bernoulli et soit X une
caractéristique de prediction pour la variable Y,
P(Y=1|x) = p
P(Y=0|x) = 1-p

On appellee rapport de vraisemblance (odds
ratio) le rapport:
𝑂 𝑌=1𝑥 =

Stephane Marchand-Maillet – University of Geneva

𝑃(𝑌=1|𝑥)
𝑃(𝑌=0|𝑥)

Intelligence Artificielle

=

𝑝
1−𝑝

AI NaiveBayes -35

Régression logistique
On a donc:
Log O(Y=1|x)=a(x-x0)

Pour la regression on part donc de l’hypothèse que
le rapport de vraisemblance du label (Y) a une
relation log-linéaire avec la variable de prédiction
(X)
C’est le principe “le plus, le mieux”
La régression cherche à estimer q=[a,x0]
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI NaiveBayes -36

Analyse multidimensionnelle
P Y=1 x =𝜙𝜃 x

fq(x) =

K
⇒ log O Y=1|x =b+ ෍ ak xk
k=1

1
𝑻

1 + e−𝐚

(𝐱−𝐱0 )

Rappel en 1D

θ=[b,(ak )]

Exemple:

(x𝑘0 )

Tache réussie = fq(age, durée d’apprentissage)
durée
1

0
âge
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI NaiveBayes -37

Analyse multidimensionnelle

fq(x) =

1
𝑻

1 + e−𝐚

(𝐱−𝐱0 )

0.5

fq=0.5

Equivalent à une classification linéaire multidimensionnelle
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI NaiveBayes -38

Rappel: Classification linéaire

aTx+b=0

a
aTx+b>0

aTx+b<0

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI NaiveBayes -39

Regression logistique et Naive Bayes
P x Y=1 P Y=1
P Y=1 x = P x Y=1 P Y=1 +P x Y=0 P Y=0
1
1
=
=
P x Y=1 P Y=1
P x Y=0 P Y=0
−log
1+
P x Y=0 P Y=0
P x Y=1 P Y=1
1+e

Naive Bayes:

or

P x Y=1 P Y=1
log P x Y=0 P Y=0

P 𝑥 𝑘 Y=1
P Y=1
=
+
log
P Y=0
P 𝑥 𝑘 Y=0
indépendance
σ𝐾
𝑘=1 log

(𝑥𝑘 −𝜇)2

1 −
= 𝑒 2𝜎2
𝑍

Si de plus le modèle est Gaussien P(xk|Y)
pour chaque caractéristique alors on
peut trouver q=[a,b] tels que:
P Y=1 x =𝜙𝜃 (𝒙)
Soit:
K
log O Y=1|x =b+ ෍ ak xk = 𝑎𝑇 𝑥 + 𝑏
k=1
Naive Bayes avec modèle Gaussien est un classifieur linéaire (aussi vrai pour d’autres
modèles de la famille exponentielle)
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI NaiveBayes -40

Estimation de paramètres
Essentiellement formulée comme une
minimisation d’erreur puis descente en gradient
Par exemple:
https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html
et aussi: https://scikit-learn.org/stable/modules/naive_bayes.html

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI NaiveBayes -41

Résumé
• La classification Bayésienne choisit le label de plus forte probabilité
étant la donnée
• Le classifieur Naive Bayes diminue la complexité en faisant
l’hypothèse d‘indépendance conditionnelle des caractéristiques
• Un modèle est place sur chaque caractéristique et appris en
fonction des caractéristiques des données d’entrainement
• La régression logistique cherche une fonction logistique qui se colle
au mieux aux données
• La régression logistique est équivalente à une classification linéaire
• Naive Bayes correspond à une régression logistique si le modèle des
caractéristique est Gaussien (ou multinomial, famille
exponentielle…)
 La régression logistique permet d’estimer un classifieur Bayésien
sans estimer le modèle des caractéristiques explicitement
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI NaiveBayes -42

