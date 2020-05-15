
#pour le Makefile
if [ -e  "Makefile" ]; then
	echo "Le fichier Makefile existe déjà"
else
	touch Makefile
	echo  "NOM ?= fabrice" >> Makefile
	echo  "" >> Makefile

	echo  "all: start" >> Makefile
	echo  "" >> Makefile

	echo  "start: \$(NOM)" >> Makefile
	echo  "	./.set.sh \$(NOM)" >> Makefile
	echo  "" >> Makefile

	echo "console:"  >> Makefile
	echo "	./.set.sh console \$(NOM)" >> Makefile

	echo "deux:"  >> Makefile
	echo "	echo vous pouvez mettre une commande spécialisée si vous le souhaitez" >> Makefile

	echo "screenshot:"  >> Makefile
	echo "	export SCREENSHOT=\$\$(ls images | wc -l) && export NUM=\$\$(python ~/python/number.py \$\$SCREENSHOT)  && import images/\$\$NUM.png" >> Makefile
	echo "remove:"  >> Makefile
	echo "	rm * .set.sh" >> Makefile
fi

#pour le .set.sh
if [ -e  ".set.sh" ]; then
	echo "Le fichier .set.sh existe déjà"
else
	touch .set.sh
	echo '
#!/bin/bash

if [ "$1" == "console" ]; then 
	echo On est dans la console
	extention=$(python3 -c "print(\"$2\"[\"$2\".index(\".\"):])")
	case $extention in
		.c)
			#code avec gdb
			;;
		.sh)
			#open a new terminal
			;;
		.py)
			python3
			;;
		.tex)
			#editeur latex
			;;
		.html)
			#editeur pour siteweb
			;;
		.m)
			octave --no-gui
			;;
		.pl)
			swipl
			;;
		.sql)
			mysql -u user -pd367*WGa! 
			;;
	esac
elif [ "$1" == "note" ]; then
	extention=$(python3 -c "print(\"$2\"[\"$2\".index(\".\"):])")
	note=~/note
	case $extention in
		.c)
			echo "$note/notec"
			;;
		.sh)
			echo "$note/notesh"
			;;
		.py)
			echo "$note/notepy"
			;;
		.tex)
			echo "$note/notetex"
			;;
		.html)
			echo "$note/notehtml"
			;;
		.java)
			echo "$note/notejava"
			;;
		.m)
			echo "$note/noteoctave"
			;;
		.pl)
			echo "$note/notepl"
			;;
		.sql)
			echo "$note/notesql"
			;;
		.md)
			echo "$note/notemarkdown"
			;;
	esac
else #on cherche les extention
	extention=$(python3 -c "print(\"$1\"[\"$1\".index(\".\"):])")
	case $extention in
		.c)
			gcc $1 -o main && ./main | less
			;;
		.sh)
			./$1 | less
			;;
		.py)
			python3 $1 | less
			;;
		.tex)
			sans=$(python3 -c "print(\"$1\"[:\"$1\".index(\".\")])")
			pdflatex $1 && zathura "$sans.pdf"
			;;
		.html)
			firefox $1 | less
			;;
		.java)
			filepath=$(pwd)
			parentname="$(basename $filepath)" 
			sans=$(python3 -c "print(\"$1\"[:\"$1\".index(\".\")])")
			cd ..
			javac -d . $parentname/$1 && java "$parentname$sans" | less
			;;
		.m)
			octave $1 | less
			;;
		.pl)
			swipl $1 | less
			;;
		.sql)
			mysql -u user -pd367*WGa! -e "$(cat $1)" | less
			;;
		.md)
			sans=$(python3 -c "print(\"$1\"[:\"$1\".index(\".\")])")
			pandoc $1 ~/note/pandoc_latex.yaml -s -o $sans.pdf &&  zathura $sans.pdf
			;;
	esac
fi
	' >> .set.sh
	chmod +x .set.sh
fi
