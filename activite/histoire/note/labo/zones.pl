empire(biologique).
empire(transhumanisme).
empire(ki).
empire(élémentaire).
empire(chimere)

lieu(ecole).
lieu(orphelina).
zone(X) :- empire(X); lieu(X).

voisin(biologique, élémentaire).
voisin(biologique, ki).
voisin(biologique, transhumanisme).
voisin(biologique, chimere)

lieu(parque).
lieu(restaurant).
region(ville).

place(parque).
batiment(ecole).
batiment(orphelina).
batiment(restaurant).
dans(X, ville) :- batiment(X); place(X).
batiment(commissariat).

region(underground).


