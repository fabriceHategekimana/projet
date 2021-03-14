# Grammaire:
## grammaire des expressions:
exp= string "(" exp ")"
   | exp more
   | int
more= "," exp more
    | empty

# forme de grammaire
L -> SFRP

S -> {T TS}
TS -> ,T TS | epsilon
T -> [String]

F -> {O OS}
OS -> ,O OS | epsilon
O -> T[T TS]
R -> {J JS}
JS -> ,J JS | epsilon
J -> [PropLogiq]

P -> {L LS}
LS -> ;; L LS
L -> [chaine]

## Grammaire logique du premier ordre
bien(vim).		vim.bien().		(vim)bien().
ami(a,b).		a.ami(b).		(a)ami(b).

