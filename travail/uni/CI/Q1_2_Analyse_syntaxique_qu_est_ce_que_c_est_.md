# Q1_2_Analyse_syntaxique_qu_est_ce_que_c_est_?

La syntaxe régit la forme des phrases
La définition syntaxique d'un langage s'appuie sur:
- les terminaux, définis au niveau lexical
- les notions non-terminales définissant des règles de bonne forme.

Cela constitu une grammaire

![outils_analyse_lexicale_et_syntaxique](images/outils_analyse_lexicale_et_syntaxique.png)

Reçois de l'analyseur lexical une suite de symboles et y reconnaît la structure du texte.  

Pour reconnaître la structure d'un texte il faut des expressions régulières et des automates à pile (mémorisation à taille bornée) pour les parenthèse et autres.  

Pour une suite d'éléments distribués par l'analyseur lexical. L'analyseur synthaxique va tenter de construire un arbre de dérivation selon la grammaire donnée. S'il n'y parvient pas, il renvoit une erreur.  

L'analyseur synthaxique utilise une pile, une fenêtre et un algorithme pour analyser les séquences qui lui sont données.  

Le symbole de pile initial est l'axiome.  
