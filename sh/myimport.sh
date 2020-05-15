


if [ "$1" == "image" ]; then
	mv ~/Images/*.png ./images
elif ["$1" == "-h" ]; then
	echo"
	blank	nothing append
	image	move all png from Images to the actual directory (thi is for latex)
	-h	show this help menu
	"
fi
