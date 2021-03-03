## Sémantique Bachelor

Définir un objectifs: gitlab

[planning](planning)

**But:**
Créer un outils d'inférence

Développement d'un outil pour définir les règles sémantiques d'un langage de programmation et les dériver méchaniquement (comme le calcul des séquents).

150 heures fin-juin (terminé)
Roulement chaque semaine présentation

[séquents](http://logitext.mit.edu/main)

forme:
prémisses
----------
Conclusion

[etude](etude)

Les prémisses sont des conjonction de prédicat
Les variables apparaissant dans les prédicats sont implicitement quantifiées universellement

Déduction = induction en sens inverse

**Ce que j'ai commencé:**
Revu slide du cours de sémantique (exemple concret d'application)
Tentative de définition et d'implémentation de quelques concepts de langage
étude du logiciel coq

**objectifs/méthodologie:**
- construire un langage et sa synthaxe pour l'évaluation
- créer un système d'inférence/dérivation assez pédagogique
- développer un mode d'emploie pour cet outil

mar 23 fév 2021 22:14:09 CET
Tenter de tester les éléments donnés dans le cours avec prolog puis voire une meilleur sémantique (voir synthaxe) pour le système de dérivation.

Labo: fait avec la définition de la liste dans le slide 4 p.26.
Remarques: 
- le système se note un peu à l'envers que la notation par séquents.
- Il faut trouver un moyen de définir nos propres symboles comme pour le système T_{[symboles]}([ensembles])
- Apprendre d'avantage sur ce que prolog peut faire et essayer de faire (plus adapté) pour le cours.
- Essayer d'en apprendre plus sur l'outil coq, qui me permettra de mieux créer les définitions.

sam 27 fév 2021 20:34:29 CET
Tentative de définition d'une liste, de fonctions de liste ainsi que leur dérivation.
J'ai finalement adopté la notion de terme comme "instruction de précompilation"
Remarque: Il faut faire attention à distinguer opérateur et type (comme élément de syntaxe) pour définir les listes

J'ai pu définir la structure d'une règle en tant que transition (représente aussi un opérateur):
	- règle(conditions, conclusion):
	    - conditions: conjonctions de prédicats
	    - conclusion: liste de prédicat/instructions à exécuter
	    - prédicat: souvent de type "element1 symbole element2"
J'ai pu avoir une première définition de l'état du système:
	- système(context, instruction, type)



