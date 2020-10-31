
PROJET=project:finances
all: start
 
start: FORCE
	sc-im code/general.csv
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


