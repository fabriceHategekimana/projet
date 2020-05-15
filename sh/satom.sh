
if [ "$1" == "office" ]; then 
	firefox https://www.office.com/?auth=2 &
elif [ "$1" == "connecteur" ]; then
	remmina
elif [ "$1" == "teams" ]; then
	teams
elif [ "$1" == "doc" ]; then
	firefox https://mypads.framapad.org/p/document-court-mv2tld7kz
else
	echo "
	commande satom [option]:

	office:	go to the office dashboard of my satom account.
	connecteur: go to the desktop of the connector.
	teams: go to the desktop of the teams connector.
	doc: open the documentation repository.
		"
fi
