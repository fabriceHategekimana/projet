Vim
===

qui: Ces tutos sont adressés à tout les utilisateurs
ou: Depuis chez vous si vous avez vim
quand: Pour votre vie de tout les jours
quoi: un éditeur de code et surtout une façon de penser
comment: En réduisant la courbe d'apprentissage

Propriétésé
==============
cli
façon de penser

## défauts
Pas visuellement beau.
Pas intuitif sans les notions de base

## avantages
Bon champ d'application
Personnalisable

Sommaire
========
- origines
- vim c'est quoi?
- Bagage
- modes
- normal
- insertion
- visuel
- commande
- Sous-modes ou modes moins courrants
- Vimscript et vimrc
- Plugins
- Documentation
- Autres (marqueurs, buffer, window, tab)

Origines
=========
- ed 1970 (Ken Thompson) edition ligne par ligne affichage par demande
- vi (Bill Joy) écran total, premier raccourcis.
- vim (Bram Moolenaar) 1988 (imitation a -> amélioré)

Vim c'est quoi?
================
C'est plus qu'un éditeur de code.
C'est un mode de penser la rédaction:
- On passe plus de temps à modifier qu'à ajouter
- On doit être à l'aise sur la homerow
- langage

Les Bagages
===========
typing
regexp

Les modes
==========
Vim est un éditeur modal: plusieurs modes:
1. normal
2. insert
3. visual
4. select
5. command
6. Ex
7. Replace
8. Completion
9. Recherche

Les plus utilisés
1. normal
2. insert
3. visual
4. command

Le mode normal
===============
Mode navigation + édition rapide

## keystrokes:
mouvements:
- flèches + hjkl
- words (w,b,e) ("[", "]", "(", ")", "{", "}")
actions:
- ligne: delete, yank, paste, change
- changement de mode (insert, commande, visual)
- spéciaux
actions+mouvements 

5

préfixes: numéro

les modes (normal, insertion, commande, visuel)
normal: nav(hjkl,^,$,(,),{, },w,W,b,B,.), retou(yy,pp,dd,x),accès
insertion: insertion (i,a,I,A,s,cc)
visuel: selection (v,C-v,V)
commande: utilisation (:,:,!)


