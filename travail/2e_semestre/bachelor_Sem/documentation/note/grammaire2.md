calc : premises MINUS MINUS conclusion
premises : fact following
fact : transition
fact : equality
transition : term MINUS SUP term
term : exp
term : state
state : INF suite SUP
suite : exp next
suite : NAME next
suite : VAR next
suite : list next
list : OB exp CB
list : OB suite CB
next : COMA suite
next : 
equality : exp EQUAL exp
following : COMA fact following 
following : 
conclusion : transition
exp : NAME OP exp CP
exp : exp more
exp : NUM
exp : NAME
exp : VAR
more : COMA exp more
more : 
