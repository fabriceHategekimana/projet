if [ ! -d "images" ]; then
	mkdir images
fi
touch $1.md
echo "
\\newcommand{\\rectangle}[3]{\\node (#1) [boite, xshift= #2 cm, yshift= #3 cm] {#1};}
\\newcommand{\\fleche}[3]{\\draw[thick,->] (#1) -- (#2) node[midway,sloped,below, rotate=0] {#3};}
\\newcommand{\\flechel}[5]{\\draw[thick,->] (#1) to [out=#4, in=#5] node[midway, sloped, below, rotate=0] {#3} (#2);}
" > $1.md
