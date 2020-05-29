PROJET=project:bd

all: start
 
start: FORCE
	zathura *.pdf & 2>error
drive: FORCE
	firefoxe https://docs.google.com/document/d/1GzoJ-4iHJGYdfP03uEElUNLmK6EW5qCX-W28ZUE6p-o/edit# &
task: FORCE
	task project:base_de_données
addtask: FORCE
	task add $(ARGS) $(PROJET)
summary: FORCE
	task $(PROJET) summary
task: FORCE
	task $(PROJET)
FORCE:
