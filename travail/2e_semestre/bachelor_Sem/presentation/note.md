# But: 
**Créer un outils pour:**

	- Définir la sémantique d'un langage
	- En voir ses dérivations

----

# Actuellement(1):
**Défini une syntax de base:**

	- Inspirée du jugement
	- Inspirée de l'ensemble termes typé 

----

## Définition (Termes)
L'ensemble des termes construit sur un domaine D de type avec l'ensemble des opérateurs OP (muni d'une arité) seront notés $$ T_{OP}(D) $$ Les termes sont définis inductivement par:
	$$ D \subseteq T_{OP}(D) $$

## Définition (Jugement)
$$ \frac{Prop_1,...,Prop_n}{Type, Valeur} $$

----

# Syntaxe

## Terme
```json
S= {bool,nat}
F= {
    True[empty,bool],
    not[bool,bool],
    and[bool,bool,bool]
}
```

## Axiom
```python
-- n in Entier
```

## Induction
```python
n in Entier, m in Entier -- n+m in Entier
```

## Programme
```python
Programme1 { inst1;;inst2;;...;;instn }
```

----

# Actuellement(2)
**Définition de l'algo de dérivation de programme:**

	- Basé sur le modèle d'interpréteur
	- Utilisation d'une grammaire algébrique
	 
----

# À faire:

 - Ajouter la notion de contexte
 - définition de l'algo de preuve

