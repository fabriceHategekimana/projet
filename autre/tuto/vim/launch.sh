vimpath=~/sessions/vim

#lancer la page d'accueil
i3-msg "workspace 5"
i3-msg "exec gnome-terminal -- bash ~/sessions/vim/cow.sh "
i3-msg "exec gnome-terminal -- cava"
i3-msg "exec gnome-terminal -- tty-clock"
i3-msg "workspace 5"


i3-msg "workspace 3"
#lancer la musique
totem $vimpath/présentation.mp3 &

#lancer la présentation en image
i3-msg "exec libreoffice $vimpath/presentation_image.odp"
i3-msg "workspace 3"


#ouvrir mdp
mdp $vimpath/vim.md &

#ouvrir une nouvelle fenêtre tmux avec les exemples
tmux new-window 

