import ply.lex as lex
import ply.yacc as yacc
import sys

# _                       
#| |    _____  _____ _ __ 
#| |   / _ \ \/ / _ \ '__|
#| |__|  __/>  <  __/ |   
#|_____\___/_/\_\___|_|   
                         
tokens = [
    'INT',
    'OP',
    'CP',
    'COMA',
    'NAME'
        ]

t_OP= r'\('
t_CP= r'\)'
t_COMA= r'\,'

t_ignore = r' '

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_NAME(t):
    r'[a-z_][a-zA-Z_0-9]*'
    t.type = 'NAME'
    return t

def t_error(t):
    print("Illegal characters!")
    t.lexer.skip(1)

lexer= lex.lex()
lexer.input("succ(add(1,2))")

#----------------------------------

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
