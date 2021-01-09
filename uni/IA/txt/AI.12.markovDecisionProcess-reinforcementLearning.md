Intelligence Artificielle
Processus de Décision Markoviens
(Markov Decision Process – MDP)

Reinforcement Learning
Stephane Marchand-Maillet

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI MDP-RL - 1

Contenu
• Problématique
• Processus Markoviens

• Processus Markoviens Décisionnels (MDP)
• Apprentissage

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI MDP-RL - 2

Reinforcement Learning (RL)
Apprentissage par renforcement
Definition: “apprendre à faire correspondre des
actions à des situations rencontrées, pour
maximiser une recompense”
Situation = état (state)
Action
Récompense (reward – value - return)
Stratégie (policy)
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI MDP-RL - 3

Différences avec l’apprentissage déjà vu
On n’a pas un ensemble de données annotées (ou non) sur
lequel on apprend
→ Différent de l’apprentissage supervisé (xi,yi)
→ Différent de l’apprentissage non-supervisé (clustering)
On apprend grâce à un signal de récompense (qui peut être
différé)
→ Différent de l’apprentissage « en ligne » (online learning)
Importance de la temporalité (sequence état-actionrécompense-état…)
On fait l’hypothèse d’une propriété Markovienne au moins
approximée
→ On se retrouve dans le contexte des MDP
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI MDP-RL - 4

Exemples d’applications
Voitures autonomes

Jeux de plateau (Go)

Jeux vidéo

[source: wikipedia]

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI MDP-RL - 5

Rappel: Boucle Action-Perception
L’agent percoit son environnement
•
Environnement lui-même
•
Résultat de ses actions (changement)

Perception
(état st)

Contexte
Environnement
Agent
Action
L’agent agit sur son environnement
•
Pour aller vers un but

On va s’intéresser a la dynamique des états (processus) afin d’atteindre un but
(maximiser une «utilité») : on veut estimer un modèle du type «P(st+1|s0,s1,…,st)»
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI MDP-RL - 6

Propriété Markovienne
Definition:
On dit qu’un processus est Markovien si chacun de ses états
représente son historique
P(st+1|s0,s1,…,st) = P(st+1|st)
ht

→ L’état st «encode» l’historique ht des états passés
→La transition d’un état à un autre est indépendante de
l’historique («trajectoire»)
Formellement:
→ Le futur (t+1) est indépendant du passé (0,…,t-1) étant
donné le (conditionnellement au) présent
→ un état est une «statistique exhaustive» (sufficient statistic)
pour le futur du processus
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI MDP-RL - 7

Markov Process (MP)
Markov Process (S,P):
Processus Markovien établi par une probabilité de transition:
• S: Ensemble d’états (discret)
• P: Dynamique ou modèle du processus: P(st+1|st)
• Dynamique Markovienne
• (Pas d’actions, pas de récompense)
Pour un ensemble d’états fini on a la matrice de transition:
Aij=(P(st+1=sj|st=si))ij
Un processus Markovien génère une chaîne de Markov (Markov Chain)
Exemple:
Marche aléatoire (random walk) dans un graphe de matrice
d’adjacence A
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI MDP-RL - 8

Markov chain
Exercice:
• Décrivez le Processus Markovien (S,P)
• Que vaut la matrice de transition A?
• Quelles sont ses propriétés?
• Comment générer une chaine à partir de ce modèle?
• Quelles sont les propriétés de cette chaine?
• Construisez et actionnez un MP plus complexe
[source: wikipedia]

Exemple d'application: Algorithme PageRank
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI MDP-RL - 9

Markov Reward Process (MRP)
On introduit l’idée de récompense (reward) qui permet d’évaluer
(value) une chaine d’états

Markov Reward Process: (S, P, R,g)
Tout au long de la chaîne d’états, l’agent reçoit un signal de
récompense qui l’informe sur la «qualité» de son état:
• S ensemble (fini) d’états (discrets)
• P dynamique de transition: P(st+1|st)
• R fonction de récompense: rt = R(st)
• γ ∈ (0,1) coefficient d’oubli: discount factor
• (pas d’actions)
Exemple: Souris dans un labyrinthe:
• R(«sortie») = +10
Note: La récompense est décalée
(delayed reward) par rapport à
• R(«oubliette») = -10
l'action
• Sinon R(«couloir») = 0
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI MDP-RL - 10

Rappel: Boucle Action-Perception
L’agent percoit son environnement
•
Environnement lui-même
•
Résultat de ses actions (changement)

Perception
st

rt

Contexte
Environnement
Agent
Action
(Dynamique)
L’agent agit sur son environnement
•
Pour aller vers un but

L’agent suit la dynamique du processus P(st+1|st)

L’Agent reçoit une «évaluation» de l’état st à travers une récompense rt
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI MDP-RL - 11

Return
Soit (S,P,R,g) un MRP et étant donné un horizon T, on définit:
• Le Return Gt comme étant la somme amortie des récompenses
obtenues tout au long d’une chaine d’états:
Gt=rt + grt+1 + g2rt+2 + g3rt+3 +… + gT-t+1rT
T est le nombre de pas de temps dans un épisode (activation du
processus)
• Peut être infini
• Sinon on parle de MRP fini
Note: g sert de «facteur d’oubli». Les récompenses passées sont
exponentiellement moins importantes
• g ~ 0 : récompense instantanée seulement
• g ~ 1 : pas d’oubli
• Cas général: évite les valeurs de return infinies

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI MDP-RL - 12

State Value Function
On definit la fonction d’évaluation d’un état s comme
étant V(s), l’espérance du return en partant de l’état s:
V(s) = E[Gt|st = s] = E[rt + grt+1 + …|st = s]

C est le return moyen que je peux espérer en étant à
l’état st et en suivant la dynamique du processus
Note: dans la "recherche adverse",
d'évaluation a une signification similaire

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

la

fonction

AI MDP-RL - 13

Markov Reward Process
0.45

+10

R(S1)

S1

0.2

P(S2|S1)
0.25

S2
0. 5

0.6

0.35

-20
0

0.15

S3
0. 5

0

Stephane Marchand-Maillet – University of Geneva

Probabilité de S1 S2 S1 S3 S3 S2 S1 S3 S3 ?
Return induit?
Calculer la fonction d'évaluation de S1
Intelligence Artificielle

AI MDP-RL - 14

Equation de Bellman pour les MRP
Si:
V(s)

Donc:

= E[rt + grt+1 + g2rt+2 + …|st = s]
= E[rt + g(rt+1 + grt+2 + …)|st = s]
= E[rt + gGt+1|st = s]
= rt + g E[Gt+1|st = s]
= rt + g Ss’P(s’|s)E[Gt+1|st+1 = s’]

V(s) = R(s) + g Ss’P(s’|s)V(s’)

Soit:

(*)

V = R + gPV

sous forme matricielle avec V = [V(si)]i et R = [R(si)]i
(*) permet de rétro-propager la valeur d'un état dans le cadre d'une
récompense décalée (modulo le coefficient d'oubli g)
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI MDP-RL - 15

Résolution analytique
Pour un MRP fini on a un point fixe:
V = R + gPV
Soit :
V = (I- gP)-1R

Cohérent avec:

Pas si simple:
• P est une matrice NxN
• Une inversion de matrice coûte O(N3)
→ Algorithme itératif (prog. dynamique)
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

Exercice: appliquez à
l’exemple précédent

AI MDP-RL - 16

Markov Decision Process (MDP)
On donne à l’Agent le choix de ses actions (décision)

Un processus de décision Markovien (MDP) est un
quintuplet (S,A,P,R,g) ou:
• S est l’espace d’états (discret ou continu)
• A est l’ensemble des actions (discret/continu)
• P(s’|s,a) (modèle ou dynamique) est la probabilité de
transition d’un état à un autre en fonction d’une action
• R(s,a) =E[rt|s,a] est la fonction de récompense (reward
function)
• γ ∈ (0,1) est le coefficient d’oubli (discount factor)
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI MDP-RL - 17

Diagramme d'états/actions/rewards
+10

S1

R(S1,A2)
0.35

S2

0.2

A1

0.6

0.45

A2

S3

0.25
P(S2|S1,A2)

0.15
-20

Un exemple en action: https://github.com/lionelblonde/mdp-toy
Remerciements à Lionel Blondé
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

View from S1
AI MDP-RL - 18

Modèle conceptuel du RL
st

Perception
(état, recompense)
rt

st+1
rt+1

Contexte
Environnement
Agent
Action: at

Durant l’apprentissage:
• En fonction de l’état perçu st, l’Agent effectue une action at qui lui donne
une récompense rt+1 et affecte l’environnement en un état st+1
• L’Agent apprend une stratégie d’action à partir de cette récompense et de
ce nouvel état
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI MDP-RL - 19

Différences avec l’apprentissage déjà vu
On n’a pas un ensemble de données annotées (ou non) sur
lequel on apprend
→ Différent de l’apprentissage supervisé (xi,yi)
→ Différent de l’apprentissage non-supervisé (clustering)
On apprend grâce à un signal de récompense (qui peut être
différé)
→ Différent de l’apprentissage « en ligne » (online learning)
Importance de la temporalité (sequence état-actionrécompense-état…)
On fait l’hypothèse d’une propriété Markovienne au moins
approximée
→ On se retrouve dans le contexte des MDP
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI MDP-RL - 20

Policy (stratégie)
La stratégie (policy p) fait le lien entre l'état courant et l'action à
prendre. C'est l'"intelligence" du processus "état → action"

La stratégie peut être déterministe
p(s) = a
Cas général, stratégie stochastique:
p(a|s) = P(at = a|st = s)
C'est la stratégie qui va faire l'objet de l'apprentissage
Une fois la stratégie p déterminée, on retombe sur un MRP ou la
stratégie se déroule avec:
Rp(s)=Sap(a|s)R(s,a)
Pp(s'|s)=Sap(a|s)P(s'|s,a)
→ On peut définir la valeur d'une stratégie dans le MDP en le
réduisant au MRP correspondant
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI MDP-RL - 21

State diagram and MDP chain
P(A2|S1) = p(A2,S1)

S1

0.7
0.3

0.35

0.2

A1

0.6

0.45

0.25

A2

S3

S2

P(S2|S1,A2)

0.15

Un exemple en action: https://github.com/lionelblonde/mdp-toy
(Remerciements à Lionel Blondé)
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

View from S1
AI MDP-RL - 22

Value functions pour un MDP
State Value: Vp(s) : la fonction d’évaluation d’un état s est
l’espérance du return en partant de l’état s et en suivant
la strategie p:
Vp(s) = Ep[Gt|st = s] = Ep[rt + grt+1 + …|st = s]
State-Action Value: Qp(s,a) : la fonction d’évaluation d’un
état s et une action a est l’espérance du return en partant
de l’état s, prenant l’action a et en suivant la stratégie p:
Qp(s,a) = Ep[Gt|st = s, at = a]
La Q-value (Q = quality) est une évaluation de l’association état-action (state-action pair)

On peut écrire:
Vp(s) = Ea~p(.|s)[Qp(s,a)]
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI MDP-RL - 23

Equation de Bellman pour un MDP
MRP:

L’intégration de la stratégie p permet de généraliser l’équation
de Bellman:
Vp(s) = Sap(a,s)Ss’P(s’|s,a)[R(s,a) + gVp(s’)]
Avec la même approche, l’équation de Bellman s’applique à
Qp:
Qp(s,a) = Ss’P(s’|s,a)[R(s,a) + gSap(a’,s’)Qp(s’,a’)]
(*)
Note : On a

Qp(s,a) = R(s,a) + gSs’P(s’|s,a) Vp(s’)
[on fait l'action a (collecte R(s,a)) et on suit la stratégie p]

C’est la base pour les méthodes itératives d’optimisation de la
stratégie (policy):
• Monte Carlo Learning, Policy iteration, Temporal Difference
Learning
(*) Ici c'est la valeur de l'association état-action que l'on rétro-propage
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI MDP-RL - 24

Optimalité
On définit la fonction optimale d'évaluation d'un
état (optimal state value) par:
V*(s) = maxp Vp(s)
de même (optimal Q-value)
Q*(s,a) = maxp Qp(s,a)
Ce qui définit la stratégie optimale (optimal
policy)
p* = argmaxp Vp(s)
∀ 𝜋 𝑉𝜋∗ 𝑠 ≥ 𝑉𝜋 𝑠
∀𝑠 ∈ 𝑆
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI MDP-RL - 25

Optimal Bellman equation
On met à jour l'équation de Bellman:
V*(s) = maxap(a,s)Ss’P(s’|s,a)[R(s,a) + gV*(s’)]
et
Q*(s,a) = Ss’P(s’|s,a)[R(s,a) + gmaxap(a’,s’)Q*(s’,a’)]
Ce sont des équations non-linéaires (car "max"):
• Value iteration
• Q Learning

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI MDP-RL - 26

Apprendre une Q-Table (Monte Carlo)
Etant donné un labyrinthe (#=mur, O=exit,
X=piège),
l'agent apprend à choisir des actions à chaque
position:
Principe de l'algorithme (apprentissage):
On tire une position de départ et on itère:
• Choix d'une action (permise) aléatoire
• Application de l'action
• Bellman pour l'état actuel → Qtable
Donc, on essaye des chemins et on retropropage la valeur globale de ces chemins:
→ Qtable nous donne la valeur de chaque
action à chaque position
→ On peut évaluer une action
→ On peut suivre les actions les plus
probables
→ On peut échantillonner des trajectoires de
l'agent
Stephane Marchand-Maillet – University of Geneva

[argmax]
Intelligence Artificielle

AI MDP-RL - 27

Echantillonnage de trajectoires

On déduit une stratégie (policy p*) de
la Qtable avec:
p*(a,s) = argmaxp Qp(s,a)
On tire une position de départ (1)
On choisit une action en fonction de la Qtable et on itère jusqu'à un
état terminal (exit ou piège)
→ Code Python sur Moodle)
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI MDP-RL - 28

Policy Iteration
On apprend une stratégie en l'améliorant à
chaque itération:
• p(0)(s)  aléatoire
• Itérer jusqu'à convergence (|p(k+1)-p(k)|<e):
– Evaluation de p(k) par sa value function Vpk
– Amélioration: Qpk(s,a) = R(s,a) + gSs’P(s’|s,a) Vpk(s')
– Nouvelle stratégie:
p(k+1) (s)= argmaxa Qpk(s,a)
[ici on fait l'action a= p(k+1) (s)
et on suit la stratégie p(k)]

On s'assure d'améliorer car:
Qp(k+1)(s,a)≥ R(s,p(k+1) (s)) + gSs’P(s’|s,a) Vpk(s')
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI MDP-RL - 29

Exploitation/Exploration
Ce type d'apprentissage pose le dilemme:
"exploitation vs exploration"
Exploitation: j'exploite ma connaissance au mieux de son
résultat. C est le phénomène "glouton" (greedy): "je fais au
mieux de ce que je sais".
Exploration: j'explore d'autres alternatives pour améliorer ma
performance (au risque de la dégrader).
Ce dilemme est dû au fait que l'agent ne sait pas si il a atteint
le maximum (Q*(s,a) , p*)
Exemple: restaurants
• Exploitation: Je connais certains restaurants de mon
quartier, je vais au meilleur de ceux que je connais
• Exploration: J'essaie un restaurant que je ne connais pas en
espérant qu'il soit encore meilleur (au risque que non)
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI MDP-RL - 30

Stationnarité
En général: stationnaire = Indépendent du temps
• Par exemple p(a,s) = P(at = a|st = s) est une distribution stationnaire
(qui ne dépend pas du pas de temps t auquel on l'applique).
• Ici, on parle de dynamique stationnaire: "les règles d'évolution de
l'environnement ne changent pas au cours du temps".
C est le cas pour les MDP en général (P s'applique a tous les temps t)
• Une stratégie stationnaire (stationary policy) implique que la
stratégie ne change pas par épisode (pas le même temps t)

• En général la stationnarité au moins partielle est une caractéristique
de l'apprentissage. Il est très difficile d'apprendre une règle si elle
change….
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI MDP-RL - 31

Observabilité partielle
L'état peut n'être que partiellement observable:
• Agent qui ne voit que son environnement
proche
• Jeu ou l'adversaire cache son jeu (cartes)
→On parle de POMDP (Partially Observable
Markov Decision Process)
→Solution: on relaxe l'hypothèse Markovienne
pour préserver l'information dans l'historique
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI MDP-RL - 32

Deep RL
• Les réseaux neuronaux (profonds) permettent
l'apprentissage de n'importe quelle fonction
(mapper)
• En particulier on peut se servir de réseaux
pour apprendre Q(s,a)
Exemple: Deep Q Network (DQN)

[From: An End-to-End Automatic
Cloud Database Tuning System Using
Deep Reinforcement Learning.
SIGMOD '19: Proceedings of the 2019
International Conference on
Management of Data June 2019]

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI MDP-RL - 33

Note: Off-policy vs On-policy
Une dichotomie fréquente pour caractériser les
algorithmes:
On-policy: L'algorithme d'apprentissage utilise la stratégie
qu'il optimise au moment de son optimisation
Off-policy: L'algorithme d'apprentissage utilise une autre
stratégie (exple: gloutonne) que celle qu'il optimise au
moment de son optimisation.
Pour aller plus loin:
• Actor-critic, REINFORCE, Policy Gradient, Policy
Optimisation (PO), TRPO, PPO,…
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI MDP-RL - 34

Résumé
L'apprentissage par renforcement (RL) est un type
d'apprentissage particulier:
• L'agent "découvre" son environnement durant
l'apprentissage
• A la fin d'un épisode, l'agent n'aura vu qu'une
partie de son environnement
• Le cœur du RL est la théorie des MDP auxquels
on ajoute l'idée de stratégie (policy)
• Le RL consiste en l'apprentissage de stratégies
• L'apprentissage peut être itératif ou plus
complexe: c ets un domaine de recherche très
actif
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI MDP-RL - 35

Références / Utiles
Ouvrage de référence (online):
Reinforcement Learning: An Introduction. Richard S.
Sutton and Andrew G. Barto. Second Edition MIT
Press, Cambridge, MA, 2018
[http://incompleteideas.net/book/the-book.html]

Cours complet: David Silver, UCL + DeepMind
•
•

https://www.davidsilver.uk/teaching/
https://deepmind.com/learning-resources/-introduction-reinforcementlearning-david-silver

Implémentations: OpenAI baselines:
• https://github.com/openai/baselines
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI MDP-RL - 36

