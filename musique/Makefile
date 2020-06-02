
PROJET=project:musique
all: start
 
start: FORCE
	zathura *.pdf & 2>error && vim -S Session.vim 2>error && rm error
addtask: FORCE
	task add $(ARGS) $(PROJET)
summary: FORCE
	task $(PROJET) summary
task: FORCE
	task $(PROJET)
projet: FORCE
	echo $(PROJET)
FORCE:


