# axiom, regle

complet(N) :- unair(N); binair(N).
incomplet(N) :- binair(N).
vide(N) :- unair(N); binair(N).

action(update).
action(check).

proposition(action).

regle(proposition).
axiom(proposition).


