# Exceptions:

Un état ou une valeur qui présente un comportement inattendu (bug ou erreur) provoqué dans l'exception.

Diagramme de classe: note

Bug: 

java.lang= importé par défaut

Stack trace= voir la hiérarchie des appel de question.

Throw exception = lever une exception
Cela sert à créer une exception:

```java
	throw new exceptionName("ajskdflk")
```

Il y a des runtime exception

Quand les exceptions sont levées, elles remontent toute la stack trace.

Gérer une interruption: décider du comportement à prendre dans ce genre de cas.
Try et au moins catch ou finally

e.getException()

On peut faire plusieurs catch pour attrapper toutes les exceptions
Le finally est toujours exécuté peut importe ce qu'il se passe dans le try.
Il faut utiliser out.close() après avoir fait un print

FileReader() //pour ouvrir un fichier
C'est mieux d'utiliser un BufferReader et lui passer un FileReader pour une meilleurs gestion


