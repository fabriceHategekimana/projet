%title: Vim
%author: Fabrice Hategekimana

```
                  
                            __   _(_)_ __ ___  
                            \ \ / / | '_ ` _ \ 
                             \ V /| | | | | | |
                              \_/ |_|_| |_| |_|
```

----

Sommaire
========
- origines
^
- vim c'est quoi?
^
- Bagages utils
^
- modes
^
- Vimscript et vimrc
^
- Plugins
^
- Documentation
^
- Autres (marqueurs, macro, quickfix, etc.)

----

Origines
=========

- *ed* 1970 (Ken Thompson) edition ligne par ligne affichage par demande
- *vi* (ex) 1976 (Bill Joy) écran total, premier raccourcis.
- *vim* (Bram Moolenaar) 1988 (imitation -> amélioré)

----

Vim c'est quoi?
================

C'est **plus** qu'un éditeur de texte.  
C'est une façon de penser la rédaction:  
- On passe plus de temps à **modifier** qu'à ajouter  
- Clavier + **homerow**  
- **langage** (requête)  

----

Les Bagages utiles
=================

* typing   
* shell (bash, zsh, cmd, powershell,...)   
* regexp   
* vi   

----

Les modes
==========

## Plusieurs modes:
1. normal
2. insert
3. visual
4. select
5. command-line
6. Ex
7. Replace
8. Completion
9. ...

----

# Les modes

## Les plus courants

1. normal
2. insert
3. visual
4. command-line

----

Le mode normal
===============

## Usage:   
	navigation + édition rapide  

## Actions:   
	`operateur` | `mouvement` | `operateur+mouvement`  

----

# Mouvements, operteurs

## Mouvements:
- flèches + hjkl
- words (w,b,e) ("(", ")", "{", "}")
- recherche (f,t,F,T,/,?)

## Operateurs:
- pending (d,y,c)
- direct (p,x,s,u,Ctrl+R)
- changement de mode (i, :, v)

----

# Operateur et mouvements

## Principe
- n operteurs et m mouvements: n*m possibilités

## Text-objects
- iw, i), it, aw, etc.

## Répétitions
- "."
- numérique: 1,...,23,...,2638,etc,...

----

Le mode insertion
=================

## Usage:
	insérer du texte

## Actions:
         O
         \^ 
   I<-i<-+->a->A    
         v
         o

----

# Le mode completion (mode mineur):

## Completion par:
- mots
- ligne
- fichier
- tags
- omni

----

Le mode Visuel
===============

## Usage:
	modification sur un champs sélectionné

## Actions:
	`Selection+action`

v, V, Ctrl+v

----

Le mode Command
===============

`champ` | `commande` | `champ+commande` 

* Settings
* Gestion de fichier (edit, write, quit, read)
* Navigation ficher (buffer, window, tab)
* Comportement de vim (map,abbrev,command,etc.)

----

# Autres fonctions de Vim

* terminal
* macro
* mark
* regexp
* quickfix
* script
* etc.

----

Vim script et le vimrc
======================

- Variables (texte, nombre, boolean, listes)  
- map, function, command, etc.  
- [Vim script the hard way](https://learnvimscriptthehardway.stevelosh.com/)

----

Plugin
======
**Pour augmenter les possibilités de vim**  

## Précautions:
1. **Savoir** ce qu'il y a dans notre vimrc
2. Installer un **nombre raisonable** de plugins
3. **Bien connaître** ses plugins

[VimAwsome](https://vimawesome.com/)

----

Documentation
=============
- **help**: (:help)  
- **sites**: (Vim Tips Wiki, youtube, sites particuliers)  
- **communautés**: (Stack Overflow, Stack Exchange, reddit, etc.) 

----

Horizon:
=========

* Editeurs+IDE
* Neovim
* Spacevim
* Onivim

----
```
                      __  __               _   _ 
                     |  \/  | ___ _ __ ___(_) | |
                     | |\/| |/ _ \ '__/ __| | | |
                     | |  | |  __/ | | (__| | |_|
                     |_|  |_|\___|_|  \___|_| (_)
                                                 
```
