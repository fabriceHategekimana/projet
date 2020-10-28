
PROJET=project:csaw
all: task
 
start: FORCE
	zathura *.pdf & 2>error && vim -S Session.vim 2>error && rm error
addtask: FORCE
	task add $(ARGS) $(PROJET)
summary: FORCE
	task $(PROJET) summary
task: FORCE
	task $(PROJET)
wiki: FORCE
	firefox http://tecfalabs.unige.ch/csaw/dw/doku.php?id=c-saw:c-saw_external_development &
note: FORCE
	vim note/note.md
pdf: FORCE
	zathura note/csaw_documentation.pdf &
FORCE:


