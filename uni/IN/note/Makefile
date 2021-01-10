all: clean

rmall: FORCE
	rm all.md
group: rmall
	cat *.md > all.md
start: group
	for file in *.md ; do ~/sh/compmd $$file pdf ; done
clean: start
	rm *.html && mv -f *.pdf ../PDF

FORCE:
