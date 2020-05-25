PROJECT=project:semtp4

all: start
 
start: FORCE
	zathura *.pdf & 2>error && vim -S Session.vim 2>error && rm error
task: FORCE
	task $(PROJECT)
addtask: FORCE
	task add $(ARGS) $(PROJECT)
summary:
	task $(PROJECT) summary

FORCE:
