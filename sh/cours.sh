chemin=~/GDrive/Transfert/cours/2e/

echo "1 BSD"
echo "2 OOP"
echo "3 Théo de l'info"
echo "4 Prog des Sys"
echo "5 semantique"
echo "6 Analyse num."
echo "7 Projet de semestre"

#On li7 Analyse numkt ce que l'utilisateur rentre
read num

#On va faire des conditionnelles
case $num in
	1)
		P0=P && P=$(pwd) && cd "$chemin/Bases_de_donées"
		;;
	2)
		P0=P && P=$(pwd) && cd "$chemin/Conceptes_et_langages_orientés_objets"
		;;
	3)
		P0=P && P=$(pwd) && cd "$chemin/Elements_de_la_theorie_de_l_information"
		;;
	4)
		P0=P && P=$(pwd) && cd "$chemin/Programmation_des_systèmes"
		;;
	5)
		P0=P && P=$(pwd) && cd "$chemin/Semantique_des_languages_informatiques"
		;;
	6)
		P0=P && P=$(pwd) && cd "$chemin/Analyse_numérique"
		;;
	7)
		P0=P && P=$(pwd) && cd "$chemin/projet_de_semestre"
		;;
esac
if [ "$1" == "-t" ]; then 
	P0=P && P=$(pwd) && cd tp		
elif [ "$1" == "-n" ]; then 
	vim note*
elif [ "$1" == "-h" ]; then 
	echo"
	blank => open the main folder of the lesson
	-t => open the tp folder of the lesson
	-n => open the note document of the lesson
	-h => show the help menu	
	"
else
	echo " "
fi
/home/fabrice/GDrive/Transfert/cours/2e/projet_de_semestre/
