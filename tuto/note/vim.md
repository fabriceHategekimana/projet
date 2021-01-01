Vim
===
Intro

Sommaire
========
- origines
- vim c'est quoi?
- Bagage utils
- modes
- normal
- insertion
- visuel
- commande
- Vimscript et vimrc
- Plugins
- Documentation
- Autres (marqueurs, macro, quickfix, buffer, window, global, tab)

Origines
=========
- ed 1970 (Ken Thompson) edition ligne par ligne affichage par demande
- vi (ex) 1976 (Bill Joy) écran total, premier raccourcis.
- vim (Bram Moolenaar) 1988 (imitation -> amélioré)

Vim c'est quoi?
================
C'est plus qu'un éditeur de texte.
C'est une façon de penser la rédaction:
- On passe plus de temps à modifier qu'à ajouter
- Clavier + homerow
- langage (requête)

Les Bagages utils
=================
typing
regexp

Les modes
==========
Vim est un éditeur modal: plusieurs modes:
1. normal
2. insert
3. visual
4. select
5. command-line
6. Ex
7. Replace
8. Completion

Les plus utilisés
1. normal
2. insert
3. visual
4. command-line

Le mode normal
===============
Usage: navigation + édition rapide

touches: action, mouvement, action+mouvement

## keystrokes:
1. mouvements:

- flèches + hjkl
- spéciaux (w,b,e) ("(", ")", "{", "}")
- recherche (f,t,F,T,/,?)

2. actions:

- ligne (double): delete, yank, change, paste
- changement de mode (insersion, command-line, visual, etc.)
- spéciales

3. actions+mouvements (ou objet) 
 
- delete, yank, change
- objets: iw, i), it, aw, etc.

4. préfixes:
numérique: 1,...,23,...,2638,etc,...

mode insert
===========
               O 
               |
commande I<-i<-+->a->A
               |
	       o
	      
Change

mode completion:
-mots
-ligne
-fichier
-tags
-omni

Le mode Visual
===============
Selection+action
v, v, <C-v>

Le mode Command
===============
settings
Gestion de fichier (edit, write, quit, read)
Navigation ficher (buffer, window, tab)
terminal
map,abbrev
script

Vim script et le vimrc
======================
Variables (texte, nombre, boolean, listes)
echo, operators
map, function, command, etc.

Plugin
======
Pour augmenter les possibilités de vim
Précautions:
1. Savoir ce qu'il y a dans notre vimrc
2. Installer un nombre raisonable de plugins
3. Bien connaître ses plugins
Vim awesome

Documentation
=============
help
sites
communautés

Horizon:
=========
Neovim
Spacevim
Onivim
