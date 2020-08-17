
PROJET=project:programme
all: start
 
start: FORCE
	vim ~/.config/libreoffice/4/user/basic/Standard/Module2.xba
fait1: FORCE
	vim ~/.config/libreoffice/4/user/basic/Standard/Module1.xba
addtask: FORCE
	. ~/sh/mytask.sh
summary: FORCE
	task $(PROJET) summary
task: FORCE
	task $(PROJET)
close: FORCE
	task $(PROJET) done
note: FORCE
	vim note/note.md
pdf: FORCE
	cd pdf && bash ~/sh/cs.sh
FORCE:


