#!/bin/sh

OMPOSITORS=('awesome' 'beryl' 'blackbox' 'compiz' 'dwm' 'enlightenment' 'fluxbox' 'fvwm' 'i3' 'icewm' 'kwin' 'metacity' 'musca' 'openbox' 'pekwm' 'ratpoison' 'scrotwm' 'wmaker' 'wmfs' 'wmii' 'xfwm4' 'xmonad')

for i in `ps -u $USER -o comm`; do
	for c in ${ COMPOSITORS[@]}; do
		if [ "$i" == "$c" ]; then
			echo "Your compositor is $i"
		fi
	done
done
