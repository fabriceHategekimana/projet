Flyweight
==========

Structural design pattern
Permet de s'implifier les structures complexes. Quand on a besoin de gérer une grande quantité d'objet similaire.

Réduir la mémoire occupée en joignant les objets similaire.

Va utiliser un hashCode pour trouver les similarités.

Si un enfant existe déjà, on le recrée pas, mais on crée un nouveau lien dans la structure.

Divide object into: intrisic or extrasic properties.
intrisic= rendent l'objet unique
extrasic= utilisé et définit par le client

Le map est inaxessible du client. Hashmap de création d'objet selon les valeurs intrisic.
Le Hashmap est de type Hashmap.

Utilisation d'un map qui répertorie tout les objets. Cela se fait à l'aide d'une factorie exécuté du côté client.
