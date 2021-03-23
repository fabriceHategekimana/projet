# Outil logique

----

# But:

## Au niveau de la gestion:
	- Facilliter le stockage de l'information
	- Facilliter l'accès à l'information

## Au niveau de la rédaction:
	- Automatiser la génération de certaines informations

----

# Qu'est ce qu'on peut faire?

1. Créer des faits
2. Poser des questions
3. Créer des règles

----

# Les faits

## syntax
[sujet] [lien] [cible]

## exemple
Pour dire "Socrate est un homme":
	add Socrate est homme

----

# Les questions

## fonction
On peut maintenant interroger le système pour en récupérer des informations.

## Cas 0
Pour demander "Est ce que Socrate est un homme?":  
	check Socrate est homme

----

# Les variables

## principe
Peut être remplacé par "**qui**", "**quoi**" "**qu'est-ce que**", etc.  

## variables réservées
	A , B , C

**Maximum deux variables dans un fait.**

----

# Autres questions: 1 variable
## Cas 1
check **A** est homme = "**Qui** est un homme?"

## Cas 2
check Socrate **A** homme = "**Quel relation** Socrate a avec 'homme'?"

## Cas 3
check Socrate est **A** = "**Qu'est-ce qu**'est Socrate?"

----

# Autres questions: 2 variables
## Cas 4
check **A B** homme = "**Qu'est-ce qui est relier à **'homme'?"

## Cas 5
check Socrate **A B** = "**Qu'est ce qu'on dit sur** Socrate?"

## Cas 6
check **A** est **B** = "**Qu'est-ce qui** 'est' **quoi?**"

----

# Règles:

## Définition
Crée "l'intelligence" du système.
Système de déduction automatique.
Utilise obligatoirement des variables.

## Syntax
add if [conditions] then [conclusions]

----

# Création d'une règle

## exemple
Pour donner la règle "Tout les hommes sont mortels":  
	add if A est homme then A est mortel
	
## déduction
Le Système poura dire "Alors socrate est mortel!".

----
