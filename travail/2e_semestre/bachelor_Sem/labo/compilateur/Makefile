all: compile

yacc:
	yacc -d calc.y

lex: yacc
	lex calc.l

compile: lex
	cc y.tab.c lex.yy.c
