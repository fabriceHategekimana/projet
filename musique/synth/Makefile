
PROJET=project:synth
all: task
 
start: FORCE
	zathura *.pdf & 2>error && vim -S Session.vim 2>error && rm error
addtask: FORCE
	. ~/sh/mytask.sh
summary: FORCE
	task $(PROJET) summary
task: FORCE
	task $(PROJET)
close: Force
	task $(PROJET) done
piano: FORCE
	fluidsynth -a alsa -g 5 giga_piano.sf2
FORCE:


