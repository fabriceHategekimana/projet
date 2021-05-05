# Documentation

# Principe de base

## Évaluation d'un langage.
Nous avons différentes approches pour l'évaluation de la sémantique d'un langage. L'approche la plus populaire est une évaluation par sémantique opérationnelle, mais nous pouvons aussi avoir une sémantique dénotationnelle ou axiomatique.

Ce travail de bachelor est une tentative pour créer un outil capable de faire une évaluation opérationnelle de la sémantique d'un langage.

## l'outil

L'outil se résume à un petit langage inspiré des règles pour le calcul des séquents et d'une arithmétique basée sur une notation préfixée. Ce langage permet simplement de géré les nombres, les booléens, les chaînes de caractère et les listes.
L'outil est aussi entouré d'un petit "debuger" pour voir pas à pas le parcours d'exécution et pour le visualiser sous la forme d'un graphe.
	
# Présentation de l'outil
## langage

Le langage de l'outils peut se diviser en trois couches:

### Le langage natif:
Est basé sur une notation abstraite basée sur la forme d'une arbre. Ainsi une opération est représenté par un nom suivit d'éléments contenu dans une parenthèse. L'arrité d'un opérateur est juste le nombre d'éléments que cet opérateur peut contenir. Ce langage natif contient les éléments de bases pour gérer:
- les nombres
- les booléens
- les chaînes de caractère
- les listes

### Les règles d'expression
Au dessus du langage natif, l'outil peut comprendre et utiliser des règles de transition pour transformer une expression et en retourner sa valeur. Une rèlge est composée en deux parties:

#### Les prémisses
Contient un ensemble de test logique, est de dérivation mis en conjonction.  
Un test logique est composé d'un membre de gauche (qui peut être une expression à developper) et d'un membre de droite qui est un terminal (un type fini) à comparer. Ces deux membres sont séparés par un comparateur logique.  
Une dérivation est composée d'un membre de gauche (qui peut être une exempleion à developper) est un membre de droite qui est une variable. Les deux membres sont séparés d'une flèche qui indique que le developpement de la parie de gauche sera assigné à la partie de droite.

#### La conclusion
Contient deux membres. Le membre de gauche est en fait l'entête de la règle, c'est une expression composé de terminaux et de variables. Le membre de droite soit une expression composé de terminaux ou de non-terminaux, soit un terminal. 

![langage_ensemble_shema](images/langage_ensemble_shema.png){ width=50% }

### Arithmétique simple
- addition **add(a,b)**   
- soustraction **sub(a,b)**  
- division **div(a,b)**  
- multiplication **mul(a,b)**  


### gestion de liste
liste: [], [1,2,3], ...   

### exemple
**l1= [1,2,3]**, **l2= [4,5,6]**  
- accès **get(l1, 0)**  => 1  
- définition **set(l2, 1, 7)**  => [4,7,6]  
- insertion  **insert(l1, 0)**  => [0,1,2,3]  
- ajout  **append(l2, 7)**  => [4,5,6,7]  
- retrait  **remove(l2, 1)**  => [4,6]  
- retrait  **removeLast(l2)**  => [4,5]  
- retrait  **pop(l2)**  => 6  
- retrait  **pop(l2, 0)**  => 4  

## Autre exemple

![](images/definition_python.png){ width=40% }

### Traduction
```javascript
modify(Tab,Pt,1) -> TabP -- <Tab,Pt,+> => <TabP,Pt>
```


## autres détails

### Nombres:
	- Le langage supporte actuellement les nombres relatifs

### Booléens:
	- Le langage supporte les booléens (True et False)

### Liste:
	- Ne peut contenir que des nombres/variables/booléens

### Variable:
	- Doit obligatoirement commencer par une majuscule

### fonction:
	- Doit obligatoirement commencer par une minuscule


## architecture du projet

![architecture](images/architecture.png)

## Quelques exemples d'utilisation

### factorielle.fa

#### règles
\myRule{}{fact(1)}{1}
\myRule{N>1}{fact(N)}{mul(N,fact(sub(N,1)))}

#### traduction
```javascript
-- fact(1) = 1  
N > 1 -- fact(N) = mul(N,fact(sub(N,1)))
```

### len.fa

#### règles
\myRule{}{len([])}{0}
\myRule{L \rightarrow Lp, Lp \in list}{Len(L)}{add(1,len(removeLast(Lp)))}

#### traduction
```javascript
-- len([]) = 0  
L->Lp, Lp in list -- len(L) = add(1,len(removeLast(Lp)))
```

### max.fa

#### règles
\myRule{A \rightarrow Ap, B \rightarrow Bp, Bp >= Ap}{max(A,B)}{Bp}
\myRule{A \rightarrow Ap, B \rightarrow Bp, Ap >= Bp}{max(A,B)}{Ap}
\myRule{}{maxL([])}{0}
\myRule{}{maxL(L)}{max(pop(L), maxL(removeLast(L)))}

#### traduction
```javascript
A -> Ap, B -> Bp, Bp >= Ap -- max(A,B) = Bp
A -> Ap, B -> Bp, Ap >= Bp -- max(A,B) = Ap
-- maxL([]) = 0
-- maxL(L) = max(pop(L), maxL(removeLast(L)))
```

### Syntaxe State (du domaine sémantique)

#### State
```sql
<e1,...,en>
```

#### State x inst
```sql
<e1,...,en>inst
```

#### Transition
```
<e1,...,en>inst => <i1,...,in>
```

### Le compteur

#### règles
\myRule{Compteur \in number}{<Compteur>plus}{<add(Compteur,1)>}
\myRule{Compteur \in number}{<Compteur>plus}{<sub(Compteur,1)>}

#### traduction
```javascript
Compteur in number -- <Compteur>plus = <add(Compteur,1)>
Compteur in number -- <Compteur>moins = <sub(Compteur,1)>

```

### Le point

#### règles
\myRule{}{<X,Y>gauche}{<sub(X,1),Y>}
\myRule{}{<X,Y>droite}{<add(X,1),Y>}
\myRule{}{<X,Y>bas}{<X,sub(Y,1)>}
\myRule{}{<X,Y>haut}{<X,add(Y,1)>}

#### traduction
```javascript
-- <X,Y>gauche = <sub(X,1),Y>
-- <X,Y>droite = <add(X,1),Y>
-- <X,Y>bas = <X,sub(Y,1)>
-- <X,Y>haut = <X,add(Y,1)>
```

## mode debug

## Principe:
Un peu similaire au trace de prolog.
Le but est de permettre à l'utilisateur de voir pas à pas le developpement de son programme pour trouver les failles.

## Permet de:
- voir l'état de l'exécution
- voir les règles applicables
- visualiser le parcours d'exécution
- (faire des test)

## Interface (visualisation par graphe)

### pyvis
![pyvis](images/pyvis.png)

inspiré de vis.js

## outils de visualisation

## Affichage
	NetworkX + pyvis + vis.js
	
## Document

### Structures:
1. principes de base
2. motivation
3. principes et concepts théorique
4. présentation de l'outils
5. documentation de l'outils
6. conclusions

TODO
glossaire:
- comparateurs logique
