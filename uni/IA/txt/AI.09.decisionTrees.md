Intelligence Artificielle
Arbres de Décision
Stephane Marchand-Maillet

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI DT-1

Contenu
• Partition et arbre de décision
• Algorithmes d’apprentissage (ID3, CART)
• Regression Tree
• Random Forest

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI DT-2

Partition et arbre de décision
Humidité

?

Température
Données annotées (Décision: vert/rouge)
 Contexte supervise (données+label)
 On veut prédire le résultat en fonction de conditions
Exemple:
• Temperature
• Humidité
 J’observe ce specimen d’oiseau (oui/non)
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI DT-3

Partition et arbre de décision
Humidité

?

Température
Données annotées (Décision: vert/rouge)
 Contexte supervise (données+label)
 On veut prédire le résultat en fonction de conditions
Exemple:
• Temperature
• Humidité
 J’observe ce specimen d’oiseau (oui/non)
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI DT-4

Partition et arbre de décision

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI DT-5

Partition et arbre de décision

Condition sur une combinaison de
Température et Humidité
aT+bH<g

Une division binaire correspond à un choix de branche dans un arbre binaire

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI DT-6

Partition et arbre de décision

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI DT-7

Partition et arbre de décision

OK

Stephane Marchand-Maillet – University of Geneva

OK

OK

Intelligence Artificielle

OK

OK

AI DT-8

Partition et arbre de décision

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI DT-9

Partition et arbre de décision

?

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI DT-10

Partition et arbre de décision

Exercice: Créez l’arbre de décision correspondant

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI DT-11

Partition et arbre de décision

?

Toujours une approximation de notre fonction de décision

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI DT-12

Arbre de décision et propositions
Exercices:
•
Factoriser l’expression en vous aidant de l’arbre
•
Ecrire l’expression pour non

?

Oui = (AꓥBꓥC)ꓦ(Aꓥ¬BꓥDꓥE)ꓦ(Aꓥ¬Bꓥ¬D)ꓦ(¬AꓥFꓥGꓥI)ꓦ(¬AꓥFꓥ¬GꓥJ)ꓦ(¬Aꓥ¬FꓥH)
 Construire un arbre = construire des expressions logiques (décisions)
 Défi: réduire la longueur des propositions (en moyenne)  profondeur de l’arbre
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI DT-13

Rappel: Mesurer l’information
Entropie d’une variable X à valeurs (discretes) dans W:

H X = − ෍ P X=x log2 P(X=x)
x∈Ω
• Maximum quand les évenements sont equiprobables
• Minimum si le choix est deterministe (1 seul évènement)
 Mesure d’information (en bits de surprise)
Entropie conditionnelle:

H X|Y =− ෍ P Y=y ෍ P(X=x|Y=y) log2 P(X=x|Y=y)
y∈ΩY
x∈ΩX
 On énumère les combinaisons
Gain d’information:
I(X;Y) = H(X)-H(X|Y) = H(Y)-H(Y|X)
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI DT-14

Construction d’un arbre de décision
Etant données des données représentées par leurs caractéristiques et
la decision induite…
…on cherche à partitionner l’ensemble de données par des decisions
sur les caractéristiques…
…de telle façon que les sous-ensembles soient d’entropie minimale.

Le but est de construire un arbre pour décider sur une situation à venir
Exemple:

Jour

Température

Humidité

Oiseau visible?

J1

Moyenne

Forte

Oui

J2

Elevée

Faible

Oui

J3

Basse

Forte

Non

J4

Gel

Faible

Oui

J5

Basse

Moyenne

Non

J6

Elevée

Forte

Oui

J7

Moyenne

Moyenne

Non

Température Moyenne, Humidité Faible  oui/non?
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI DT-15

Contexte d’apprentissage

Faible

Moyenne

Forte

Humidité

Température
Gel

Très basse

Basse

Moyenne

Elevée TrèsElevée

Contexte d’apprentissage:
• Données quantifiées

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI DT-16

Partition et arbre de décision

Faible

Moyenne

Forte

Humidité

Température
Gel

Très basse

Basse

Moyenne

Elevée TrèsElevée

Contexte d’apprentissage:
• Données quantifiées
• Décisions univariées (par paramètre) type:
si Température = “élevée” alors …
•  Partition parallèle aux axes
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI DT-17

Partition et arbre de décision

Faible

Moyenne

Forte

Humidité

Gel

Très basse

Basse

Moyenne

Elevée TrèsElevée

Toujours une approximation de notre fonction de décision

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI DT-18

Algorithme ID3 (Iterative Dichotomiser 3, Quinlan 1986)
• Algorithme type glouton (greedy) pour la
construction d’arbres de décision
• Utilise un critère récursif de partition basé sur le
gain d’information maximum
ID3(W)
1. Soit W les données et H(X) l’entropie de la
variable associée
2. Partitionner W= W1UW2 (créer les sous-arbres)
selon la caractéristique C telle que le gain
d’information I(X;C) soit maximum
3. Soient Xi les restrictions de W à Wi
a. Si H(Xi)>0 alors ID3(Wi)
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI DT-19

Exemple (h(x)= −xlog2 x)
4

T

H

O

3

H(O)=ℎ
+ℎ
~0.98
7
7
H(O|?)=SP(?)SP(O|?)log2P(O|?)
Gain: I(O;?) = H(O)-H(O|?)
1ère décision:
Température: ([J4];-)(-;[J3,J5])([J1];[J7])([J2,J6];-)(-;-)
1
1
2
2
2
1
1
2
2
H(O|T)=7 ℎ 1 + 7 ℎ 2 + 7 ℎ(2) + ℎ(2) + 7 ℎ(2)
~0.28
Humidité: ([J2,j4];-)(-;[J5;J7])([J1,J6];[J3])
2
7

H(O|H)= ℎ

2
2

2

2

3

2

1

+ ℎ
+ ℎ( ) + ℎ( )
7
2
7
3
3
~0.39
 Gain: I(O;T) > I(O;H)
 Température réduit le plus l’entropie…
 2ème décision: Humidité…
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

Exercices:
• Créez les arbres de decision
• Implémentez l’algorithme
AI DT-20

Exemple 2: Données
Day

Outlook

Temperature

Humidity

Wind

Play?

D1

Sunny

Hot

High

Weak

No

D2

Sunny

Hot

High

Strong

No

D3

Overcast

Hot

High

Weak

Yes

D4

Rain

Mild

High

Weak

Yes

D5

Rain

Cool

Normal

Weak

Yes

D6

Rain

Cool

Normal

Strong

No

D7

Overcast

Cool

Normal

Strong

Yes

D8

Sunny

Mild

High

Weak

No

D9

Sunny

Cool

Normal

Weak

Yes

D10

Rain

Mild

Normal

Weak

Yes

D11

Sunny

Mild

Normal

Strong

Yes

D12

Overcast

Mild

High

Strong

Yes

D13

Overcast

Hot

Normal

Weak

Yes

D14

Rain

Mild

High

Strong

No

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI DT-21

Premières itérations
Données H(X) = 0.940
Sunny

Overcast

Rain

Gain

Weak

Strong

Gain

0.971

0

0.971

0.247

0.811

1.0

0.048

Hot

Mild

Cold

Gain

High

Normal

Gain

1.0

0.911

0.811

0.029

0.985

0.592

0.15

 Racine = “Outlook”
 Branche Sunny:
High

Normal

Gain

Weak

Strong

Gain

0

0

0.971

0.918

1.0

0.019

Hot

Mild

Cold

Gain

0

1

0

0.57
Exercice: Faire les calculs restants

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI DT-22

Arbre correspondant
Outlook
Sunny

Rain
Overcast

Yes

Humidity

Wind

D: 3,7,12,13

High

Strong

Normal

No

Yes

No

D: 1,2,8

D: 9,11

D: 6,14

Weak

Yes
D: 4,5,10

Exercice:
•
Ecrire l’expression logique pour Yes

Outlook= Rain, Humidity=High, Temperature=Cool, Wind=Strong  No

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI DT-23

Algorithmes C4.5 et C5.0 (Quinlan)
C4.5 modifie ID3 pour:
• Gérer des valeurs continues
 Un seuil adaptatif est créé pour diviser les données à
chaque pas.
Exemple: Température et Humidité non quantifiées
• Autres propriétés: élagage, mesures manquantes, mesures
avec pondérations
 C’est celui généralement utilisé
C5.0 modifie C4.5 pour l’efficacité:
• Rapidité, consommation mémoire
• Arbres plus réduits
• Autres propriétés (Boosting, etc)
 Produit commercial
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI DT-24

Rappel: Evaluation
On doit être capable de quantifier la qualité de
l’apprentissage:
On définit des mesures d’évaluation
Réalité

Prédiction
Positif

Négatif

Pertinent

Vrai Positif (TP)

Faux Négatif (FN)

Non-pertinent

Faux Positif (FP)

Vrai Négatif (TN)

Réalité

Prédiction
TN

FN
Pertinent

TP

FP
Positif

Données
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI DT-25

Rappel: Evaluation
• Taux d’erreur (Error Rate):

FP+FN
ER=TP+TN+FP+FN

– Potentiellement normalisé par la taille des classes
P(erreur|paramètres q)

• Précision/Rappel (information retrieval)
TP
P=
TP+FP

TP
R=
TP+FN

 mAP: mean Average Precision

• F1 score:

2PR
F1 =
P+R

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI DT-26

Evaluation
Si on atteint le niveau de l’arbre ou le critère de partition est 0
(et que les données d’entrainement sont cohérentes), l’erreur
d’entrainement est nulle (par définition)
Si les données de test sont cohérentes avec l’entrainement on
aura une erreur de test nulle aussi
Par contre:
• Complexité élevée
• Risque de sur-apprentissage

 On peut utiliser les données et l’évaluation pour introduire
formellement une tolérance (dans l’erreur d’entrainement)
pour garantir une simplicité de l’arbre (principe de parcimonie
du modèle) – cf pruning
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI DT-27

Algorithme CART
CART (Classification And Regression Tree)
• Proposé indépendamment de ID3 pour des tâches de
classification et régression
Classification Tree: Les feuilles sont des valeurs quantifiées
• Utilise l’index d’impureté Gini [rappel: ID3  Entropie]
Regression Tree: Les feuilles sont des valeurs approximées
(p.ex moyenne)
• Au lieu d’une prédiction binaire (oui/non), permettent
de prédire une valeur
• Critère d’homogénéité: p.ex: écart-type
Exemples:
– prix d’un objet en fonction de ses caractéristiques
(immobilier, assurance,…)
Approxime une fonction en fonction de ses valeurs d’entrée
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI DT-28

Index Gini
Pour chacun des sous-ensembles Wk calcul de la probabilité d’erreur
(P(Ek) = 1-P(Wk)) en proportion de la présence du label (P(Wk))
 Mesure l’“impureté” d’un ensemble partitionné en K classes Wk:

G(W)=σk P x∈Ωk

1−P x∈Ωk

= 1− σk(P x∈Ωk )2

 Encourage des ensembles homogènes
• Min G(Ωk ) = 0 si Ωk est déterministe (1 seul label)
• Max G(Ωk ) si P(Ωk )=1/K (répartition uniforme)
 Approximation de l’entropie*

Peut être utilisé comme critère de partitionnement itératif (comme
(H(X))
*de Shannon, cf Entropie de Tsallis
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI DT-29

Données (classification)
Day

Outlook

Temperature

Humidity

Wind

Play?

D1

Sunny

Hot

High

Weak

No

D2

Sunny

Hot

High

Strong

No

D3

Overcast

Hot

High

Weak

Yes

D4

Rain

Mild

High

Weak

Yes

D5

Rain

Cool

Normal

Weak

Yes

D6

Rain

Cool

Normal

Strong

No

D7

Overcast

Cool

Normal

Strong

Yes

D8

Sunny

Mild

High

Weak

No

D9

Sunny

Cool

Normal

Weak

Yes

D10

Rain

Mild

Normal

Weak

Yes

D11

Sunny

Mild

Normal

Strong

Yes

D12

Overcast

Mild

High

Strong

Yes

D13

Overcast

Hot

Normal

Weak

Yes

D14

Rain

Mild

High

Strong

No

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI DT-30

CART: Index Gini pour la racine
G(“Sunny”)= 1- (2/5)2- (3/5)2 = 0.48
G(“Overcast”)= 1- (4/4)2 = 0
G(“Rain”)= 1- (3/5)2- (2/5)2 = 0.48

Outlook

IG(“outlook”) = (5/14)*0.48+(4/14)*0+(5/14)*0.48
= 0.342
Outlook Temperature
IG

0.342

0.439

Yes

No

N (14)

Sunny

2

3

5

Overcast

4

0

4

Rain

3

2

5

Humidity

Wind

0.367

0.428

Outlook
Sunny
2+ / 3-

Stephane Marchand-Maillet – University of Geneva

Overcast
4+ / 0-

Intelligence Artificielle

Rain
3+ / 2-

AI DT-31

CART: Recursion
?

?

Outlook

Day

Temp.

Humidity

Wind

Play

D3

Hot

High

Weak

Yes

D7

Cool

Normal

Strong

Yes

D12

Mild

Mild

Strong

Yes

D13

Hot

Hot

Weak

Yes

Outlook = Overcast
Day

Temp.

Humidity

Wind

Play

Day

Temp.

Humidity

Wind

Play

D1

Hot

High

Weak

No

D4

Mild

High

Weak

No

D2

Hot

High

Strong

No

D5

Cool

Normal

Weak

No

D8

Mild

High

Weak

No

D6

Cool

Normal

Strong

No

D9

Cool

Normal

Weak

Yes

D10

Mild

Normal

Weak

Yes

D11

Mild

Normal

Strong

Yes

D14

High

High

Strong

Yes

Outlook est fixe dans
chacune des branches

Outlook = Sunny
Stephane Marchand-Maillet – University of Geneva

Outlook = Rain
Intelligence Artificielle

AI DT-32

CART: Regression Tree
Principe de Régression:
• On approxime des données (x,y) par une
fonction f
• On minimise l’erreur d’approximation
Exemple: Régression linéaire

Erreur= ෍(yi −f xi )2
i

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI DT-33

Regression Tree
Les données sont des valeurs en fonction de
caracteristiques
Exemple: Appréciation (%) du dessert vs sucre (g)
Appréciation (%)
Faux
Faux

Sucre (g)

Une régression linéaire (même optimale) donnerait de mauvaises prédictions
 Besoin d’une fonction plus complexe
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI DT-34

CART: Regression
On teste tous les seuils (pour chaque donnée) et
on regarde la qualité de l’approximation par une
fonction choisissant la moyenne pour chaque sousensemble
Bonne division
A rediviser
Choix de la racine (avec tolérance)
Mauvaise
division

Récursion sur les sous ensembles
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI DT-35

CART: Regression Tree
• Divise les données récursivement en testant les
attributs et choisit de meilleur seuil global (par
énumération par attribut et pour tous les attributs)
pour les valeurs de moindres carrés (Sum of Square
Residuals)
• Les feuilles prennent la valeur moyenne
(max,min,médiane) des observations qu’ils
contiennent
• Le critère d’arrêt est une tolérance basée sur
– La profondeur de l’arbre
– La valeur de l’erreur
– Le nombre de données par feuille
Rapport à la qualité de l’estimation (qualité vs complexité)
Rapport Biais/Variance
Compromis sur-apprentissage/généralisation
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI DT-36

Regression: Exemple de données

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI DT-37

Elagage (Decision Tree pruning)
• La construction d’un arbre cherche à minimiser
l’entropie des sous-ensembles (entropie des
feuilles à 0)
• Les données d’entrainement sont un échantillon
de la réalité  risque de sur-apprentissage
On réduit la taille (profondeur) de l’arbre par
élagage des feuilles
Augmente la généralisation
Accélère le calcul de décisions
Gagne de la place mémoire

Compromis performance (erreur) vs complexité
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI DT-39

Random Forests

SK.Learn RandomForest XXX:

Exemple: https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#

Principe: La construction d’un arbre est biaisé vers les données
d’entrainement
 On veut construire plusieurs arbres et moyenner leurs résultats
 On diversifie les données par échantillonnage de l’ensemble de départ
Bagging (bootstrap aggregation) consiste à échantillonner (avec remise)
l’ensemble de départ:
• Une donnée peut etre présente plusieurs fois
• On devient robuste aux outliers
Random feature selection : On sélectionne un sous ensemble de
caractéristique par sous-ensemble
• On filtre les caractéristiques inutiles/puissantes
•
d pour la classification, d/3 pour la régression

On crée des ensembles et on construit un arbre sur chaque ensemble
 La classification est faite par vote (majorité)
 La régression est faite par moyennage
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI DT-40

Exemple

Du fait du moyennage, les frontières de décision
sont plus lisses

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI DT-41

Résumé

Illustration ludique:
http://www.r2d3.us/visual-intro-to-machine-learning-part-1

On se place dans un contexte supervisé
 On cherche à approximer une fonction de décision
Les arbres représentent une partition récursive de l’ensemble
d’entrainement
 Prédicat logique sur les caractéristiques
 Suite de décisions basiques à appliquer
 Potentielle bonne interprétation des décisions

L’optimalité est décidée sur les critères (entropie, Gini) et propriétés de
l’arbre (profondeur, complexité)
La régression généralise la classification en fournissant une
information non quantifiée
Les Random Forest permettent de réduire le biais des données
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI DT-42

