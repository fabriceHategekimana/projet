Intelligence Artificielle
Réseaux Bayésiens
Stephane Marchand-Maillet

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Reseaux Bayesiens 1

Contenu
Réseaux Bayésiens
Inférence exacte
Inférence approximée

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Reseaux Bayesiens 2

Réseau Bayésien
Def: Un réseau Bayésien (Bayes(ian) Network) est
un modèle de graphe de probabilités (PGM) ayant
une structure de graphe dirigé acyclique (DAG)

Exemple: Student Network
Difficulty

Intelligence

Grade

SAT

Letter
(de: Daphne Koller and Nir Friedman, Probabilistic Graphical Models, 2009 )
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Reseaux Bayesiens 3

Exemple: Propagation de risques

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Reseaux Bayesiens 4

Exemple: Le réseau “Asia”

Lauritzen, S. L. and Spiegelhalter, D. J. (1988). Local computations with probabilities on graphical structures
and their application to expert systems.Journal of the Royal StatisticalSociety, Series B, 50:157–224.

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Reseaux Bayesiens 5

Réseau Bayésien
On représente une connaissance à l’aide du réseau
Bayésien et on peut ensuite l’interroger (pour faire
une inférence)
• On considère la probabilité jointe de toutes les
variables
• On développe selon le réseau (factorisation PGM)
• On utilise la règle de la somme (marginalisation)
pour éliminer les variables qui ne nous
intéressent pas

On peut faire une inférence exacte
… ou approximée
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Reseaux Bayesiens 6

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

AI Reseaux Bayesiens 7

Un exemple de réseau
Connaissance:
• On sait que les champignons poussent sous les sapins
• On sait que les déjections d’oiseaux favorisent les champignons
• Si il y a des champignons et que je les trouve, je peux m’en faire une poêlée
• Il peut y avoir des écureuils dans ces bois

Question: Quelle est la probabilité de me faire une poêlée quand je vois un sapin?

Sapin

Oiseau

Ecureuil

Champignon

Poêlée
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Reseaux Bayesiens 8

Inférence
La probabilité jointe est:
P(S,O,C,P,E)=P(E)P(S)P(O)P(C|S,O)P(P|C)
On cherche à estimer (inférer):
P(p,s)
P(p,s)
P(P=p|S=s) = P(p|s)=
=
∝ P(p,s)
P(s) P(p,s)+P(¬p,s)
 on infère les 2 cas P(p,s) et P(¬p,s) pour éviter de calculer le dénominateur
En marginalisant (règle de la somme):
P(p,s)=SeSoScP(s,o,c,p,e)
=SeSoScP(e)P(s)P(o)P(c|s,o)P(p|c)
On note que (on factorise):
P(p,s)= P(s)SoP(o)ScP(c|s,o)P(p|c)SeP(e)
Or: SeP(e)=1
 Constat 1: chaque composante connexe du graphe peut être traitée
indépendamment (les écureuils n’influent pas la poêlée)
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Reseaux Bayesiens 9

Inférence
P(p|s)= a P(s)SoP(o)ScP(c|s,o)P(p|c)
Méthode directe: énumération:

2n facteurs
n: nombre de variables
à marginaliser

P(s)
P(o)
P(¬c|s,o)
P(c|s,¬o)

P(c|s,o)

P(p|c)

P(p|¬c)

Stephane Marchand-Maillet – University of Geneva

So

P(¬o)
P(¬c|s,¬o)

P(p|c)

Sc

P(p|¬c)

Intelligence Artificielle

AI Reseaux Bayesiens 10

Elimination de variables
P(p|s)= a P(s) SoP(o) ScP(c|s,o)P(p|c)
Dépend de s (fixe), p(fixe), o et c (marginalisé)

On crée le facteur fC(o):
fC(o)=ScP(c|s,o)P(p|c)
et on réécrit:
P(p|s)= a P(s)SoP(o) fC(o)
On recommence:
fO() = SoP(o) fC(o)
Ainsi:
P(p|s)= a P(s) fO()
 On organise les calculs en facteurs réutilisables pour
minimiser la redondance (visible sur les grands réseaux)
Exercice: factorisez un PGM plus complexe
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Reseaux Bayesiens 11

Elimination de variables
Algorithme général:
Répéter:
• Choisir une variable X à factoriser
• fX(vars restantes)= Sx P(… X=x …)
jusqu’à épuisement des variables
 l’inférence exacte est toujours #P-Hard (énumération)
 Dans une structure d’arbre, l’inférence est linéaire (en nombre d’entrées
dans les tables de conjonction)
Note:

Arbre
Une seule racine
Stephane Marchand-Maillet – University of Geneva

Poly-arbre (polytree)
chaque nœud a un seul
chemin vers un autre
Intelligence Artificielle

AI Reseaux Bayesiens 12

Inférence approximée
Au lieu de calculer formellement le résultat, on
utilise le réseau pour générer des échantillons
Sapin

Vrai

Faux

0.7

0.3

Oiseau

Sapin

Sapin

Vrai

Oiseau
Champi

Vrai

Faux

0.6

0.4

Oiseau

Faux

Vrai

Faux

Vrai

Faux

V

0.7

0.6

0.4

0.1

F

0.3

0.4

0.6

0.9

Champignon

Poêlée

Champi
Poêlee

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

Vrai

Faux

V

0.8

0.0

F

0.2

1.0

AI Reseaux Bayesiens 13

Inférence approximée
Principe: On utilise le réseau comme un modèle génératif et on
échantillonne P(S,O,C,P) selon les distributions
Exemple:
• On sait que P(S)=0.7, on tire V/F selon cette probabilité  V (par
exemple)
• On sait que P(O)=0.6, on tire V/F selon cette probabilité  F (par
exemple)
• On sait que P(C|S=V,O=F)=0.6. On tire  V (par exemple)
• On sait que P(P|C=V)=0.8  F (par exemple)
 On obtient un échantillon de la probabilité jointe P(S,O,C,P)
Sapin

Oiseau

Champi

Poêlée

Tirage 1

V

F

V

F

Tirage 2

V

V

F

F

…

…

…

…

…

Tirage N

F

V

V

V

 On peut calculer une estimation
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Reseaux Bayesiens 14

Exemple académique

(de: Daphne Koller and Nir Friedman, Probabilistic Graphical Models, 2009 )
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Reseaux Bayesiens 15

Inférence
• Pour inférer des distributions plus complexes
on doit échantillonner avec des procédés du
type Monte-Carlo (MCMC – pas traités ici)
• On peut utiliser la factorisation en fonctions
potentielles Y(X,Y,Z,W) de cliques
• Pour découvrir les cliques dans un réseau
orienté, on doit “moraliser” le graphe

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Reseaux Bayesiens 16

Estimation de paramètres
• Si on connait la structure de G=(V,G)
• Soit qi les paramètres de P X i X γi
Xgi=G-1(Xi), les parents de Xi dans G

• Étant donné un échantillon on cherche à optimiser les paramètres
par maximum de vraisemblance (maximum likelihood)
1
∗
𝜃 = argmax ෍ log 𝑃(𝑥 𝑚 , 𝜃)
𝑀
𝜃
𝑚
• En utilisant la factorisation dans le réseau Bayésien on a:
1
∗
𝜃 = argmax ෍ ෍ log 𝑃(𝑥𝑖𝑚 |𝑥𝛾𝑚𝑖 , 𝜃𝑖 )
𝑀
𝜃
𝑚
𝑖
• Comme chaque facteur est indépendant (par définition), on peut
dissocier les problèmes en M problèmes indépendants et le
résoudre analytiquement
– par exemple si P Xi Xγi est Gaussien, on utilise la moyenne et la
variance pour estimer qi
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Reseaux Bayesiens 17

Implémentation / simulation
On peut utiliser un simulateur:
Par exemple: http://www.openmarkov.org/

http://www.openmarkov.org/docs/tutorial/openmarkov-tutorial.pdf
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Reseaux Bayesiens 18

Résumé
• Les réseaux Bayésiens sont des PGM dirigés acycliques
• Ils sont le support à la factorisation de probabilité jointe
• Ils permettent de répondre à des requêtes par inférence

• L’inférence exacte est prohibitive sauf dans le cas des
réseaux en arbre
• On peut utiliser l’échantillonnage pour faire de l’inférence
approximée
 MCMC, Gibbs sampling, Variational Inference
Details:
Christopher M. Bishop, Pattern Recognition and Machine
Learning, 2006
Daphne Koller and Nir Friedman, Probabilistic Graphical
Models, 2009
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Reseaux Bayesiens 19

