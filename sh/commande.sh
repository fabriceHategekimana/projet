

if [ "$1" == "-s" ]; then 
	cd ~
	#on mémorise les alias
	echo "$(alias)" > listeAlias.txt
	#on compresse les notes, les scripts, python et les fichiers de configuration
	mv ~/sh
	zip -r configuration sh note python .bashrc .vimrc .tmux_conf listeAlias.txt
	save configuration.zip
elif [ "$1" == "-h" ]; then 
	echo"
	blank => create a command with the two first parameter (name, command)
	-s => save all the command in a zip \"command.zip\" and send it to my personnal drive
	-h => show the help menu	
	"
else
	echo "alias $1='$2'"

	echo "Est-ce que cela vous convient? [y/n]"
	read ok

	if [ "$ok" = "y" ]; then
		echo "alias $1='$2'" >> ~/.bashrc
		. ~/.bashrc
	fi
fi
