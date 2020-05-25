La syntaxe:
===========

La partie visible du langage. Définition des expressions valides.
Composition:
	syntaxe= lexème+structure syntaxique

**Lexèmes**: unités syntaxiques élémentaires (mots-clés, identificateur, opérateur, séparateurs)
**Structure syntaxique**: spécification des séqunces admissibles de lexèmes

## Analyse lexicale (analyseur):
	Reconnaître les lexèmes d'une phrase (expressions régulières)

## Grammaire formelle (générateur):
	catégories syntaxiques et leur relations. 	
	catégories syntaxique= non terminaux.
	symboles finaux= terminaux
	règle d'écriture= production
	
## Définition Formelle (grammaire génératrice):
Quadruplet (N, T, R, a)

* N: **non terminaux**
* T: **terminaux**
* R: **production** (règles grammaticales)
* a: **symbole de départ**
  
 ## Classification de Chomsky
 Classifie les grammaire en 4 types:  
 1. Sans restriction   
 2. Dépendante du contexte  
 3. Indépendante du contexte
 4. Régulière 
   
## sytaxe concrète:  
C'est un peut le code implémenté spécifiquement à un langage.
  
## Syntaxe abstraite  
Liée aux symboles non-terminaux de la grammaire. Sert à donner des types aux données.

## Syntaxe des expressions arithmétiques
Exp= T{ +,*,-,/}(N)
si e appartient à Exp et n appartient à N
alors on note: e -> n <-> (e, n) appartient à eval 
Donc une evaluation eval appartein à Exp x N
