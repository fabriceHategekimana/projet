# Q_6_9_Analyseurs_LR1_table_des_actionsConstruction de la table des action LR(1) comme SLR(1)  
  
**Table des actions**  
indiques 3 actions (sinon erreur):  
	- lecture terminal (décalage)  
	- reduction production (reduction)  
	- acceptation (acceptation)  
ligne 0: états (q)  
colonne 0: terminaux (a)  
cases: actions x transitions (q,a)  
remplissage:  
- pour (q,a) si q contient item avec dot(a) -> décalage  
- si q a item terminal [X->alpha dot()] `et` si terminal a est dans les suivant de X  -> réduction X->alpha dans (q,a)  
- Mettre acceptation dans la case (qf,#)  
- Mettre erreur dans les cases vides  
qf= état final = [S'->S dot()]  
  
La caractéristique est la même pour la table LR(0):  
dans chaque case: unique action ou erreur  
  
