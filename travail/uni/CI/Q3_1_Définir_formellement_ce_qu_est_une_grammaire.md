# Q3_1_Définir_formellement_ce_qu_est_une_grammaire
Une grammaire est un 4-tuple G= {V_T, V_N, P, S}

- V_t est l'ensemble des symboles terminaux ou l'alphabet formant les mots du langage
- V_N est l'alphabet des symboles non terminaux avec V_T intersection V_N = ensemble_vide
- P est l'ensemble des règles grammaticals, ou production, de la forme alpha->beta où alpha et beta sont des séquence de terminaux ou de non terminaux et où alpha contient au moins un nom terminal
- S est l'axiome ou le symbole initial, un non terminal particulier qui correspond à la racine de la grammaire.

Dérivation:
On appel dérivation en une étape le passage d'une séquence à une autre. Si on a plusieurs productions, on préferera utiliser une étoile sur la flèche.
Soient une grammaire G={V_T, V_N, P, S} et A->B une production de P. La séquence de terminaux et non terminaux alpha.A.beta appartenant à (V_T union V_N)* peut être dérivé en une séquence alpha.B.beta en appliquant la `production.` c-a-d en substituant A par B.

