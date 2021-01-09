Intelligence Artificielle
Gestion de l’aléatoire
Stephane Marchand-Maillet

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Aléa-1

Contenu
• Notion de probabilité
• Les outils probabilistes pour l’IA

• Variations sur le théorème de Bayes
• Notion d’entropie

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Aléa-2

Evénements
La sémantique des probabilités peut être ambiguë:
• Probabilité qu’un événement A se réalise
→ Probabilité que la proposition « A se réalise » soit vraie
→ A est vu comme une proposition logique
→ On parle de « non A » (¬A)
→ C’est la vision de A comme variable aléatoire
Mais A est aussi vu comme un ensemble de réalisations
valides (évènement élémentaires): Exple: {1,3,5} pour les
faces impaires d’un dé
→ Version ensembliste on écrit « A∩B » et « Ac »
→ Définition d’un univers W (A ⊆ W)
→ C’est la version proche du formalisme de la théorie de la
mesure ou de l’approche fréquentiste
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Aléa-3

Définition
La probabilité P(A) d’un évènement A de l’univers W est telle que
(axiomes de Kolmogorov):
1. 0≤P(A) ≤1
La probabilité est une mesure positive

2.

P(W)=1
La mesure de l’univers est 1
La probabilité qu’au moins un évènement élémentaire se réalise est 1

3.

P(AUB)=P(A)+P(B) si A∩B = ∅
Les mesures s’additionnent si l’intersection est vide
C

A
B
W
Attention: cette représentation a ses limites (cf plus tard)

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Aléa-4

Propriétés
A
W

Ac

Etant donné A on a:
W = Ac U A et A∩Ac = ∅
→P(W) = P(Ac U A) = P(Ac)+ P(A) = 1
→ P(Ac) = 1- P(A)
Exercice: Prouvez que P(AUB) = P(A) + P(B) - P(A∩B) (cf lois de De Morgan)
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Aléa-5

Calcul effectif
Pour des probabilités discrètes (W dénombrable
et fini):
|A|
A⊆W
P(A)=
|Ω|
Si A est composé d’événements (a) élémentaires
disjoints et équiprobables:
Mesure d’un événement
1
P(A) = σa∈A P(a) et P a =
|Ω|

élémentaire (« |a| »)

Décompte des
événements élémentaires a

donc |Ω|=σ𝑎∈Ω 1

Stephane Marchand-Maillet – University of Geneva

(car P(W)=1)
Intelligence Artificielle

Ω
AI Aléa-6

Exemple
Dé équilibré à 6 faces:
• Ω= 1,2,3,4,5,6
• Un évènement A= 2,4,6
• |Ω|= σa∈Ω 1 = 6

1 1
• P a =
=
|Ω| 6

a∈Ω

1
• P( 2 ) =
6
3 1
• P(A)=P( 2,4,6 )=P( 2 )+P( 4 )+P( 6 ) = =
6 2
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Aléa-7

Variable aléatoire (définition informelle)
Une variable aléatoire X peut être vue comme une
proposition pouvant être vraie avec la probabilité
p∈(0,1) et fausse avec la probabilité 1-p
Exemple (dé à 6 faces):
• Univers: Ω= 1,2,3,4,5,6
• Un évènement A= 2,4,6
• On déclare la variable aléatoire X (résultat)
• P(A) = P( 2,4,6 ) est traduit en P(X∈ 2,4,6 )
• Ou P( 5 ) = P(X=5) (Note: P(X ≠5) = 1 - P(X=5))
ensembliste

logique

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Aléa-8

Probabilité conditionnelle
Définition:
P(A∩B)
P AB =
P(B)
“Probabilité de A sachant (la probabilité de) B”
“B est le nouvel univers”

A

A∩B

B

A

W
P(A)
Stephane Marchand-Maillet – University of Geneva

B

W
P(A|B)
Intelligence Artificielle

AI Aléa-9

Probabilité conditionnelle
On a donc:

P(A∩Ω)
P(A) = P(A∩W)/1 =
= P(A|W)
P(Ω)
→ Toute probabilité est conditionnée à son
univers
P(A) en connaissance de (sachant)… B, W, …
P(A) en ignorant ce qui n’est pas dans.. B, W,…
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Aléa-10

Exercice: étudiez les cas A=B et B=W

Cas particuliers
• B⊂A
P A∩B P(B)
A
P AB =
=
=1
P(B)
P(B)
B
→ si on sait que B est réalisé alors A est certain
(B est le nouvel univers, seule la partie B de A est visible)
• A⊂B
P A∩B P(A)
P AB =
=
B
P(B)
P(B)
→ A est mesuré complètement en fonction de B
(B est le nouvel univers)
• A∩B = ∅

A
B

P A∩B P(∅)
P AB =
=
=0
P(B)
P(B)
→ A n’est pas visible dans le nouvel univers (B)

Stephane Marchand-Maillet – University of Geneva

A

Intelligence Artificielle

AI Aléa-11

Loi des probabilités totales
On a:
P(A) = P(A∩W)
et A∩W = A∩(B U Bc) = (A∩B) U (A∩Bc)
et (A∩B) ∩ (A∩Bc) = ∅

Bc

B
A
W

Donc (axiome 3):
P(A) = P((A∩B) U (A∩Bc)) = P(A∩B) + P(A∩Bc)
Soit:
P(A) = P(A|B).P(B)+ P(A|Bc).P(Bc)
Plus généralement:
P(A)= σN
i=1 P A Bi .P( Bi )
A

si la famille Bi est une partition de W
(couvre W et sont disjoints 2 à 2)
Stephane Marchand-Maillet – University of Geneva

W
Intelligence Artificielle

AI Aléa-12

Probabilité jointe
P(A∩B)
Si P A B =
P(B)
alors P(A∩B) = P(A|B).P(B)

P(A∩B) = P(A,B) est la probabilité jointe des
temporalité
évènements A et B
P(A∩B) = P(A|B).P(B)
Proba jointe,
Proba des 2 evenements

Proba de l’un (B)…
…proba de l’autre (A)
sachant le premier (B)
temporalité

A et B se réalisent (ou non)
Stephane Marchand-Maillet – University of Geneva

A se réalise (ou non) sachant B
Intelligence Artificielle

B se réalise (ou non)
AI Aléa-13

Exemple
Une urne contient des objets (balles et cubes) de couleur (rouges ou blancs)
Evenement A=“l’objet est rouge”
Evenement B=“l’objet est un cube”

• P(A) = proportion d’objets rouges = 16/26 ~ 0.61
• P(B) = proportion de cubes = 14/26 ~ 0.53

Rouge

Blanc

Cube

12

2

Balle

4

8

• P(A,B)=proportion de cubes rouges = 12/26 ~ 0.46

• P(A|B)=chance d’avoir un objet rouge sachant la probabilite de tenir un cube
= 12/14 ~ 0.85
• P(Ac|B)=chance d’avoir un objet blanc sachant la probabilite de tenir un cube
= 2/14 ~ 0.19
• P(A|Bc)=chance d’avoir un objet rouge sachant la probabilite de tenir une
balle = 4/12 ~ 0.33
Exercice: refaire les calculs avec une plus forte proportion de balles que de cubes
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Aléa-14

Indépendance
Définition:
On dit que deux évènements A et B sont
indépendants ssi:
P(A∩B) = P(A,B) = P(A).P(B)
P(A∩B) P A P(B)
→P A B =
=
= P(A)
P(B)
P(B)
→B n’apporte pas de connaissance pour A
→Et A n’apporte pas de connaissance pour B
Attention: l’indépendance n’implique pas A∩B= ∅
Sinon: P(A∩B) = P(∅) = 1-P(W) = 0 ≠ P(A).P(B)
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Aléa-15

Attention aux illustrations
A et B sont disjoints: A∩B= ∅

B

A

P(A∩B) = P(∅) = 1-P(W) = 0

W

Forme
W2

B

W=W1xW2

A,B
A et B sont indépendants (“orthogonaux”)
P(A,B) = P(A)P(B)

A
Stephane Marchand-Maillet – University of Geneva

W1
Couleur
Intelligence Artificielle

AI Aléa-16

Théorème de Bayes
Si A et B sont deux évènements alors:
P A B P(B)
P BA =
P(A)
Preuve:
Directe à partir de la définition de la
probabilité conditionnelle

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Aléa-17

Facettes du Théorème de Bayes
Interprétation:
La probabilité conditionnelle introduit une temporalité. On peut
donc étudier les effets (observable) d’une cause (supposée)
A = Observation de l’effet (symptôme)
B = présence de la cause (cachée)
Je peux observer les effets sous l’hypothèse de la cause: c’est P(A|B) =
P(effet|cause)
J’ai une idée a priori sur la présence de la cause: c est P(B) = P(cause)
J ai une idée sur la présence de l’effet: c est P(A)=P(effet)
→ Je peux estimer la présence de la cause (sans l’observer
directement) sachant que j’ai observé l’effet:
c’est P(B|A) que je peux calculer par le théorème de Bayes

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Aléa-18

Interprétation opérationnelle
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
AI Aléa-19

Interprétation
Modification de connaissance
apportée par l’observation
(observation de l’effet normalisée
par notre apriori sur la présence de l’effet)

P cause effet =

P effet cause
P(effet)

Notre certitude sur la présence de
la cause après avoir observé l’effet

Notre certitude sur la présence de
la cause avant d’avoir observé l’effet

P maladie sympôme =
Stephane Marchand-Maillet – University of Geneva

P(cause)

P

symptôme maladie
P(symptôme)

Intelligence Artificielle

P(maladie)
AI Aléa-20

Exercice
Je veux savoir si il fait soleil en écoutant les oiseaux
J’observe que :
• Les oiseaux chantent 9 fois sur 10 quand le soleil est la
• 7 fois sur 10 quand je tends l’oreille j’entends les oiseaux
chanter
• Il fait soleil 1 jour sur 4

Avant d’ouvrir mes volets, j’entends les oiseaux. Quelle est la
probabilité qu’il y ait du soleil?

P chant soleil P(soleil) 0.9∗0.25
P soleil chant =
=
≅ 0.32
0.7
P(chant)

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Aléa-21

Exercice

P soleil chant ≅ 0.32

Je veux savoir si il fait soleil en écoutant les oiseaux
J’observe que :
• Les oiseaux chantent 9 fois sur 10 quand le soleil est la
• 7 fois sur 10 quand je tends l’oreille j’entends les oiseaux chanter
• Il fait soleil 1 jour sur 4
→ Les oiseaux chantent très souvent quand le soleil est la (90%)
→ Mais les oiseaux chantent souvent EN GENERAL (70%)
→ L’information du chant des oiseaux ne modifie pas beaucoup ma connaissance sur
la présence du soleil (32% au lieu de mon apriori de 25%)
posterior = 1.28 * prior

P soleil chant =

P chant soleil
P(soleil)
P(chant)

Ce serait différent si:
• Les oiseaux chantaient moins souvent (30%) en général: P soleil chant =?
• Le soleil brillait plus souvent (75%): P soleil chant =?
•

Que se passe t il si les oiseaux chantent 9 fois sur 10 quand je tends l’oreille?

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Aléa-22

Exercice
Comment exprimer que les oiseaux chantent toujours et seulement
quand il y a du soleil?
P chant soleil = 1 et P(chant)=P(soleil)
Dans ce cas:
P(chant,soleil) = P chant soleil P(soleil) = P(soleil)
= P soleil chant P(chant) =
P chant soleil P(soleil)
P(chant) = P(chant)
P chant
Suffit-il de dire: P(chant)=P(soleil)?
chant

chant

soleil
soleil
W

W
Non

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Aléa-23

Cas particulier

=1
P effet cause P(cause)
P cause effet =
P(effet)

Je veux savoir si il fait soleil en écoutant les oiseaux
et je sais que P chant soleil = 1
→ Les oiseaux chantent à chaque fois qu’il y a du soleil (mais pas
seulement)
P(chant∩soleil)
=1
P(soleil)
→ On peut ne considérer que les chants car
P(soleil|non-chant)=0
→ P chant soleil =

P(soleil)
⇒ P soleil chant =
P(chant)
W=chant

chant

soleil

soleil
W
Stephane Marchand-Maillet – University of Geneva

Je n’ai plus d’information pour décider
Intelligence Artificielle

AI Aléa-24

Autre écriture
On sait que P(A) = P(A|B).P(B)+ P(A|Bc).P(Bc)
Donc:
P A B P(B)
P BA =
P(A|B).P(B)+ P(A|Bc).P(Bc)

P(A|Bc).P(Bc)
P B A = 1+
P A B P(B)

−1

La certitude que la cause est présente (P cause effet =1) est altérée
par le fait d’observer le même effet en l’absence de la cause

P(effet|non−cause).P(non−cause)
P cause effet = 1+
P effet cause .P(cause)
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

−1

AI Aléa-25

Contexte de test
On a une hypothèse (H, « cause ») qu’on cherche a
verifier à travers des observations (O, « effets »)

(effet)
Observation

P O H P(H)
P HO =
P(O|H).P(H)+ P(O|Hc).P(Hc)

Observé
Pas observé

Hypothèse (cause)
Hypothèse vraie

Hypothèse fausse

Vrai positif P(O,H)

Faux positif P(O,Hc)

Faux négatif

Vrai négatif

La probabilité que l’observation soutienne
l’hypothèse (P(H|O)) est la proportion de vrais
positifs parmi tous les positifs
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Aléa-26

Arbre de décision
Un arbre de décision représente une séquence de décisions et leurs
branchements possibles
A

B
P(B,A)

P(¬B,A)
P(B, ¬A)

P(¬B, ¬A)

• La probabilité d’un nœud est le produit des probabilités le long du
chemin
• L’arbre n’est pas forcément binaire
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Aléa-27

Arbre de décision
On peut faire de l’inférence:
P B A P(A)
P AB =
P(B)?
P(B)
Probabilités totales →

P B A P(A)
P AB =
P(B|A)P(A)+P B ¬ A P(¬ A)

Exercice: calculez P(¬ A|B)

P(A,B)
(1)
P AB =
=
P(A,B)+P(¬ A,B) 1 +(3)
On va étudier la construction d’arbres de décision
dans la suite du cours
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Aléa-28

Exemple 1
2 urnes contenant des balles rouges et blanches
Rouge

Blanc

Urne 1

12

2

Urne 2

4

8

Je tire une balle rouge d’une des urnes. Quelle est
la probabilité que ce soit l’urne 1?

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Aléa-29

Exemple 1
On veut calculer P(Urne 1|Rouge)

Tirage rouge
Choix de l’urne

P(Urne1,Rouge) = 3/7

P(Urne 1,Blanc) = 1/14
P(Urne 2,Rouge) = 1/6

P(Urne 2, Blanc) = 1/3
=1
P(Urne 1|Rouge) = P(Urne1,Rouge) / (P(Urne1,Rouge)+ P(Urne 2,Rouge) )
= (3/7) / ((3/7)+(1/6)) = 0.72 → 72%
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Aléa-30

Exemple 2
• Je sais que 80% des champignons sont
comestibles
• Un spécialiste sait reconnaitre à 95% un
champignon comestible
• Par contre, il surestime 3% des champignons
Je trouve un champignon et il le classe comme
comestible: quelles sont mes chances de me
régaler?
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Aléa-31

Exemple 2
On veut calculer P(comestible|oui) :

Expertise

Comestible

P(comestible,oui)

P(comestible,non)
P(Indigeste,oui)

P(Indigeste, non)

Réponse = (0.8*0.95)/((0.8*0.95)+(0.2*0.03)) = 99,2%
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Aléa-32

Mesurer l’incertitude: notion d’entropie
Etant donné un ensemble W d’éléments équiprobables, on cherche à distinguer
chaque élément avec des questions binaires (Vrai/Faux)
Combien de questions au minimum faut-il pour identifier un objet?

La réponse est la profondeur de l’arbre (de décision) binaire équilibré dont les feuilles
sont les éléments de W, soit log2(|W|). C’est une mesure (en bits) de l’incertitude du
système (son contenu d’information).
Exemple: Dé équilibré à 8 faces:

0 1

D = |W|

1

D = log2(|W|) = 3

2
3
4

…
1

2

3

4

5

6

7

8

Note: l’arbre représente le codage binaire d’un label pour chaque élément
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Aléa-33

Entropie (construction informelle)
Pour le tirage d’un dé équilibré à 8 faces, on a pour chaque face a:
P(a) = 1/|W| soit D = -log2(P(a))

On généralise en distribuant l’incertitude du système sur chaque
événement a.
On définit donc l’entropie d’une variable aléatoire X représentant le
résultat d’un tirage sur W par la somme (moyenne) pondérée:
H X = − ෍ P a log2 P(a)
a∈Ω

Note:
Pour des événements a équiprobables on a P(a) = 1/|W|
donc
H(X) = − σa∈Ω P a log 2 P(a) = log 2 |W|

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Aléa-34

Autre construction (informelle)
Soit une variable aléatoire X séparant W en W1 et W2 avec la probabilité p1 (X=x1)
et p2 = 1-p1 (¬X, X=x2) respectivement
X

W1

¬X

W2

Pour a ∈ W on a

W

P(a) = P(a|X)P(X)+P(a|¬X)P(¬X) = P(a|X) p1+P(a|¬X) p2
Dans W1 et W2 les événements sont équiprobables donc pour “coder” W1 il faut –log2p1
bits et pour “coder” W2 il faut –log2p2 bits

Soit en moyenne
H(X) = - p1log2p1 – p2log2p2
bits d’incertitude sur le système complet
En généralisant le raisonnement on arrive à
H(X) = − σa∈Ω P a log 2 P(a)
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Aléa-35

Exemple
Documents pertinents pour une requête:
• Soit une collection de documents W
séparée en 2 sous ensembles W1 et W2
(pertinents et non-pertinents
respectivement).
L’entropie de la requête est une mesure de
l’incertitude:
• Une requête séparant les documents
équitablement apportera une incertitude
plus grande (log2(2) = 1) qu’une requête
définissant un petit ensemble de
documents pertinents.
Note: Dans W1 et W2 les documents deviennent équivalents
(équiprobables)

Source: Wikipedia

Autre exemple: pièce biaisée
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Aléa-36

Entropie conditionnelle
L’entropie H(X) est une mesure de l’information contenue dans une
variable aléatoire X. Quid de l’information contenue dans X dans le
contexte de la connaissance de Y?
Exemple: X=« Les oiseaux chantent », Y=« C’est l’été »
C’est l’entropie conditionnelle (par énumération) :
H X|Y =− ෍ P Y=y ෍ P(X=x|Y=y) log2 P(X=x|Y=y)
y∈ΩY
x∈ΩX
Note (avec probabilités jointes):
H X|Y =−

෍
P(X=x,Y=y) log2
x∈ΩX y∈ΩY

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

P(X=x,Y=y)
P(Y=y)

AI Aléa-37

Information mutuelle / Gain
Le gain d’information de la connaissance de Y sur X (et inversement)
définit l’information mutuelle entre X et Y:

I(X;Y) = H(X)-H(X|Y) = H(Y)-H(Y|X)
On peut représenter graphiquement l’information par les diagrammes
de Venn:
I(X;Y) Ce que partagent X et Y
H(X|Y)

H(Y|X)
Ce qu’il reste de Y
quand on connait X

Ce qu’il reste de X
quand on connait Y

H(X)
L’information
contenue dans X

H(Y)
L’information
contenue dans Y

Un cercle représente un conteneur d’information. Si les variables ne
sont pas indépendantes (elle partagent de l’information mutuelle),
leurs cercles se recouvrent d’autant. Sinon I(X;Y)=0
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Aléa-38

Résumé
• Les probabilités discrètes se calculent de façon ensembliste
(par énumération – approche fréquentiste)
• On raisonne en général sur des variables aléatoires
(propositions logiques)
• La notion de probabilité conditionnelle permet de faire de
l’inférence: on exploite l’information donnée par nos
observations dans le contexte de nos hypothèses (approche
épistémologique – basée sur le belief (croyance, certitude))
• La notion d’entropie permet de quantifier l’information et
donc donne un critère d’optimisation pour l’inférence
→ On va exploiter ces constructions dans les prochains
chapitres
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Aléa-39

