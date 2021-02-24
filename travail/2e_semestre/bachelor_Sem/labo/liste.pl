entier(un).
entier(deux).
entier(trois).
entier(quatre).
entier(cinq).
entier(six).
entier(sept).
entier(huit).
entier(neuf).

liste(empty).
liste(cct(N,L)) :- entier(N), liste(L).

#problèmes rencontré avec la définition des séquent traduction pas vraiment évidente en ce qui concèrne l'ordre de mise en place
#Ce qui serait pas mal serait une définition plus explicite des opérateurs dans les termes T_{[symboles]}([ensembles)])
#[symboles] => définit par l'utilisateur
#[ensembles] => choisit par l'utilisateur mais prédéfini par l'outils (entier, float, etc.)

