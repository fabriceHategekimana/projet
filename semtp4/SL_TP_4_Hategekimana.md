
\newcommand{\rectangle}[3]{\node (#1) [boite, xshift= #2 cm, yshift= #3 cm] {#1};}
\newcommand{\fleche}[3]{\draw[thick,->] (#1) -- (#2) node[midway,sloped,below, rotate=0] {#3};}
\newcommand{\flechel}[5]{\draw[thick,->] (#1) to [out=#4, in=#5] node[midway, sloped, below, rotate=0] {#3} (#2);}

FORTH
=====

## Exercice 1 Manipulation de pile
1. Définissez, sous forme de règles d'inférence, la syntaxe abstraite du langage de manipulation de pile décrit ci-dessus.  
-Nous traitons le cas d'une pile qui accueil de nombres naturels. Le langage n'est constitué que d'instructions simples (empty push top pop)

empty \infer{expr \xrightarrow{} empty}{expr }  
push \infer{expr \xrightarrow{} push(p,e)}{expr }  
top \infer{expr \xrightarrow{} top(p)}{expr }  
pop \infer{expr \xrightarrow{} pop(p)}{expr }  

2. Donnez la sémantique d'évaluation de ces opération sous la forme de règles d'inférence, en précisant bien le domaine sémantique.
-Le domaine sémantique concèrne le sommet de la pile et le reste de la pile.  
On a donc $$Pile \in (sommet,reste)$$
Les opération pile vide (empty) et concaténation \_::\_. Elle s'applique sur une pile d'entier. On a donc$$T_{empty,\_::\_}(\mathbb{N})$$.

$$ p \in Pile,  n \in \mathbb{N}$$

empty \infer{empty \in Pile}{ }  
push \infer{p \xrightarrow{push(p,e)} n::p}{ }  
top \infer{n::p \xrightarrow{top(p)} n}{ }  
pop \infer{n::p \xrightarrow{pop(p)} p}{ }  

3. Écrivez en LogicKit ou Prolog les règles permettant de manipuler une pile.
-

## Exercice 2: Avec des GOTOs...
1. Quel est le résultat du programm suivant? Détaillez les étapes d'exécution de manière informelle.
```
1 1 2 + + LABEL=1 4 - JUMP=1 5 +
```
-Le résultat est 1.
```
1. Tout d'abord on rempli la pile (de bas en haut) de 1,1 puis 2
2. On addition 2 et 1 (les deux premier nombres de la pile) on obtient 3 qu'on pose à la place des deux autres.
3. On addition on addition 3 et 1 (les deux premier nombres de la pile) on obtient 4 qu'on pose à la place des deux autres.
4. On dépose un label 1 à cet étape du calcule.
5. On pose 4 au sommet de la pile (on a de bas en haut 4,4).
6. On soustrait les deux premiers nombres de la pile et on obtient 0 qu'on pose à la place des deux autres.
7. Comme la valeur est à 0 on saute au label un et on recommence à partir du point 5.
8. On fait donc comme au point 5 et 6, on ajoute 4 au sommet et on soustrait pour obtenir -4 qu'on met au sommet de la pile.
9. Le résultat n'est pas 0 donc on continue.
10. On ajoute 5 au sommet et on fait l'addition (-4 + 5) et on obtient 1.
```

2. Donnez la syntaxe concrète de ce langage en notation EBNF  
EBNF:  
$$<COMMANDE>:= (<NUMBER>^+ <OP>^*)^*$$
$$<OP>:= <OPP>|<GOTO>$$
$$<OPP>:= <ARITHMETIC><KEY>$$
$$<GOTO>:= LABEL=<N> | JUMP=<N>$$
$$<N>:= <NUMBER>^+$$
$$<ARITHMETIC>:= +|-|*|/$$
$$<KEY>:= SWAP|DUP|OVER|DROP$$
$$<NUMBER>:= (0..9)^*$$

3. Donnez la syntaxe abstraite de ce langage sous forme de règle d'inférence.
expression \infer{expr \xrightarrow{} terme expr}{ }  
number \infer{terme \xrightarrow{} n}{ }  
SWAP \infer{terme \xrightarrow{} SWAP}{ }  
DUP \infer{terme \xrightarrow{} DUP}{ }  
OVER \infer{terme \xrightarrow{} OVER}{ }  
DROP \infer{terme \xrightarrow{} }{ }  
LABEL=\<N> \infer{terme \xrightarrow{}LABEL=<N>}{ }  
JUMP=\<N> \infer{terme \xrightarrow{} JUMP=<N>}{ }  

4. Donnez la sémantique d'évaluation d'un programme FORTH avec les instructions JUMP et LABEL.

$$ p, p'\in Pile,$$ $$ n, n' \in \mathbb{N}$$

empty \infer{empty \in Pile}{ }  
number \infer{p \xrightarrow{n} n::p \in Pile}{ }  
SWAP \infer{n::n'::p \xrightarrow{SWAP} n'::n::p \in Pile}{ }  
DUP \infer{n::p \xrightarrow{DUP} n::n::p \in Pile}{ }  
OVER \infer{n::n'::p \xrightarrow{OVER}n'::n::n'::p \in Pile}{ }  
DROP \infer{n::p \xrightarrow{DROP} p \in Pile}{ }  
LABEL=\<N> \infer{p \xrightarrow{LABEL=<N>} (rien)}{ }  
JUMP=\<N> \infer{p \xrightarrow{JUMP=<N>} (rien)}{ }  

5. Écrivez en LogicKit ou Prolog les règles correspondantes.

## Exercice 3: Et avec des fonctions:
1.Évaluez le programme suivant de manière informelle: 
```
: CARRE DUP * ; ( definition de CARRE )
11 CARRE	( on obtient 121 en sommet de la pile )
```
a. Dans la première ligne, on crée la fonction carré qui duplique le premier élément de la pile et qui fait ensuite une multiplication.
b. Dans la deuxième ligne, on rempli d'abord la plie du chiffre 11.
c. On lance ensuite la fonction CARRE qui va multiplier 11 avec lui-même (ce qui va donner 121)

2. Donnez la syntaxe concrète de ce langage en notation EBNF.
C'est comme le deuxième exercice (question 2.), mais on enlève la partie avec le \<GOTO> et on ajoute une partie concernant la partie \<FUNCTION>.
Je ne vais pas réécrire ce que j'ai fait mais je montre les principaux changements:

$$<COMMANDE>:= <FUNCTION>^+ (<NUMBER>^+(hello) <OP>^*)^*$$
$$<FUNCTION>:= :<COMMANDE>;$$

3. Donnez la syntaxe abstraite de ce langage sous forme de règle d'inférence.
FUNCTION \infer{FUNCTION \xrightarrow{} expr}{ }  

4. Donnez la sémantique d'évaluation d'un programme FORTH avec fonctions.
C'est comme avant mais, pour la partie function:

FUNCTION \infer{p \xrightarrow{FUNCTION} p'}{ }  

5. Écrivez en LogicKit ou Prolog les règles correspondantes.

6. Est-t-il possible d'avoir des fonctions récursives? Que peut-t-il se passer?
Oui, il est possible d'avoir des fonctions récursives, mais ce n'est pas du tout recommandable puisque le langage définit n'a pas de structure de contrôle pour arrèter la récursion (comme des structures conditionnelles vu que le GOTO ne compte plus).
À cause de ça, ce qui se passerai serait une boucle infinie qui ne s'arrêterait pas.

## Exercice 4: Conditionnelles
1. Quell différence y a-t-il par rapport au GOTO vu précédement?
-Ici, on perd l'aspect récursif mais on peut maintenant  mettre une cascade de test conditionnel et prendre plusieurs décisions à partir de là.
De plus, si nous disposons des fonctions, nous pouvons malgré tout retrouver la récursivité précédement perdu.

2. Donnez la syntaxe concrète de ce langage en notation EBNF.
C'est comme l'exercice 2 (question 2.) avec quelques modifications.
On ajoute un domaine condition et le reste comme suite:
$$<CONDITION>:= DUP <NUMBER> <OPTEST> IF ."<CARACTER>"<ELSE>THEN$$
$$<ELSE>:= (ELSE <CONDITION>)^*."<CARACTER>"$$
$$<OPTEST>:= <|>|=|<=|>=|!=$$
$$<CARACTER>:= ((a..z)^*(A..Z)^*(0..9)^*)^*$$

3. Donnez la syntaxe abstraite de ce langage sous forme de règle d'inférence.
expr \infer{expr \xrightarrow{} CONDITION}{ }  
CONDITION \infer{CONDITION \xrightarrow{} ELSE}{ }  
ELSE \infer{ELSE \xrightarrow{} CONDITION}{ }  

4. Donner la sémantique d'évaluation d'un programme FORTH avec conditions.  
CONDITION \infer{p \xrightarrow{CONDITION} N \in Caractères}{ }  

5. Écrivez en LogicKit ou Prolog les règles correspondantes.

