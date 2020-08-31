
PROJET=project:rendu
all: task
 
start: FORCE
	zathura *.pdf & 2>error && vim -S Session.vim 2>error && rm error
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


