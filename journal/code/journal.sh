if [ "$1" == "add" ]; then
	shift
	echo "labels:"
	read labels
	python3 ~/projet/journal/code/journaladd.py "$@ | $labels"
else
	python3 ~/projet/journal/code/journalview.py "$@"
fi
