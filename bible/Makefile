
PROJET=project:bible
all: start
 
start: FORCE
	zathura *.pdf & 2>error && vim -S Session.vim 2>error && rm error
addtask: FORCE
	make add  
summary: FORCE
	task  summary
task: FORCE
	task 
note: FORCE
	vim note.md

FORCE:
