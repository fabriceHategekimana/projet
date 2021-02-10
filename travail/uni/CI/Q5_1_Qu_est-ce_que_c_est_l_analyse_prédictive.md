# Q5_1_Qu_est ce_que_c_est_l_analyse_prédictive
Est basée sur le déterminisme du langage.

L'analyseur peut prédire la production à utiliser.

Fonctionne avec les grammaire LL(k), on s'arrête à K=1

Se base sur les fonctions de prédiction Premier() et Suivant()

L'analyse prédictive à quelques méthode qu'on a vu en cours:
L'analyse déscendante LL(1)
L'analse ascendante LR(0), SLR(1), LR(1)

Le point clé de cette analyse prédictive est l'utilisation d'une table d'analyse qui permet de déterminer la transition ou l'action à faire.
