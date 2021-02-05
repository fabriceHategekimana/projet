# Algorithme_de_Peterson
Sert à l'exclusion mutuelle de deux processus.

on peut le représenter comme un triplet (turn, p0, p1)

Transitions:
demande=> + (-x, ? rang(p0) 1 p0, rang(p1) 1 p1)
lâchement + (0, ? rang)

Aucune exécution ne peut être en interblocage car:
(wantCS[1]=true && turn=1) && (wantCS[0]=true && turn=0)

Il n'y a pas de starvation non plus car quand un a fini, il casse la boucle d'attente de l'autre.

