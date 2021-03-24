import ply.lex as lex
import ply.yacc as yacc
import sys

function_dict= {"add": "%s+%s", "sub":"%s-%s", "succ":"%s+1"}

def func(f,i):
    return eval(f%i)

# _                       
#| |    _____  _____ _ __ 
#| |   / _ \ \/ / _ \ '__|
#| |__|  __/>  <  __/ |   
#|_____\___/_/\_\___|_|   
                         
tokens = [
    'NUM',
    'OP',
    'CP',
    'COMA',
    'NAME'
        ]

t_OP= r'\('
t_CP= r'\)'
t_COMA= r'\,'

t_ignore = r' '

def t_NUM(t):
    r'\d+'
    t.value = str(t.value)
    return t

def t_NAME(t):
    r'[a-z_][a-zA-Z_0-9]*'
    t.type = 'NAME'
    return t

def t_error(t):
    print("Illegal characters!")
    t.lexer.skip(1)

lexer= lex.lex()

#----------------------------------

#Parser

def p_calc(p):
    '''
    calc : exp
    '''
    print(p[1])

def p_exp_operator(p):
    '''
    exp : NAME OP exp CP
    '''
    mt= tuple(p[3])
    p[0] = func(function_dict[p[1]], mt)

def p_exp_more(p):
    '''
    exp : exp more
    '''
    p[0] = p[1]+p[2]

def p_exp_int(p):
    '''
    exp : NUM
    '''
    p[0] = [p[1]]

def p_more_exp(p):
    '''
    more : COMA exp more
    '''
    p[0] = p[2]+p[3]

def p_more_empty(p):
    '''
    more : COMA exp
    '''
    p[0] = p[2]


def p_error(p):
    print("Error")

parser= yacc.yacc()

while True:
    try:
        s = input('')
    except EOFError:
        break
    parser.parse(s)
