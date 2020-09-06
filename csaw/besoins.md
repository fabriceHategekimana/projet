
\newcommand{\rectangle}[3]{\node (#1) [boite, xshift= #2 cm, yshift= #3 cm] {#1};}
\newcommand{\fleche}[3]{\draw[thick,->] (#1) -- (#2) node[midway,sloped,below, rotate=0] {#3};}
\newcommand{\flechel}[5]{\draw[thick,->] (#1) to [out=#4, in=#5] node[midway, sloped, below, rotate=0] {#3} (#2);}


Besoins du wiki:
================

Il doit expliquer ce que le prochain développeur doit savoir.

Qu'est-ce qu'on doit savoir sur le projet?

La structure du projet:

1) Les fichiers utilisés (diagramme de flux)
2) Les entités (table UML)
3) Les choses qui restent à faire (questions)
4) Descriptions techniques et spécifiques (texte et exemple)
