
PROJET=project:task
all: start
 
start: FORCE
	zathura *.pdf & 2>error && vim -S Session.vim 2>error && rm error
addtask: FORCE
	task add  
summary: FORCE
	task  summary
task: FORCE
	task 
project: FORCE
	echo $(PROJET)
FORCE:


