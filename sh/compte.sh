
open () {
	libreoffice --calc *.xlsx
	sc *.sc
}

chemin=$(pwd)
cd ~/compte

if [ -z $2 ]; then
	#deux possibilités
	if [ -z  $1 ]; then
		#menu des projets
		select compte in *
		do
			cd $compte
			open 
		done
		exit 0	
	else
		#ouverture du projet indiqué
		cd $1
		open
	fi

else
	#création d'un compte
	mkdir $1
	cd $1
	mv $chemin/$2 .
fi

