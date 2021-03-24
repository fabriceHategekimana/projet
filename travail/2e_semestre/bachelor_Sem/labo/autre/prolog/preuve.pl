
liste([]).
liste(conc(n,l)) :- liste(l).

long([], R) :- R is 0.
