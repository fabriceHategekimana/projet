
\newcommand{\rectangle}[3]{\node (#1) [boite, xshift= #2 cm, yshift= #3 cm] {#1};}
\newcommand{\fleche}[3]{\draw[thick,->] (#1) -- (#2) node[midway,sloped,below, rotate=0] {#3};}
\newcommand{\flechel}[5]{\draw[thick,->] (#1) to [out=#4, in=#5] node[midway, sloped, below, rotate=0] {#3} (#2);}


Siren REST APIs (in Siren Investigate)
======================================

Permet de faire des requêtes pour obtenir des dashboard et des search.
C'est quoi des requête utilisant la syntaxe de [Siren_Federate](Siren_Federate)?

## Authentification
Géré à l'aide de [Siren_investigate](Siren_investigate)

Siren Investigate donne aussi un JDBC drivers for Elasticsearch qui sont disponible sur le CData website.
les valeurs retournées par l'API peuvent être utilisé en tant que vue dans le les requêtes SQL qui sont envoyés dans les drivers.
Il y a un API pour les dashboards et un API pour les recherches.
