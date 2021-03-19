# Outils éditeur

Langage:

**proposition:**
	sujet lien cible

**règle:**
	`Si` A `et` B `et` C `alors` D
	
Concept:
**Héritage et induction:**
Quand on écrit une règle, on aimerai qu'elle s'applique dans les deux sens:
1. Héritage: Quand une condition est respectée, les conclusions sont sauvegardés dans la base
2. Induction: Pour vérifier une conclusion, on applique l'exploration

On a trois forme de règle:
1. uni to uni (unidirectionnel)
2. multi to uni (bidirectionnel)
3. uni to multi (bidirectionnel)

Si D alors A et B et C
Si A et B et C alors D

## Arithmétique logique:
L'utilisateur à le droit d'entrer pas mal de formule, mais il se doit de suivre cette structure:
- Toute proposition doit être en forme normal disjonctive
Donc (A1 et ... et An) ou (B1 et ... et Bm) ou ...
Sinon le reste sera considéré comme une erreur.

## Algorithme de conversion langage à SQL

Utiliser
UNION pour le OR
CROSS JOIN pour le OU
JOIN pour les variables liées

**algo:**
1. groupement
2. comptage des groupe
3. sélection d'un schéma
4. développement dans le schéma

Propriété:
Comme les relations sont binaire et pour le principe de récursivité. L'utilisateur a le droit à maximum 3 Variables dans ses propositions.

- S'il y a 3 variables, cela doit suivre cette forme:
	- A->B et B->C
- S'il y a 2 variables, c'est plus libre mais elles doivent au moins être liés une fois. ("A et B" est faux par exemple)

On a 4 groupe pour le regroupement:

| id | groupe |
|----|--------|
| 0  | A      |
| 1  | A-B    |
| 2  | B      |
| 3  | B-A    |

chaque numéro n est lié à son voisin n+1, sauf 3 qui est lié à zéro (liaison cyclique)

Il suffit alors de regrouper toutes les propositions en groupe et de les ordonné pour le choix d'un schéma.

J'ai pu faire le compte et on a 15 schéma possible selon les cas d'apparition de groupe (on enlève le cas où il y a zéro groupe car il n'y a rien à faire dans ce cas):

| nb grp | cas               |
|--------|-------------------|
| 4      | 0123              |
| 3      | 012,013,230,123   |
| 2      | 23,13,12,30,02,01 |
| 1      | 0,1,2,3           |
| 0      | -                 |



## algorithme d'intégration d'une règle ou d'un fait
Rétropropagation (intégration de règle):
Quand une règle est entrée, elle s'applique à tout les faits de la base de donées.

Propagation (intégration de fait):
Quand un fait est entrée elle s'exécute avec toutes les règles de la base de données.


Plus tard:
- Changer la grammaire pour limiter à la forme normal disjonctive. 
- Faire des tests à la main de traduction d'expressions de plus en plus complex et établir une table de transition
