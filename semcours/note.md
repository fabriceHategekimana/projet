
\newcommand{\rectangle}[3]{\node (#1) [boite, xshift= #2 cm, yshift= #3 cm] {#1};}
\newcommand{\fleche}[3]{\draw[thick,->] (#1) -- (#2) node[midway,sloped,below, rotate=0] {#3};}
\newcommand{\flechel}[5]{\draw[thick,->] (#1) to [out=#4, in=#5] node[midway, sloped, below, rotate=0] {#3} (#2);}
   
objectifs:  
Ce cours sert d'introduction aux langages de programmation importants par les concepts  
Qu'ils mettent en oeuvre et aux principes de la sémantique des langages. 
  
contenu:  

	* Introduction aux paradigmes fonctionnel, logique, procédural
	* La programmation logique
	* Notions d'induction et d'induction structurelles
	* Sémantique opérationnelles, dénotationnelle et axiomatiques des langages
	* Règles SOS, notions d'équivalences, sémantique d'évaluation et sémantique calculatoire
	* Preuves, validité et complétude
	* Logique du premier ordre, clause de Horn et satisfaction
	* Règles de typage et de visibilité: typage statistique et dynamique, polymorphisme paramétrique et ad-hoc, inférence de type
