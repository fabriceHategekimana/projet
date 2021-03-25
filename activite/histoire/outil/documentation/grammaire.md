# Grammaire

S : num Action
  Action
Action: add modifiy
      | delete modify
	  | check query
	  | display query
modify: fact
	  | rule
fact  : ent ent ent
rule  : if logalg then conj
logalg: fact2 more
more: op fact2 more
	| empty
op: and
  | or
conj: fact2 moreconj
moreconj: and facte2 moreconj
        | empty
fact2: ent ent var
	 | ent var ent
	 | var ent ent
	 | ent var var
	 | var ent var
	 | var var ent
	 
