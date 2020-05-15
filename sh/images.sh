
if [ "$1" == "general" ]; then
	import ~/Images/screenshot/$(python ~/python/number.py $(ls images | wc -l)).png
else
	import images/$(python ~/python/number.py $(ls images | wc -l)).png
fi
