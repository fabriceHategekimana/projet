
if [ -z "$1" ]; then
	chemin="."
else
	chemin=$1
fi

P0=P && P=$(pwd) && P0=P && P=$(pwd) && cd $chemin
compteur=0
pdf=0

#ici on affiche les éléments avec la numérotation adéquate
for i in *.pdf; do
	if [ "$i" != "*.pdf" ]; then
		((compteur++))
		((pdf++))
		echo $compteur $i
	fi
done

#s'il existe des pdf
if [ "$pdf" != "0" ]; then 
	#on prend ensuite le chiffre que veut l'utilisateur
	read num

	compteur=0
	for i in *.pdf; do
		((compteur++))
		if [ "$compteur" == "$num" ]; then
			zathura "$i" &
		fi
	done
else
	ls -d */
fi
