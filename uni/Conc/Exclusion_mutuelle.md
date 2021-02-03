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
