# Algorithme de Lamport
Utilise des clock logic

1. les processus echanges les messages
2. les messages doivent être envoyé avant d'être reçu
3. send/recive sont utiliser pour ordonner les événements et synchronise le clock logic

Utiliser la notation  "arrive avant" (a->b, "a envoie un message à b")

on assigne une valeur de clock à chaque événement. Le temps ne peut pas revenir en arrière.

Dans le cours:
À chaque demande, chaque algorithme se voit attribuer un numéro (qui doit être plus grand que les précédent). Il vérifie qu'il n'y ait aucun autre processus dans la SC et qu'il a le numéro le plus petit.

On utilise un estempille temporel (timestamp) pour représenter le graphe (noeud: timestamp, arc: précédence)

Problème, cette représentation peut aller jusqu'à l'infini et on peut avoir des problèmes de mémoire.
La solution est d'en faire un fini en supprimant la notion d'ordre total
