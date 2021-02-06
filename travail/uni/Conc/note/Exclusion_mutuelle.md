# Problème d'exclusion mutuelle (mutex)

## Comment synchroniser l'accès aux variables de données

### Section critique et Lock
On utilise des opérations de type atomique: 
`deux accès à la variable doivent se faire de manière indivisible`.

`Section critique`: Un bout de code qui s'execute de façon atomique, souvent protégé par un verrou (Lock)

On préfère que le thread libère le verrou peu importe ce qu'il arrive (on utilise un try and catch)

[Algorithme_de_Peterson](Algorithme_de_Peterson)
[Lamport_s_Bakery_algorithm](Lamport_s_Bakery_algorithm)
