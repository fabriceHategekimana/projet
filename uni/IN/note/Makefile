all: rendu

rmall: FORCE
	rm all.md
group: rmall
	cat *.md > all.md
start: group
	for file in *.md ; do ~/sh/compmd $$file pdf ; done
clean: start
	rm *.html && mv -f *.pdf ../PDF
zip: clean
	zip INResumeQ5-9+21 ../PDF/*
rendu: zip
	mv ../note/INResumeQ5-10+21.zip ~/rendu/

FORCE:
