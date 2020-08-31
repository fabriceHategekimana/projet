\newcommand{\rectangle}[3]{\node (#1) [boite, xshift= #2 cm, yshift= #3 cm] {#1};}
\newcommand{\fleche}[3]{\draw[thick,->] (#1) -- (#2) node[midway,sloped,below, rotate=0] {#3};}
\newcommand{\flechel}[5]{\draw[thick,->] (#1) to [out=#4, in=#5] node[midway, sloped, below, rotate=0] {#3} (#2);}

---

title: rapport

---


Voila du texte
==============

## Voila encore du texte

Voila toujours du texte

titre1	titre2 	titre3
------	------	------
un	deux	trois
quatre	cinq	six

```python
#Voila du code en python
def addition(a, b):
	c= a + b
	print("la réponse est: ", c)
```

> citation
Classique des éléments

## notation mathématique en latex
\( \norm{\alpha A}= |\alpha| \norm{A} \)
