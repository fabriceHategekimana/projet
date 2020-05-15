#!/bin/bash
#variables de départ
startingPoint=$(pwd)
projectFolder=~/projet


#fonctions de départ
goToStartingPoint(){ 
	cd $startingPoint
}
goToProjectFolder(){
	cd $projectFolder
}
projectExists(){
	projects=$(ls $projectFolder)
	exists=$(echo $projects | grep -o $1)
	if [ -z $exists ]; then
		exists=0	
	else
		exists=1
	fi
}
existsOrSelect(){
	projectExists $1
	if [ $exists == 1 ]; then
		name=$1
	else
		goToProjectFolder
		select project in *
		do
			name=$project
			break;
		done
		goToStartingPoint
	fi
}

createMakefile(){
	touch Makefile
	echo "
all: start
 
start:
	zathura *.pdf & 2>error && vim -S Session.vim 2>error && rm error

" >> Makefile
}

executer(){
	if [ "$1" == "create" ]; then
		shift
		goToProjectFolder
		name=$1
		mkdir $name
		cd $name
		createMakefile
		shift
		goToStartingPoint
		cp $@ $projectFolder/$name  2> error
		rm error
	elif [ "$1" == "add" ]; then
		shift
		#will get the $name for later
		existsOrSelect $1
		if [ $exists == 1 ]; then
		      shift 
		fi	
		cp "$@" $projectFolder/$name
		cd $projectFolder/$name
	elif [ "$1" == "delete" ]; then
		shift
		if [ $# == 0 ]; then
			goToProjectFolder
			select project in *	
			do
				rm -r $projectFolder/$project
				break;
			done
			goToStartingPoint
		else
			for project in "$@"
			do
				rm -r $projectFolder/$project
			done
		fi
	else
		existsOrSelect $1
		cd $projectFolder
		cd $name
		make $2
	fi
}

executer $@
