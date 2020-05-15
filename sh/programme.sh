

if [ "$1" == "-d" ]; then 
	#SCRIPT POUR PRÉPARER LE BUREAU POUR LE PROGRAMME DU DIMANCHE
	#rend propre le repertoire dim
	cd ~/Bureau/dim
	mv -u *.odp *.pptx ~/Bureau/dimanche
	cd fini
	mv -u *.odp *.pptx /home/fabrice/Documents/Église/Siloé/Répertoire 
	#on ouvre avec nautilus les repertoirs nécesaire
	#dim pour créer le nouveau programme
	nautilus ~/Bureau/dim &
	#repertoire pour extraire les chants qu'on veut
	nautilus /home/fabrice/Documents/Église/Siloé/Répertoire &
elif [ "$1" == "-l" ]; then 
	#code à exécuter
	lab=/home/fabrice/Documents/eglise/siloé/lab
	cd $lab
	vim -S laboratoire.vim
elif [ "$1" == "-h" ]; then 
	echo"
	blank => remind the author that he must to write a specific code about libreoffice
	-d => open the folder to make the powerpoint version of the programme for Sunday
	-l => open the laboratory to make a programme
	-h => show the help menu	
	"
else
	echo "Choisissez une action à réaliser. Rappel: il faudra aussi faire le code libreoffice pour le programme"
fi

