Decorator
==========

Structural pattern

Les décorateurs ajoute du nouveau contenu sans altéré la structure de l'objet qu'on modifie. Ils font une surcharge.

On peut ainsi wrapper la classe tout en gardant la signature de celle-ci.

Le decorator doit être une abstract class qui implémente l'interface en question.

On crée une classe concrète qui étant le décorateur. Cela permet de pouvoir ajouter des fonctionnalité à un groupe d'interface sans en modifier l'interface principale.

