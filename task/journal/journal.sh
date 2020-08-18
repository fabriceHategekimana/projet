if [ "$1" == "add" ]; then
	shift
	echo "labels:"
	read labels
	python3 ~/projet/task/journal/journaladd.py "$@ | $labels"
else
	python3 ~/projet/task/journal/journalview.py "$@"
fi
