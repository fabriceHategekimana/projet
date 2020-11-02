
PROJET=project:satom
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
mail: FORCE
	firefox https://outlook.office.com/mail/inbox/id/AAQkAGNiNzI0NDcyLWRlNjAtNDdjNC1iMzEwLTEwM2ZmOGE0OGMzZAAQANauEigVHVpNnxV4tfZXPkU%3D &

site: FORCE
	firefox https://control.divio.com/
neo4j: FORCE
	firefox http://localhost:7474/browser/
FORCE:


