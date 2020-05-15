mdp="code1.7.3"
read -s -p "Password: " mdpentre
echo ""
if [ "$mdpentre" != "$mdp" ]; then
	echo "mauvais mot de passe"
else
	echo "" >> ~/note/journal
	echo "$(date)" >> ~/note/journal
	echo "" >> ~/note/journal
	vim ~/note/journal
fi
