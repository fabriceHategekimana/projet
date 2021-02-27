
Exemple de code:

T(_+_)`[`Entier(`int`)`]`

#Règles
`--` n `in` Entier
n `in` Entier, m `in` Entier `--` n+m `in` Entier

-------------------

T(_::_)`[`Entier(`int`), Liste(`int`)`]`

#Règles
`--` n `in` Entier
`--` [] `in` Liste
n `in` Entier, l `in` Liste `--` n::l `in` Liste
n `in` Entier, m `in` Entier `--` n::m `in` Liste


-------------------

T()`[``]`

#Règles
-- 0 `in` EP
k `in` EP -- k+2 `in` EP

#Preuve
4 appartient à EP

# Programme
$ 4 `in` EP


