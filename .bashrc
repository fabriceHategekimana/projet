# ~/.bashrc: executed by bash(1) for non-login shells.
# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)
# for examples

# If not running interactively, don't do anything
case $- in
    *i*) ;;
      *) return;;
esac 

# don't put duplicate lines or lines starting with space in the history.
# See bash(1) for more options
HISTCONTROL=ignoreboth

# append to the history file, don't overwrite it
shopt -s histappend

# for setting history length see HISTSIZE and HISTFILESIZE in bash(1)
HISTSIZE=1000
HISTFILESIZE=2000

#default editor
export EDITOR=vim

# check the window size after each command and, if necessary,
# update the values of LINES and COLUMNS.
shopt -s checkwinsize

# If set, the pattern "**" used in a pathname expansion context will
# match all files and zero or more directories and subdirectories.
#shopt -s globstar

# make less more friendly for non-text input files, see lesspipe(1)
[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"

# set variable identifying the chroot you work in (used in the prompt below)
if [ -z "${debian_chroot:-}" ] && [ -r /etc/debian_chroot ]; then
    debian_chroot=$(cat /etc/debian_chroot)
fi

# set a fancy prompt (non-color, unless we know we "want" color)
case "$TERM" in
    xterm-color|*-256color) color_prompt=yes;;
esac

# uncomment for a colored prompt, if the terminal has the capability; turned
# off by default to not distract the user: the focus in a terminal window
# should be on the output of commands, not on the prompt
#force_color_prompt=yes

if [ -n "$force_color_prompt" ]; then
    if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then
	# We have color support; assume it's compliant with Ecma-48
	# (ISO/IEC-6429). (Lack of such support is extremely rare, and such
	# a case would tend to support setf rather than setaf.)
	color_prompt=yes
    else
	color_prompt=
    fi
fi

if [ "$color_prompt" = yes ]; then
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
fi
unset color_prompt force_color_prompt

# If this is an xterm set the title to user@host:dir
case "$TERM" in
xterm*|rxvt*)
    PS1="\[\e]0;${debian_chroot:+($debian_chroot)}\u@\h: \w\a\]$PS1"
    ;;
*)
    ;;
esac

# enable color support of ls and also add handy aliases
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'
    #alias dir='dir --color=auto'
    #alias vdir='vdir --color=auto'

    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi

# colored GCC warnings and errors
#export GCC_COLORS='error=01;31:warning=01;35:note=01;36:caret=01;32:locus=01:quote=01'

# some more ls aliases
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'

# Add an "alert" alias for long running commands.  Use like so:
#   sleep 10; alert
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'

# Alias definitions.
# You may want to put all your additions into a separate file like
# ~/.bash_aliases, instead of adding them here directly.
# See /usr/share/doc/bash-doc/examples in the bash-doc package.

if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi

# enable programmable completion features (you don't need to enable
# this, if it's already enabled in /etc/bash.bashrc and /etc/profile
# sources /etc/bash.bashrc).
if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi
export PATH=/usr/share/swift/usr/bin:/usr/share/swift/usr/bin:/usr/share/swift/usr/bin:/usr/share/swift/usr/bin:/home/fabrice/bin:/home/fabrice/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
export PATH=/usr/share/swift/swift-5.1-RELEASE-ubuntu18.04/usr/bin:/usr/share/swift/usr/bin:/usr/share/swift/usr/bin:/usr/share/swift/usr/bin:/usr/share/swift/usr/bin:/usr/share/swift/usr/bin:/home/fabrice/bin:/home/fabrice/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin

#afficher l'entrée de base
figlet Jesus est Seigneur

#les alias basic modifiés
alias cd='export P=$P0 && P0=$(pwd) && cd'
alias rm='rm -r'

#les commandes de création d'environnement de programmation
alias mktex='. ~/sh/mktex.sh'
alias mkswift='. ~/swift/setup.sh'
alias mkc='. ~/sh/mkc.sh'
alias mkpy='. ~/sh/mkpy.sh'

#Les commandes pour internet
alias portail='firefox https://portail.unige.ch/accueil &'
alias moodle='firefox https://moodle.unige.ch/my/ &'
alias gitlab='firefox https://gitlab.unige.ch/ &'
alias whatsapp='firefox https://web.whatsapp.com/ &'
alias geeksforgeek='firefox https://www.geeksforgeeks.org &'
alias gmail='firefox https://mail.google.com/mail/u/0/#inbox &'
alias keep='firefox https://keep.google.com/u/0/ &'
alias calendar='firefox https://calendar.google.com/calendar/r?tab=wc&pli=1 &'
alias youtube='firefox https://www.youtube.com/ &'
alias mobility='firefox https://my.mobility.ch/login &'

#les commandes de note
alias nt='vim /home/fabrice/note/note'
alias vimnt='vim ~/vim/note'
alias texnt='vim ~/latex/note'
alias journal='. ~/sh/journal.sh'
alias bashnt='vim ~/sh/note'

#les commandes avancées
alias cs='. ~/sh/cs.sh'
alias cours='. ~/sh/cours.sh'
alias save='. ~/sh/save.sh'

#les commandes pas encore triées

alias actuel='. ~/sh/actuel.sh'
alias cnt='vim ~/c/note'

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/fabrice/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/fabrice/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/home/fabrice/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/home/fabrice/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<

alias rendu='. ~/sh/rendu.sh'
alias programme='. ~/sh/programme.sh'
alias compta='. ~/sh/compta.sh'
alias tutoriel='sc /usr/share/doc/sc/tutorial.sc'
alias g='. ~/sh/g.sh'
alias commande='. ~/sh/commande.sh'
alias session='. ~/sh/session.sh'
alias forti='cd ~/forticlientsslvpn/ && sudo ./fortisslvpn.sh'
alias myrm='. ~/sh/myrm.sh'
alias temp='. ~/sh/temp.sh'
alias bashrc='. ~/sh/bashrc.sh'
alias pdf='. ~/sh/pdf.sh'
alias vimrc='vim ~/.vimrc'
alias Téléchargements='cd ~/Téléchargements'
alias environment='. ~/sh/environment.sh'
alias visa='firefox https://one.viseca.ch/fr/logged-out'
alias bcge='firefox https://www.bcge.ch/authen/login?lang=fr'
alias siloé='cd ~/Documents/eglise/siloé'
alias octave='octave --no-gui'
alias google='w3m google.ch'
alias spirituel='. ~/sh/spirituel.sh'
alias topbible='w3m https://topbible.topchretien.com/'
alias organisation='cs ~/Documents/organisation/'
alias priorité='vim ~/Documents/organisation/activités/priorité'
alias telegram='cd ~/Telegram/ && ./Telegram &'
alias mksite='. ~/sh/mksite.sh'
alias mep='cd ~/Documents/eglise/mep'
alias wordpress='firefox localhost/wordpress/wp-admin/ &'
alias sitemep='cd /var/www/html/wordpress/wp-content/themes/twentymep/'
alias ici='export ICI=$(pwd)'
alias push='. ~/sh/push.sh'
alias pull='. ~/sh/pull.sh'
alias euronews='firefox https://fr.euronews.com/bulletin &'
alias rts='firefox https://www.rts.ch/info/ &'
alias news='. ~/sh/news.sh'

#load the terminal directly to tmux
tmux

alias mkjava='. ~/sh/mkjava.sh'
alias resume='firefox https://drive.google.com/drive/u/0/folders/13Tw3ChvkzGSoCctLmvpn2aYzunMVFy1_ &'
alias semantique='firefox https://gitlab.unige.ch/semantique/semantique_2020 &'
alias projet='. ~/sh/projet.sh'
alias compte='. ~/sh/compte.sh'
alias mkpl='. ~/sh/mkpl.sh'
alias sempull='git pull course master'
alias sempush='git push origin master'
alias sql='. ~/sh/sql.sh'
alias facebook='firefox https://www.facebook.com/ &'
alias mksql='. ~/sh/mksql.sh'
alias outlook='firefox https://outlook.unige.ch/owa/#path=/mail/inbox &'
alias mk='. ~/sh/environmentGenerator.sh'
alias activite='cd /home/fabrice/Documents/organisation/activités'
alias mkoctave='. ~/sh/mkoctave.sh'
alias vims='vim -S Session.vim'
alias myimport='. ~/sh/myimport.sh'
alias Images='cd ~/Images'
alias Vidéos='cd ~/Vidéos'
alias serveur='cd /var/www/html'
alias csaw='cd /var/www/html/CSAWCUIprojet/csawBeta'
alias traduction='firefox https://www.deepl.com/fr/translator &'
alias mkdoc='. ~/sh/mkdoc.sh'
alias i3config='vim ~/.config/i3/config'
alias comptonconfiguration='vim .config/compton/compton.conf'
alias luminosite='sudo chmod o+rw /sys/class/backlight/intel_backlight/brightness'
alias mkmd='. ~/sh/mkmd.sh'

alias onedrive='firefox https://satomitlearning-my.sharepoint.com/personal/fabrice_hategekimana_satom_ch/_layouts/15/onedrive.aspx &'
alias satom='. ~/sh/satom.sh'
alias lo='libreoffice'
alias mkphp='. ~/sh/mkphp.sh'
alias imprimante='. ~/sh/imprimante.sh'
alias stop='. ~/sh/stop.sh'
alias bibliographie='firefox www.unige.ch/biblio &'
