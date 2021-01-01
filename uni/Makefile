all: start

start: FORCE
	for file in *.md ; do ~/sh/compmd $$file pdf ; done
other: FORCE
	vim IN.md
clean: FORCE
	rm *.html && mv -f *.pdf PDF
group: FORCE
	cat note.md Singleton.md Abstract_Factory.md Prototype.md Wrapper.md Proxy.md Decorator.md Template.md Flyweight.md Command.md Compose.md Builder.md Facade.md Observer.md State.md >> all.md

FORCE:
