#Définition des empires et de leur voisinage
empire(biologique).
empire(transhumanisme).
empire(ki).
empire(élémentaire).
empire(chimere)

voisin(biologique, élémentaire).
voisin(biologique, ki).
voisin(biologique, transhumanisme).
voisin(biologique, chimere)

west(biologique).
est(élémentaire).
nord(ki).
sud(transhumanisme).

#Définition des lieux
lieu(ecole).
lieu(orphelina).
zone(X) :- empire(X); lieu(X).
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
