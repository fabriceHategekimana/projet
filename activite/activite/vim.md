Vim
====

Vim est un éditeur de texte créer en 1991
Son nom complet vient de "vi improved" qui fait référence à vi

Vi et un autre éditeur de texte né en 19--
Il contient en lui (pareil chez vim) un mode appelé ex mode qui vient de l'éditeur ex

Ex est un éditeur de texte en ligne de commande né en 1976
son nom vient de "extend" car il ajoute des fonctionnalités à ed

Ed est un éditeur de texte en ligne de commande née en 1969
C'est l'un des tout premier éditeur de texte crée à côté des systèmes d'exploitation Unix par Ken Thompson et Dennis Ritchie.

## Étude de Ed
La meilleur façon de pouvoir approfondir mes connaissances sur vim est de pouvoir au moins comprendre le fonctionnement de ed, car ce qu'on peut faire avec ed, on peut aussi le faire avec vim.
Une bonne connaissance du shell unix ainsi que son système de fichier sont recommandés car ed est fait pour intéragir assez proche de ces derniers.

Modes:
Il y a deux mode de base, command et input. Input serait l'équivalent de insert sur vi ou vim.

input mode:
Permet d'entrer du text avec a (=append) i (=insert) c (=change). On quitte ce mode avec ".".

command mode:
Permet de manipuler le text à l'aide de commande. La forme courante est:
[adresse[,address]]Commande[paramètres]
On peut aussi invoquer des commande du shell en les précédent du "!"

Liste de commandes:
P (=prompt) : 
p (=print) : affiche le contenu de la plage de lignes choisie
r (=read) : lit un stream (fichier ou stdout d'une commande)
w (=write) : enregistre le nom d'un fichier
W (=Write) : ajoute la rangée à la fin du fichier visé
s (=substitute) : substitue un pattern par du text
[number] : pour sauter à une ligne en particulier
e (=edit) : edite un fichier
f (=filename) : change le nom du buffer actuel
d (delete) : supprime la rangée de ligne spécifiée
g (global) : repère les occurences cité et applique la commande indiqué (comme s)
v (?) : comme g mais s'applique aux lignes non-visée par l'expression
j (join) : joint une addresse de ligne
kx (mark) : mark une ligne au registre x
m (move) : déplace une rangée vers une autre ligne
t (copy) : copie une rangé de ligne vers une autre ligne
u (undo) : annule l'effet de la commande précédente
x (?) : copie le cut buffer dans la ligne mentionnée
y (yank) : copie la ligne dans le cut buffer
# (comment) écrit un commentaire (ignoré par le logiciel)

Adressage:
',' tout le dossier
';' pos actuel jusqu'à fin du dossier
