




select myrm in *
do
	rm -fr $myrm
	echo "$myrm removed"
done
