
\newcommand{\rectangle}[3]{\node (#1) [boite, xshift= #2 cm, yshift= #3 cm] {#1};}
\newcommand{\fleche}[3]{\draw[thick,->] (#1) -- (#2) node[midway,sloped,below, rotate=0] {#3};}
\newcommand{\flechel}[5]{\draw[thick,->] (#1) to [out=#4, in=#5] node[midway, sloped, below, rotate=0] {#3} (#2);}

tables pour les dashboard
**Admin**
name	dc	dm	s	owner	info	more_options
----	--	--	-	-----	----	-------------

**Teacher**
name	dc	dm	view	create	info
----	--	--	----	------	-----	----
name	src	dc	dm	s	info	more

**Student**
name	owner	edit	info	   	   	   
----	-----	----	----	---	---	----	
name	src	dc	dm	s	share	more

**more options**
edit	duplicate	delete	share	view
----	---------	------	-----	-----
ats	ats		ats	at	ts


