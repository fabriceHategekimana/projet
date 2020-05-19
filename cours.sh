#!/bin/bash
#variables de départ
startingPoint=$(pwd)
coursFolder=~/cours


#fonctions de départ
goToStartingPoint(){ 
	cd $startingPoint
}
goTosimpleCoursFolder(){
	cd $coursFolder
}
simpleCoursExists(){
	cours=$(ls $coursFolder)
	exists=$(echo $cours | grep -o $1)
	if [ -z $exists ]; then
		exists=0	
	else
		exists=1
	fi
}
existsOrSelect(){
	simpleCoursExists $1
	if [ $exists == 1 ]; then
		name=$1
	else
		goTosimpleCoursFolder
		select simpleCours in *
		do
			name=$simpleCours
			break;
		done
		goToStartingPoint
	fi
}

createFiles(){
	touch Makefile
	echo "
all: start
 
start:
	echo hello world!
revisions:
	cd ~/cours/revisions
exercices:
	cd ~/cours/exercices
tps:
	cd ~/cours/tps

" >> Makefile
	mkdir revisions
	touch revisions/notes.md
	touch revisions/questions.md
	mkdir exercices
	mkdir tps
}

createDoc(){
	. ~/sh/mkdoc.sh
}

executer(){
	if [ "$1" == "create" ]; then
		shift
		goTosimpleCoursFolder
		name=$1
		mkdir $name
		cd $name
		createFiles
		shift
		goToStartingPoint
		cp -r $@ $coursFolder/$name  2> error
		rm error
	elif [ "$1" == "add" ]; then
		shift
		#will get the $name for later
		existsOrSelect $1
		if [ $exists == 1 ]; then
		      shift 
		fi	
		cp -r "$@" $coursFolder/$name
		cd $coursFolder/$name
	elif [ "$1" == "delete" ]; then
		shift
		if [ $# == 0 ]; then
			goTosimpleCoursFolder
			select simpleCours in *	
			do
				rm -r $coursFolder/$simpleCours
				break;
			done
			goToStartingPoint
		else
			for simpleCours in "$@"
			do
				rm -r $coursFolder/$simpleCours
			done
		fi
	elif [ "$1" == "push" ]; then
		goTosimpleCoursFolder
		#mettre à jour calcurse
		cp -r ~/projet/calcurse/calcurse/todo ~/projet/calcurse/calcurse/apts ~/projet/calcurse/calcurse/notes ~/projet/calcurse/data
		#code pour Github
		git add .
		git commit -m "update"
		git push
	elif [ "$1" == "pull" ]; then
		git pull
	else
		existsOrSelect $1
		cd $coursFolder
		cd $name
		make $2
	fi
}

executer $@
