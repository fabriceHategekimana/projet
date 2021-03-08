empire(biologique).
empire(transhumanisme).
empire(ki).
empire(élémentaire).

lieu(ecole).
lieu(orphelina).
zone(X) :- empire(X); lieu(X).

voisin(biologique, élémentaire).
voisin(biologique, ki).
voisin(biologique, transhumanisme).
