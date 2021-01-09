Graphes Computationnels
Différentiation automatique
Rétropropagation
Chapitre
Réseaux de Neurones Artificiels (Artificial Neural Networks – ANN)
Stephane Marchand-Maillet

Intelligence Artificielle
Graphes Computationnels
Différentiation automatique
Rétropropagation
Chapitre
Réseaux de Neurones Artificiels (Artificial Neural Networks – ANN)
Stephane Marchand-Maillet

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Neural Nets - 2

Rappel: Backpropagation
On a:
𝜕L 𝜕𝜙𝑗𝑙 𝜕L
𝑙
𝑙 𝜕L
=
= 𝜙𝑗 (1 − 𝜙𝑗 ) 𝑙
𝜕𝑎𝑗𝑙 𝜕𝑎𝑗𝑙 𝜕𝜙𝑗𝑙
𝜕𝜙𝑗

(1)

De plus:
𝑁𝑙

𝑁𝑙

𝜕𝑎𝑗𝑙 𝜕L
𝜕L
𝑙−1 𝜕L
𝑙−1 = ෍
𝑙−1
𝑙 = ෍ 𝑤𝑘𝑗
𝜕𝜙𝑘
𝜕𝜙𝑘 𝜕𝑎𝑗
𝜕𝑎𝑗𝑙

(2)

𝜕𝑎𝑗𝑙 𝜕L
𝜕L
𝑙−1 𝜕L
=
=
𝜙
𝑘
𝑙−1
𝑙−1
𝜕𝑤𝑘𝑗
𝜕𝑤𝑘𝑗
𝜕𝑎𝑗𝑙
𝜕𝑎𝑗𝑙

(3)

𝑗=1

𝑗=1

Finalement:

→ On utilise l’itération de (1) et (2) (en partant de l’erreur à la couche L: L( 𝜙𝑗𝐿 𝑥𝑖 , 𝑦𝑖 ) pour inférer
𝜕L
𝜕L
toutes les valeurs de 𝑙 et 𝑙
𝜕𝜙𝑗

𝜕𝑎𝑗

→ On peut calculer les gradients:

𝜕L
𝑙−1
𝜕𝑤𝑘𝑗

pour toutes les couches (3)

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Neural Nets - 3

Outil 1: Graphe computationnel
Représente le calcul d'une fonction
Nœuds: variables et operateurs (résultats intermédiaires)
Arcs: dépendances dans le calcul
[idée similaire à celle d'un arbre syntaxique]

Exemple simple:

f(x,y,z) =

x2(x+y-z)

on veut

𝜕 f 𝜕f 𝜕f

,

,

𝜕𝑥 𝜕𝑦 𝜕𝑧

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Neural Nets - 4

f(x,y,z) =

x2(x+y-z)

on veut

x

2
a1
=
x
^2

y

+ a2 = x+y

z

𝜕f 𝜕f 𝜕f

,

,

𝜕𝑥 𝜕𝑦 𝜕𝑧

* f(x,y,z)= a1*a3

- a3 = a2-z

On construit le graphe en définissant des variables intermédiaires (ici a1, a2, a3)
A chaque niveau (couche), la fonction ne s'exprime qu'en fonction des résultats de la couche précédente
NB: cette étape correspondrait à la transcription de notre équation de réseau en un graphe.
Exercice écrivez le graphe d'un neurone:
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Neural Nets - 5

f(x,y,z) =

x2(x+y-z)

on veut

𝜕f 𝜕f 𝜕f

,

,

𝜕𝑥 𝜕𝑦 𝜕𝑧

16

x

2
a1
=
x
^2

4
96

11

y

+ a2 = x+y

* f(x,y,z)= a1*a3

7

z

- a3 = a2-z

5

6

Propagation: On peut se servir du graphe pour calculer la valeur de la fonction pour certaines valeurs des
paramètres (ici on donne des valeurs à x,y,z)
NB: cette étape correspondrait à activer le réseau pour une ou plusieurs données d'entrée (xi = [xki])
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Neural Nets - 6

f(x,y,z) =

x2(x+y-z)

on veut

x

2
a1
=
x
^2

y

+ a2 = x+y

z

𝜕a2
𝜕𝑥

=1

𝜕a2
𝜕𝑦

𝜕f 𝜕f 𝜕f

,

,

𝜕𝑥 𝜕𝑦 𝜕𝑧

𝜕a1
= 2𝑥
𝜕𝑥

* f(x,y,z)= a1*a3
𝜕f
𝜕𝑎1

=1

= 𝑎3

𝜕f
𝜕𝑎3

= 𝑎1

- a3 = a2-z
𝜕a3
=
𝜕𝑎2

1

𝜕a3
=
𝜕𝑧

−1

On peut aussi calculer toutes les dérivées "locales" (en rouge) de la fonction à chaque noeud en fonction des variables
intermédiaires dont elle dépend (couche précédente)
𝜕a3
Note: les termes n'ayant pas de chemin entre eux sont = 0 (exple: 𝜕𝑎1 = 0)

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Neural Nets - 7

f(x,y,z) =
𝜕f
=
𝜕𝑥
𝜕f 𝜕a1 𝜕f 𝜕a3 𝜕a2
+
𝜕𝑎1 𝜕𝑥 𝜕𝑎3 𝜕𝑎2 𝜕𝑥

x2(x+y-z)

on veut

x

2
a1
=
x
^2

y

+ a2 = x+y

z

𝜕a2
𝜕𝑥

=1

𝜕a2
𝜕𝑦

𝜕f 𝜕f 𝜕f

,

,

𝜕𝑥 𝜕𝑦 𝜕𝑧

𝜕a1
= 2𝑥
𝜕𝑥

* f(x,y,z)= a1*a3
𝜕f
𝜕𝑎1

=1

𝜕f
𝜕𝑎3

= 𝑎3

= 𝑎1

- a3 = a2-z
𝜕a3
=
𝜕𝑎2

1

𝜕a3
=
𝜕𝑧

−1

De cette façon, on retrouve bien la procédure (formule) de dérivation composée:
• On part du niveau le plus profond et on remonte (rétropropage) en suivant chaque chemin (ici vert et rouge) en
• multipliant a chaque noeud traversé
• ajoutant à chaque jonction
𝜕f
𝜕𝑥

=

𝜕f 𝜕a1
𝜕f 𝜕a3 𝜕a2
+
𝜕𝑎1 𝜕𝑥
𝜕𝑎3 𝜕𝑎2 𝜕𝑥

= a3(2x)+a1(1)(1) = (a2-z)2x + x2 = (x+y-z)2x + x2
Stephane Marchand-Maillet – University of Geneva

Somme sur les chemins entre f
et x (rétropropagation)

Intelligence Artificielle

AI Neural Nets - 8

f(x,y,z) =

𝜕f
𝜕f 𝜕a3 𝜕a2
=
𝜕𝑦 𝜕𝑎3 𝜕𝑎2 𝜕𝑦

x2(x+y-z)

on veut

x

^2

y

+ a2 = x+y
𝜕a2
𝜕𝑥

z

=1

𝜕a2
𝜕𝑦

𝜕f 𝜕f 𝜕f

,

,

𝜕𝑥 𝜕𝑦 𝜕𝑧

* f(x,y,z)= a1*a3
𝜕f
𝜕𝑎1

=1

= 𝑎3

𝜕f
𝜕𝑎3

= 𝑎1

- a3 = a2-z
𝜕a3
=
𝜕𝑎2

1

𝜕a3
=
𝜕𝑧

−1

Autre exemple (à développer)

NB: On a toujours la possibilité de vérifier avec la méthode de différentiation "classique"

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Neural Nets - 9

f(x,y,z) =

x2(x+y-z)

on veut
16

^2 a1

x

𝜕f 𝜕f 𝜕f

,

,

𝜕𝑥 𝜕𝑦 𝜕𝑧

8
𝜕a1
= x2
= 2𝑥
𝜕𝑥

4
96

11

* f(x,y,z)= a1*a3

+ a2 = x+y

y

𝜕a2
𝜕𝑥

7

=1

𝜕a2
𝜕𝑦

𝜕f
𝜕𝑎1

=1

𝜕f
𝜕𝑎3

= 𝑎1

16

6

6

z

= 𝑎3

- a3 = a2-z
𝜕a3
=
𝜕𝑎2

5

1

𝜕a3
=
𝜕𝑧

−1

Finalement grâce aux valeurs propagées (bleues) on peut maintenant retro-propager les valeurs des
dérivées (vertes)
𝜕f
𝜕𝑥

6

=

8

16 1

1

𝜕f 𝜕a1
𝜕f 𝜕a3 𝜕a2
+
𝜕𝑎1 𝜕𝑥
𝜕𝑎3 𝜕𝑎2 𝜕𝑥

= a3(2x)+a1(1)(1) = (a2-z)2x + x2 = (x+y-z)2x + x2= 64

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Neural Nets - 10

Différentiation automatique
Soit u=(u,u’) et v=(v,v’) avec:
• u+v = (u+v, u’+v’)
• u.v = (uv,u’v+v’u)
• un = (un, nun-1)
• a.u = (a.u,au’)
• cos(u) = (cos (u), u’sin(u))
• …
Exemple: f(x)=3x2+2x-1, calculer f’(3)
x = (3,0) → f(x) = f((x,1))=3(x,1)2+2(x,1)-1(1,0) = 3(x2,2x)+(2x,2)-(1,0)
→ f((3,1)) = (27,18)+(6,2)-(1,0) = (32,20) = (f(3),f’(3))

Calculer f’(10): f((10,1))=(300,60)+(40,2)-(1,0)=(339, 62)
Exercice: Pour f(x)=cos(2x)exp(3x2-2x+3), calculer f’(12)
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Neural Nets - 11

Solution
f(x)= cos(2x).exp(3x2-2x+3)
• j(u) = j((u,u’)) = (j(u),u’j’(u))
f(x) = f((x,1))= cos(2.(x,1)).exp(3(x,1)2-2(x,1)+3(1,0))
=(cos(2x),2sin(2x)).(exp(3x2-2x+3),(6x-2)exp(3x2-2x+3))

f((12,1))=(cos(24),2sin(24))(e411,70e411)
= (cos(24)e411, 2sin(24) e411+70e411cos(24))
=(cos(24) e411, 2e411 (sin(24)+35cos(24))
→f’(12)=2e411 (sin(24)+35cos(24)

f((2,1)) = (cos(4) e11,2sin(4)e11+10e11cos(4))
→ f’(2)=2e11(sin(4)+5cos(4))
Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Neural Nets - 12

Utilisation dans notre exemple

x

^2 a1 =

x2

(x,x')=(4,0)

y
(7,0)

=1

(x+7,1)=(11,1)

z
(5,0)

Nos nouveaux objets
"remplacent" les dérivées
locales (facilitent la gestion)

𝜕a1
= 2𝑥
𝜕𝑥
(x2,2x) = (16,8)

* f(x,y,z)= a1*a3

+ a2 = x+y
𝜕a2
𝜕𝑥

𝜕a2
𝜕𝑦

f(x,y,z) = x2(x+y-z)

=1

(4+y,1)=(11,1)

𝜕f

𝜕f

= 𝑎3
𝜕𝑎1

𝜕𝑎3

= 𝑎1

(6a1,6) = (96,6) (16a3,16) = (96,16)

- a3 = a2-z
𝜕a3
=
𝜕𝑎2

𝜕a3
1
= −1
𝜕𝑧
(a2-5,1)=(6,1) (11-z,-1)=(6,-1)

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Neural Nets - 13

En pratique: rétropropagation
y(u)=u2
(u est l'entrée de la fonction.
𝜕Y
= 2𝑢 u=x dans ce cas)
𝜕𝑢

x

4 1*6*(2*4)

64

(somme)

y

16

1*6

1*16*1*1

7
1*16*1*1

16

z

^2

+

11

1*16*1
5

1*16*(-1)

𝜕f
𝜕𝑦

= 𝑥2

1*16

y(u)=u-z
𝜕Y
=1
𝜕𝑢

-

y(u)=a3*u=6u
𝜕Y
= 𝑎3 = 6
𝜕𝑢

*

𝜕f
𝜕𝑧

96

f(x,y,z)

y(u)=a1*u=16u
𝜕Y
= 𝑎1 = 16
𝜕𝑢

1
(départ de retropropagation)

6

y(u)=a2-u
𝜕Y
= −1
𝜕𝑢

-16

16

f(x,y,z) = x2(x+y-z)

-16

1- Propagation des valeurs
2- Rétropropagation des dérivées
Produit le long des chemins
Somme aux jonctions

= −𝑥 2

Stephane Marchand-Maillet – University of Geneva

Intelligence Artificielle

AI Neural Nets - 14

