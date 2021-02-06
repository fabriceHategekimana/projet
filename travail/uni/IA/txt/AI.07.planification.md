Intelligence Artificielle
Planification
Stephane Marchand-Maillet

Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Planification-1

Contenu
• Planification par représentation logique
• Formalisation

• Méthodes de planification

Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Planification-2

Planification
Position du problème:
La planification est le problème de produire une
séquence d’actions (un plan) menant à un objectif
fixé

Les méthodes recherche sont un cas particulier de
planification où les outils utilisés sont des structures
de données (graphe, arbres) et des algorithmes de
recherche. Le plan est le chemin de sI à sG
Ici on va utiliser les outils de la logique pour la
planification
Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Planification-3

Rappel: Boucle Action-Perception
Perception
Données

Capteurs
Contexte
Environnement

“Intelligence” Décision
Action
Effecteurs

• Monde
• Autres agents
• …

Agent

L’agent perçoit l’état actuel, et agit vers l’objectif
Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Planification-4

Exemple
Blocs:
Pince P (effecteur)

A

B

Bloc A
Plan (d’actions)

Table T

B

Bloc B

C

C

Bloc C

A

Initial
Stephane Marchand-Maillet – University of Geneva – Computer Science

Objectif
AI Planification-5

Formalisation: faits, états
Observer les faits et les réifier:
• Un fait est une proposition (vraie):
sur(A,B): le cube A est sur le cube B (vrai)

• On généralise (réifie) en fonction de l’état s:
sur(x,y,s): à l’état s, l’objet (cube, table) x est sur l’objet y

• On peut écrire:
sur(A,B,sI) ou sur(B,C, sG)
ou
∀ x,y,s sur(x,y,s) ⇒ ¬ libre(y,s)

Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Planification-6

Formalisation: action
On fait de meme pour les actions:
• L’action deplacer(x,y,z) est l’opération de
déplacer l’objet x (qui est sur y) vers z
• On applique cette operation sur l’état s pour
générer un nouvel état s’
s’ = faire(action, s)

• On peut écrire
libre(B,faire(deplacer(A,B,T),s))
ou
sur(x,y,s) ⋀ libre(x,s) ⋀ (z ≠ y) ⇒ libre(y,faire(deplacer(x,y,z),s)
Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Planification-7

Actions
sur(x,y,s) ⋀ libre(x,s) ⋀ libre(z,s) ⋀ (z ≠ y) ⇒ libre(y,faire(deplacer(x,y,z),s)

Pré-conditions à l’action

Effet de l’action

sur(x,y,s) ⋀ libre(x,s) ⋀ libre(z,s) ⋀ (z ≠ y) ⇒ sur(x,z,faire(deplacer(x,y,z),s)

B

B
C

A

Stephane Marchand-Maillet – University of Geneva – Computer Science

C

A
AI Planification-8

Formalisation: axiomes
On inclut des axiomes vrais pour tous les états
comme règles d’inférence
∀ x,y,s

sur(x,y,s) ⇒ ¬ libre(y,s)

Question: comment arriver à représenter le monde dans son
ensemble?
∀ x,y,s sur(x,y,s) ⋀ (x ≠ u) ⇒ sur(x,y,faire(deplacer(u,v,w),s)
(déplacer u n’affecte pas les positions relatives de x et y)

«Frame problem»: envelopper le monde
• Effets locaux
• Axiomes globaux
Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Planification-9

Enveloppe du monde

Créer un environnement local maitrisable

Stephane Marchand-Maillet – University of Geneva – Computer Science

https://abcnews.go.com/GMA/Living/machine-fold-laundry-debuts-ces/story?id=60260894

https://www.wired.com/2011/06/yes-a-laundry-folding-robot/

AI Planification-10

Exemple pratique: langage STRIPS
STRIPS: STanford Research Institute Planning System (70’s)
→ Créé pour la robotique (robot Harvey)
Principe: Basé sur la réduction de problèmes:
Décomposer un problème en sous-problèmes solubles
• A l’état s, chercher une différence avec sG (proposition
pas directement prouvable)
• Chercher une action a permettant de réduire cette
différence et dont les préconditions sont satisfaites en s
• Appliquer l’action a vers s’ et chercher à atteindre sG de
s’
Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Planification-11

STRIPS
• Pas de proposition négative
• Hypothèse du monde fermé:
Ce qui n’est pas exprimé comme vrai est faux
• Pas de disjonction (OR)
• Pas de variable

Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Planification-12

Exemple: Blocs
• Etat: conjonction de propositions
cube(A) ⋀ cube(B) ⋀ cube(C) ⋀
sur(A,B) ⋀ sur(B,C) ⋀ sur(C,T) ⋀
libre(A) ⋀ vide(P)

• Objectif (état): conjonction de propositions
cube(A) ⋀ cube(B) ⋀ cube(C) ⋀
sur(C,A) ⋀ sur(B,C) ⋀ sur(A,T) ⋀
libre(B)
L’objectif est réalisé quand toutes les propositions le
décrivant font partie de l’état courant
Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Planification-13

Représenter une action
action(sujets)
Préconditions: doivent être vraies
Effets:
Add-list: propositions ajoutées
Delete-list: propositions supprimées

Résultat: conjonction de propositions (nouvel état)

Exemple:
depiler(x,y)
P: vide(P), cube(x), cube(y), libre(x), sur(x,y)
A: tenir(x), libre(y)
D: libre(x), vide(P), sur(x,y)
Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Planification-14

Exemple à développer
• Un robot aspirateur A
• 2 pièces R1, R2
• De la poussière

→ But: 2 pièces propres
• Agent? Etat?
• Actions?
• Etat initial? Etat final?
Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Planification-15

Exemple à développer
• Un robot aspirateur A
• 2 pièces R1, R2
• De la poussière

→ But: 2 pièces propres
• Agent? Etat?
• Actions?
• Etat initial? Etat final?
Stephane Marchand-Maillet – University of Geneva – Computer Science

dans(A,R1), propre(R1)
deplace(A,R1), aspire(R1)

AI Planification-16

Exemple contraint

Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Planification-17

Chaînage avant
• On développe un graphe pour explorer les états
en appliquant les actions possible
• L’exploration s’arrête quand toutes les
propositions du but sont présentes dans l’état
courant

→Niveau de branchement élevé
→Pas de garantie de complétude (cycle)
→Pas de garantie d’optimalité
→On cherche une heuristique pour guider la
construction de la solution
Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Planification-18

Chaînage avant
depiler(A,B)

deposer(A)

saisir(A)

depiler(B,C)

…

Stephane Marchand-Maillet – University of Geneva – Computer Science

…

empiler(B,A)

…
empiler(A,B)

deposer(B)

…

saisir(C)
…

AI Planification-19

Graphe de planification
• On construit un graphe connectant les états par des actions
applicables
sur(A,B)
sur(B,C)
sur(C,T)
vide(P)
libre(A)

sur(A,B)
sur(B,C)
sur(C,T)
vide(P)
libre(A)
tenir(A)
libre(B)

depiler(A,B)

sur(A,B)
sur(B,C)
sur(C,T)
vide(P)
libre(A)
tenir(A)
libre(B)
sur(A,T)
libre(A)

deposer(A)

sur(A,B)
sur(B,C)
sur(C,T)
vide(P)
libre(A)
tenir(A)
libre(B)
sur(A,T)
libre(A)
tenir(C)
libre(C)

…

depiler(B,C)
saisir(A)

• La profondeur des propositions dans ce graphe sert d’heuristique
(approximation) admissible et consistante
• A* avec cette heuristique produit une solution avec un minimum
d’actions (optimale)
Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Planification-20

Chaînage arrière
On part de l’objectif et on régresse par actions
pertinentes pour retourner à l’état initial
→ Niveau de branchement réduit
Def: une action est pertinente pour un état si une
proposition de sa ADD-LIST est contenue dans l’état
Exemple:
empiler(x,y)
P: tenir(x), cube(x), cube(y), libre(y)
A: sur(x,y), libre(x), vide(P)
D: libre(y), tenir(x)
est pertinente (empiler(C,B)) pour l’état:
Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Planification-21

Planification non-linéaire
Certains sous-objectifs peuvent
être incompatibles si ils ne sont
pas atteints dans le bon ordre.
Exemple:
1

2

• Si le robot met la clé dans la boîte (2) avant de fermer la
porte (1), l’objectif ne peut pas être atteint

→La planification non-linéaire opère par ordonnancement
partiel des taches en gérant les conflits (cycles et menaces)
Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Planification-22

Planification non-linéaire

Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Planification-23

Planification non-linéaire

Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Planification-24

Planification non-linéaire

Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Planification-25

Planification non-linéaire

Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Planification-26

Planification non-linéaire

Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Planification-27

Planification non-linéaire

Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Planification-28

Planification non-linéaire

Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Planification-29

Planification non-linéaire

Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Planification-30

Planification non-linéaire

Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Planification-31

Planification non-linéaire

Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Planification-32

Planification non-linéaire

Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Planification-33

Planification non-linéaire

Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Planification-34

Planification non-linéaire

Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Planification-35

Planification non-linéaire

Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Planification-36

Planification non-linéaire

Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Planification-37

Planification non-linéaire

Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Planification-38

Planification non-linéaire

Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Planification-39

Planification non-linéaire

Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Planification-40

Planification non-linéaire

Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Planification-41

Résumé
• La planification représente les états comme
des conjonctions de propositions logiques
• Les actions sont des modificateurs
– Précondition
– Add-/Delete-lists

• Le chainage avant souffre d’un facteur de
branchement trop important
• Le chainage arrière régresse de l’objectif vers
l’état initial
• La planification non-linéaire explore un espace
de plans partiels (ordre partiel)
Stephane Marchand-Maillet – University of Geneva – Computer Science

AI Planification-42

