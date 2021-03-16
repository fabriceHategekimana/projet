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

GRAMMAIRE

S : CHECK
  | ADD
CHECK : "check" LOGARI
ADD : "add" AXIOM
    | "add" RULE
AXIOM : PREDICAT
RULE : "if" LA
     | "if" P
LA : LOGARI "then" PREDICAT
P : PREDICAT "then" PREDICAT
  | PREDICAT "then" LOGARI
PREDICAT : `subject` `adj` GOAL
GOAL : `goal`
     | `empty`
LOGARI : F G
G : "and" LOGARI
  | "or" LOGARI
  | `empty`
F : "(" LOGARI ")"
  | "not" "(" LOGARI ")"
  | PREDICAT

Reste l'arithmétique logique

Utiliser
UNION pour le OR
CROSS JOIN pour le OU
