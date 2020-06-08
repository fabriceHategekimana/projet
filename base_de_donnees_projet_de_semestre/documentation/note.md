
## Description de l'application:

Nous nous mettons ici dans la place du patron. C'est pour nous la place qui exploite le plus les 5 tables.
En effet, on pourrait construire d'autres interfaces dédiée qui permettraient aux employer de visualiser leur chantiers en cours.
Cependant, cela ne serai seulement qu'un exercice de consultation s'ils n'en ont que les droits.

Les deux fichiers utilisé pour le fonctionnement du logiciels sont:
1. espacePlus.exe
2. espacePlus.db

## Premier lancement
Cela dépend du système windows utilisé. Par rapport à celui de la maison, le windows de l'université bloque dans un premier temps le logiciel car il ne reconnait pas l'auteur.
Il affichera alors une fenêtre comme ceci:


Dans cet interface, les deux principales resources qui vont êtres manipulées sont les chantiers ainsi que les livraisons.
L'interface peut-être subdivisé en 6 blocs

**(1) selection d'année**
Représenter les chantier de façon annuel semblais préférable, c'est pourquoi ce sélecteur détermine l'année dans laquelle on travail.
Ainsi, ce paramètre va être automatiquement mis comme condition pour toutes les requêtes qui résultent sur des relations.

**(2) mois et numéros des semaines de l'année**
Cette table est là pour fonctionner de concert avec la table du dessous. Elle permet de savoir sur quelle période s'étant un chantier.

**(3) liste des chantiers de l'année**
Cette table fonctionne avec la table juste à sa droite. Elle permet de savoir à quelle ligne appartient un projet.

**(4) table de visualisation des chantiers sur l'année**
Comme le titre indique, cette table est là pour avoir une vue global des chantiers qu'il y a eu au cours de l'année.

**(5) calendrier des livraison**
C'est un outils qui nous permettra de localiser les livraison sur le temps.

**(6) table des livraisons**
Nous permet de pouvoir traiter les livraisons sur l'année.


## Quelques exemples d'utilisation (avec illustration)

#### Visualiser les livraisons
Il est possible de voir les livraisons pour un jour donnée. Pour cela, il suffit d'utiliser le calendrier en bas à gauche et sélectionner un jour en faisant un clique dessus. 
_Exemple_
On sait qu'il y a eu une livraisons le 7 juillet 2014 et on voudrai connaître le véhicule qu'on a utilisé.
On se déplace avec le calendrier pour arriver au mois de juillet et on sélection le jour numéro 7.
On voit s'afficher sur la table juste à gauche la livraison correspondante à ce jour.
On sait maintenant que le Van B3 a été utilisé pour faire la livraison.
Si on ne veut pas s'embêter à chercher une livraison dans les 365 possibilité que nous offre l'année, on peut simplement cliquer sur le bouton au dessus de la table des livraisons. Comme son nom l'indique, il va nous afficher toute les livraisons, mais seulement celles pour l'année en cours.

#### Créer, modifier et supprimer des livraisons
On peut aussi créer des livraisons. Pour cela, il suffit de sélectionner un jour qui nous convient dans le calendrier puis de double-cliquer sur la table et choisir le bouton "add" sur la petite fenêtre qui apparaît en haut à gauche de l'écran. On peut double-cliquer sur l'en-tête ou une ligne au hasard du moment qu'on sélection le bouton "add" (ça donnera le même résultat pour l'ajout d'une livraison).
Cela va créer une livraison avec des valeurs par défauts (sauf la date qui aura préalablement été définie grâce au calendrier).

Modifier les paramètres d'une livraison n'est pas trop compliqué.
Il faut tout d'abord afficher la livraison désirée (peut importe comment, tout les moyens de visualisation vu précédemment marchent).
Il faut ensuite double-cliquer sur la cellule qui nous intéresse (attention à ne pas double-cliquer sur un en-tête car cela ne donnera rien).
Finalement, on choisit le bouton "edit" de la petite fenêtre qui s'affiche en haut à gauche.
Selon la colonne de la cellule sélectionnée, le logiciel va déterminer le type d'édition correspondant:

**Édition par zone de texte**
C'est l'édition classique ou par défaut. Normalement ce choix d'édition est définit si la valeur de la cellule a plus un rôle informatif.
Cela veut dire que l'utilisateur est libre d'entrer les données qu'il veut vu qu'elles ne sont pas analysées/calculées par le logiciel.
Elle ne représente pas un risque de destruction de la base de donnée.

**édition par calendrier**
Cela concerne les dates (mais pas les heures) C'est pour être sûr que le bon format de date est enregistre vu qu'il sert en parti à l'identification des livraisons. Le jour sélectionné dans le calendrier sera alors écrit au format "JJ/MM/AAAA".

**édition par liste**
Cela se produit lorsque la colonne fait référence à l'une des listes existantes du projet (chantiers, flottes, etc.).
Il présente une liste des éléments possibles avec leurs détails. La sélection d'un élément va mettre son paramètre référencé dans la cellule qu'on édite. La sélection des élément se fait par double-clique.

Il est possible de supprimer une livraison. Il suffit simplement de faire un double-clique sur la ligne qui nous intéresse et de choisir "delete" dans la petit fenêtre qui s'affiche en haut à gauche.

__Exemple_:
On a oublié qu'on a livré pour le 10 juillet à 14h00 des produits de chez suter dans le chantier A4. Voici comment on procède pour l'ajouter:

On sélectionne le 10 juillet 2014 sur le calendrier en bas à gauche.
On fait un double-clique sur l'en-tête de la table à la droite du calendrier et on sélection le bouton "add" dan la petite fenêtre qui s'affiche en haut à gauche. 
Quand la livraison apparaît, on double-clique sur la cellule concernant le chantier et on sélectionne "edit" dans la petite fenêtre qui s'affiche en haut à gauche.
On a alors une liste des chantier pour l'année. On double clique sur la ligne dont le numéro de chantier est "NUM_CHANTIER" en double-cliquant dessus. La valeur est alors affiché sur la cellule en question.
Pour l'heure on fait la même logique: double-cliquer sur la cellule, "edit", écire "14h00" (sans les guillemets) puis appuyer sur le bouton "valider en bas de la fenêtre". La cellule devrait être mise à jours.
Pour le fournisseur, il suffit de: double-cliquer sur la cellule correspondante, "edit", sélectionner l'entreprise dont le nom est "Suter" en double-cliquant dessus. La cellule devrait être mise à jours.
Les données sont maintenant rentrées.

#### Visualiser les chantiers
Les détails des chantiers peuvent être visualisés. Il suffit de double-cliquer sur l'un des chantiers de la colonne de gauche puis d'appuyer sur le bouton "détail" de la petite fenêtre qui s'affiche en haut à gauche. On voit alors les détails du chantiers

#### Créer, modifier et supprimer des chantiers
Pour créer un chantier, il suffit de double-cliquer n'importe où sur la colonne de gauche puis de cliquer sur le bouton "add" de la petite fenêtre qui s'affiche en haut à gauche. On voit alors apparaître le chantier en question. L'identifiant est créé automatiquement et ne peut pas être changé.

Pour modifier un chantier, il suffit d'aller voir dans ses détails (double-clique puis "détail") et de double-cliquer sur l'une des celulles correspondantes. Attention, cliquer sur l'en-tête ne donnera rien.
Le logiciel choisit alors les option de modifications présentés précédement pour l'édition des livraisons. Cependant, les chantiers on une option d'édition en plus:

**édition par liste de liste**
Quand une cellule contient en elle même une liste qui prend sa source sur une table existante. Il faut alors une liste (à gauche) pour gérer les éléments sélectionnés et une liste (à droite) pour montrer les éléments sélectionnables. Double-cliquer sur un élément de la table de droite va soit ajouté l'employé s'il ne fait pas déjà parti de la liste des séléctionnés, ou soit enlever l'employé de la liste des sélectionnés s'il en fait déjà parti. En appuyant sur validé, les changements sont enregistrés. (Je ne comprend pas pourquoi, mais le programme se ferme lorsqu'on appuie sur le bouton validé puis qu'on ferme la fenêtre précédente. Il y a peut-être un appel de fonction qui pointe sur la mauvaise fenêtre à fermer).

_Exemple_
On veut ajouter un chantier de 3 semaines commençant à partir du 8 février et comptant 3 employés parmi lequel se trouve un menuisier.
Voila comment procéder:
On ajoute un chantier en double-cliquant sur la colonne des chantiers à gauche. On sélectionne le bouton "add" dans la petite fenêtre qui s'affiche en haut à gauche pour voir un nouveau chantier apparaître.
On double-clique sur ce chantiers et on sélectionne le bouton "detail" dans la petite fenêtre qui s'affiche en haut à gauche. On est maintenant devant les détails du chantiers sélectionné.
Il nous reste a double-cliquer la cellule sous l'en-tête "DATE_DEBUT" et sélectionner le 8 février 2014 avec le calendrier qui s'affiche. Il suffit ensuite d'appuyer sur le bouton "valider".
On change aussi la cellule "1 semaine" en "3 semaines".
Pour les employés. Il suffit d'utiliser l'outil d'édition liste par liste pour faire notre sélection.
