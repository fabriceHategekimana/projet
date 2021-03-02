
Exemple de code:

# Terme
T(_+_)`[`Entier(`int`)`]`

##Axiom
`--` n `in` Entier

##Induction
n `in` Entier, m `in` Entier `--` n+m `in` Entier

-------------------

# Terme
T(_::_)`[`Entier(`int`), Liste(`int`)`]`

#Règles
`--` n `in` Entier
`--` [] `in` Liste
n `in` Entier, l `in` Liste `--` n::l `in` Liste
n `in` Entier, m `in` Entier `--` n::m `in` Liste


-------------------

# Terme
T()`[``]`

#Règles
-- 0 `in` EP
k `in` EP -- k+2 `in` EP

#Preuve
4 appartient à EP

# Programme
$ 4 `in` EP

-------------------

matrice="1,2;3,4M"
matrice="(\d,)\+(;)\*dM"

T{_+_,_-_}(Matrice(matrice))
