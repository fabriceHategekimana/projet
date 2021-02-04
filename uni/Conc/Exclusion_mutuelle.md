# Problème d'exclusion mutuelle

## Comment synchroniser l'accès aux variables de données

### Section critique et Lock
On utilise des opérations de type atomique: deux accès à la variable doivent se faire de manière indivisible.
Section critique: Un bout de code qui s'execute de façon atomique, souvent protégé par un verrou (Lock)

On préfère que le thread libère le verrou peu importe ce qu'il arrive (on utilise un try and catch)


Algorithme de Peterson
Lamport's Bakery algorithm

### Synchronisation
La difficulté principale pour assurer l’exclusion mutuelle vient du fait
qu’un processus doit
    1. Lire la valeur d’une variable pour tester que la SC est accessible
    2. Réserver l’accès à la SC en modifiant la valeur d’une variable
et que le processus peut perdre le contrôle pendant l’intervalle de
temps nécessaire à ces opérations (lecture et écriture).

En Java le mot clé synchronized permet de définir une routine qui ne
peut être exécutée que par un seul processus simultanément.

Utiliser une FIFO et synchroniser les méthodes de gestion de la queue

Avec la loi d'amdal, on se rend compte que les programmes synchronisés (s'executant séquentiellement) risquent de ralentir le programme.

La synchronisation est un problème si on a une interuption (par ex. exception).

# Méthode des invariants
Une proposition est invariante si elle est toujours vraie, dans tout les états possible du programme.

Les méchanismes de synchronisation permettent l'exclusion mutuelle et la coordination de l'exécution des threads sans utiliser de boucles d'attentes actives.

Sémaphore:
	- valeur booléenne
	- file d'attente de processus bloqués

Les méthode P() et V()
Lorsque P() est exécutée on a
    1.si valeur=true, alors valeur=false
    2.si valeur=false, le processus appelant est bloqué
Lorsque V() est exécutée on a
1. valeur=true, si la file d’attente des processus n’est pas libre on libère un processus
