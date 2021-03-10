ki(a).
arme(a).
ki(b).
arme(c).

ka(N) :- ki(N), arme(N).
ki(N),arme(N) :- ka(N).
