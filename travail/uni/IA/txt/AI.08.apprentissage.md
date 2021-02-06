Intelligence Artificielle
Introduction à l’Apprentissage
Stephane Marchand-Maillet

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Learning 1

Contenu
• Types d’apprentissage
• Composantes de l’apprentissage
• Evaluation
• Généralisation et sur-apprentissage

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Learning 2

Apprentissage vs recherche
Algorithmes de recherche:
• Enumérations organisées pour chercher une solution
• On injecte de la connaissance par le modélisation des
états et en utilisant des heuristiques
 Exploration de l’univers d’états
Apprentissage:
• On collecte de données
Echantillonnage de l’univers d’états
On essaie d’inférer (généraliser) de la connaissance à
partir de ces exemples
• On injecte de la connaissance en utilisant des modèles
qui ont potentiellement généré les données
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Learning 3

Exemple
Jeu d’échecs:
• Recherche: On utilise l’algorithme MiniMax avec une
heuristique pondérant les pièces pour leur importance
stratégique
– Branchement = 35, Horizon = 20, 2.1030 tests
La connaissance est dans la maximisation de l’utilité (et
heuristique)

• Apprentissage: On apprend, à partir de parties jouées
dont on connait le résultat, un modèle de joueur
(p.exple: réseau de neurones) qui en fonction d’un
contexte (position des pièces) joue un coup
 La connaissance est dans les parties jouées qui
permettent d’inférer des décisions
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Learning 4

Modèles et caractéristiques
On modélise le contexte (ses échantillons, les données) par
des caractéristiques supposées être pertinentes (pour le
problème):
Exemple: modèle d’une personne
• Médical: taille, poids, âge, genre,…
• Marketing: âge, genre, revenu,…
• Politique: rural/urbain, âge, revenu,…
 La couleur des cheveux est peu pertinente
Pertinence

~ corrélation avec l’objectif en question
~ contenu d’information

Remarque importante:
Attention aux biais (sociétaux) internes aux données
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Learning 5

Exemple: le modèle Gaussien
On veut prédire une caractéristique d’un objet
On lui associe un modèle
Exemple: diamètre d’une pomme
• On collecte plusieurs de ces objets
• On mesure la caractéristique
 Prédiction basique: moyenne
 Ordre supérieur: introduction de la variance
Modèle Gaussien: «La valeur de caractéristique devient exponentiellement
moins probable au fur et à mesure qu’elle s’écarte de la moyenne»
1 −(𝑣−𝜇)
P(v)= 𝑒 2𝜎2
𝑍

2

 Apprentissage: on optimise les paramètres q= [m,s] avec les données
 Hypothèse d’un prototype «moyen» dont les observations sont une
«déformation»
 Ici, on interdit les distributions bimodales (exple: taille d’une personne)
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Learning 6

Apprentissage
On part de données et on cherche:
• une association que l’on connait
Apprentissage supervisé: on connait la décision
associée à certains exemples de nos données
Méthodes: classification, régression,…

• une structure que l’on veut découvrir
Apprentissage non-supervisé: on cherche des
structures dans les données qui nous permettront
de mieux les comprendre
Méthodes: clustering, embedding,…
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Learning 7

Apprentissage non-supervisé
Clustering

f2

f1

Etant données des données dans leur espace de
représentation….
Exemples: communautés, profils, …
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Learning 8

Apprentissage non-supervisé
Clustering

f2
Cluster 1
Cluster 2

f1

… on cherche à leur associer des labels
(pas abordé dans ce cours)
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Learning 9

Apprentissage non-supervisé
Embedding

On cherche des représentations pertinentes pour
les données
(pas abordé dans ce cours)
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Learning 10

Apprentissage supervisé
Classification:
On connait les classes (décisions, labels) Y={yi} pour
certaines données (exemples, contextes) X={xi} , on s’en
sert pour apprendre une « fonction » qui attribuera des
classes aux données non classifiées (prédiction)
Classe

Donnée
« fonction »

Exemples:
• Classification d’images (labélisation)
– Classe yi = « chat », « chien », « arbre », …

• Prise de décision selon des capteurs (diagnostic)
– Classe yi = « oui », « non », « sain », « malade », …
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Learning 11

Exemple: classification
Données classifiées
Chat

Chat

Souris

Souris

Chat

Souris

Chat

Souris

Chat

Chat

Souris

Chat

Souris

Chat

Souris

Souris

Souris

Données non-classifiées

?

?

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Learning 12

Exemple: classification
Chat Chat
Chat
Chat
Chat
Chat
Chat
Chat
Souris
SourisSouris
Souris
Souris
Souris
Souris
Souris Souris

On représente les données classifiées
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Learning 13

Exemple: classification
Chat Chat
Chat
Chat
Chat
Chat
Chat
Chat

Chat
Souris

Souris
SourisSouris
Souris
Souris
Souris
Souris
Souris Souris
On apprend une fonction de classification
Note: on peut utiliser les données non-classifiées pour l’apprentissage (apprentissage semi-supervisé)
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Learning 14

Exemple: classification

Chat

?

Souris

?

On représente les données non-classifiées
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Learning 15

Exemple: classification

Chat

Chat

Souris

Souris

On peut classifier ces données (prédiction de classe)
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Learning 16

Apprentissage supervisé
Régression:
On connait les sorties (valeurs) yi pour certaines
données (exemples, contextes) xi, on s’en sert
pour apprendre une « fonction » qui attribuera
(prédira) des valeurs aux données inconnues
Valeur
yi

Donnée
xi
« fonction »

Equivalent à une classification avec classes
continues
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Learning 17

Exemple: Régression
Valeur yi

Nouvelle
Valeur

Prédiction

Fonction de régression

Nouvelle
donnée

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

Donnée xi

AI Learning 18

Dualité classification-régression
Valeur yi (classe)

Prédiction

Fonction de régression

chat
souris

Seuil

Prédiction

Nouvelle
donnée

Stephane Marchand-Maillet – University of Geneva

Nouvelle
donnée

Intelligence Artificielle

Donnée xi
(exple: taille)

AI Learning 19

Dualité classification-régression
Valeur yi

Prédiction

Fonction de régression

chat
souris

Seuil

Prédiction

Nouvelle
donnée

Stephane Marchand-Maillet – University of Geneva

Nouvelle
donnée

Intelligence Artificielle

Donnée xi

AI Learning 20

Apprentissage (semi-)supervisé
On vise l’association: exemple  classe
Exple: image  label (chien, chat, …)
Etant donnés un ensemble E={(xi,yi)} d’exemples associés à des classes
(entrainement) et un ensemble T={xi} (test) d’exemples pour lesquels on
cherche la classe associé:
Types d’apprentissage:
• Inductif: on apprend un modèle (règles générales) sur l’ensemble E
Peut inclure une forme d’inférence

• Déductif: on utilise ces règles pour attribuer des classes sur T

• Transductif: On apprend sur E (et T) pour prédire des classes sur T
Lien avec l’apprentissage semi-supervisé et l’apprentissage “actif”
Capacité à apprendre une approximation des exemples (qui permet la
gestion des exceptions aux règles)
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Learning 21

Transductive learning

Test T
Entrainement E

“When solving a given problem try to avoid solving a
more general problem as an intermediate step.”

From: The Nature of Statistical Learning Theory, Vapnik, Springer, 1998

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Learning 22

Apprentissage
L’apprentissage dépend de la méthode utilisée:
• Hypothèses sous-jacentes
• Modèle de données
• Modèle d’apprentissage et critère d’optimalité

Voir: https://scikit-learn.org

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Learning 23

Apprentissage
On choisit un modèle de fonction d’apprentissage
fq avec des paramètres q et on cherche les
paramètres optimaux grace aux données X
𝜃 ∗ = argmin 𝐿(𝜙𝜃 (X); X)
𝜃

où L(X’,X) est une mesure d’erreur
Exemple:
• Modèle de classification linéaire: q = [a,b]
• L(.,.) mesure le taux de données mal classifiées
par fq
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Learning 24

Composantes de l’apprentissage
• On doit définir un objectif:
– Quelles sont les classes? Combien sont-elles?
– Quelle prédiction veut-on?

• On fixe un modèle d’apprentissage:
– Quels sont ses paramètres? Sa complexité? Sa capacité?
– Quels sont ses hyper-paramètres?
– Ai-je assez de données pour apprendre ce modèle?

• On rassemble des données:
– Quelle est leur représentation?
– Quel volume? Quelle diversité?
Apprentissage  classes associées à un sous-ensemble?

• On fixe une mesure d’évaluation:
– Quelle est la qualité de mon apprentissage?
– Mes données sont-elles pertinentes (représentatives) pour
évaluer?
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Learning 25

Objectif de l’apprentissage
• Consiste à définir une abstraction du problème
en question
• L’objectif doit être clair:
– il définit l’évaluation

• L’objectif doit être aussi simple que possible:
– Il conditionne la complexité du modèle
– Il doit extraire la connaissance pertinente

C’est une étape largement arbitraire mais qui
conditionne la suite:
Les limites et hypothèses posées ici sont
indépassables pour la suite
Lien avec l’« Enveloppe du monde » (univers clos)
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Learning 26

Modèle d’apprentissage
Le choix du modèle se base sur:
• Ses performances connues pour le type de problème
• Ses hypothèses sous-jacentes (connaissance a priori)
• Sa complexité, sa robustesse
• Le nombre de ses (hyper-)paramètres
• Le volume de données disponible
• Le volume de données requis pour l’apprendre
• La connaissance qu’on a du problème
• …
• La mode du moment
Exemple de modèles:
• Réseaux de Neurones
• Arbres de décisions
• Classifieurs à Noyaux
• …
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Learning 27

Données
Une (grande) partie de la connaissance de notre monde
(en plus des hypothèses du modèle)
Les questions liées sont:
• Leur représentation
– Extraction de caractéristiques (coût, dimension)
– Qualité de la représentation (pertinence, discrimination)

• La qualité
– Bruit associé aux mesures

• Le volume, la diversité
– Relation à la complexité du modèle et du problème
– Lien avec la théorie de l’estimation statistique

• La labélisation
– Qualité versus quantité
– Proportion label/sans-label, entre classes
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Learning 28

Evaluation
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

AI Learning 29

Evaluation

Souris
(non-pertinent)

Valeur du seuil

True Positive rate

Exemple: ROC curve

Chat
(pertinent)

TP

TN
FN

FP
Taille

Negatif

False Positive rate

Positif

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Learning 30

Evaluation

Souris
(non-pertinent)

Valeur du seuil

True Positive rate

Exemple: ROC curve

Chat
(pertinent)

TP

TN
FN

FP
Taille

Negatif

False Positive rate

Positif

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Learning 31

Evaluation
• Error rate:

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

AI Learning 32

Protocole supervisé

𝜃 ∗ = argmin 𝐿(𝜙𝜃 (X); X)
𝜃

Entrainement: On utilise les données pour estimer q*:
• On utilise les données d’entrainement labelisées pour
minimiser L(.,.)
 On obtient pour une certaine erreur
d’entrainement (training error)
Test: On évalue les performances du modèle 𝜙𝜃∗ avec des
données inconnues jusque la:
• On teste le modèle appris 𝜙𝜃∗ avec des données de
test labelisées (indépendantes de l’entrainement) dont
on cache le label
On obtient l’erreur de test (test error). C’est celle
qui définit les performances du modèle
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Learning 33

Validation
Le modèle contient en général des hyper-paramètres (paramètres
d’architecture)
Exemples:
• Degré d’une fonction de régression
• Nombre de neurones
On rajoute une étape de validation dans l’entrainement pour tester
plusieurs valeurs d’hyper-paramètres. On utilise (et teste) le modèle
donnant l’erreur d’entrainement la plus basse.

Entrainement:
Pour chaque valeur d’hyper-paramètre:
Entrainer le modèle sur l’ensemble E
Valider sur l’ensemble V
Choisir les paramètres q* qui minimisent l’erreur d’entrainement
Test:
Utiliser l’ensemble de données T pour tester le modèle (test error)
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Learning 34

Protocole d apprentissage
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

AI Learning 35

Propriétés
Simplicité (parcimonie) des modèles:
• On cherche un compromis entre la simplicité du
modèle et sa performance
• Principe de parcimonie (cf Rasoir d’Occam)
– Cf critères « Information Criterion »: BIC, AIC, …

Simplicité:
• Moins de paramètres  meilleure estimation à volume
de données constant
• Données bruitées  on ne veut pas apprendre les
détails des données (sur-apprentissage)
• Complexité moindre (sémantique et computationnelle)
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Learning 36

Sur-apprentissage
On apprend les détails (bruit dans les données)

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Learning 37

Généralisation
On cherche un modèle efficace hors des données
d’entrainement:
• Trop simple: mauvaise prédiction
• Trop complexe: il apprend les données sans se
préoccuper de l’espace entre les données
On cherche une certain niveau de continuité de
l’information
En général:
sur-apprentissage
Erreur

ETest

EEntrainement
Etapes d’entrainement
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Learning 38

Résumé
• L’apprentissage se base sur les données pour estimer la
réalité comme une «fonction» (dont on estime les
paramètres)
• Le choix de représentation des données est important
pour les performances
• Le protocole d’apprentissage inclut:
– Un objectif, un modèle, des données labélisées et une
mesure d’évaluation

• Les données sont la vue partielle du monde auquel le
modèle a accès (en plus de ses propres hypothèses)
– Leur choix (représentativité : volume, diversité) est
important pour éviter les biais, le sur-apprentissage et le
manque de généralisation
– La validation croisée permet de diversifier les données et
de fournir une statistique (variance) sur les résultats
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Learning 39

Outlook
Dans ce cours nous verrons:
• Les arbres de décision
• Les réseaux Bayésiens
• Le classifieur « Naive Bayes »
• Les réseaux de Neurones

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Learning 40

