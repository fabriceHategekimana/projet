# Q5_4_transition_de_lecture_transition_d_expansion_ordre_préfixe

Pour faire les transitions, on se sert d'un algorithme particulier.

Si le symbole au sommet de la pile est un terminal:
	Si correspond au symbole de la fenêtre:
		on dépile et on passe
	Sinon
		Echec

Si le symbole au somme de la pile est un non-terminal:
	Si la table contient la transition:
		on dépile et on empile le résultat de la dérivation
	Sinon
		Echec

On est dans un algorithme de lecture descendante LL(k):
Les premiers symboles traités seront tout à gauche.

	
