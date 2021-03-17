
import sys

typeTable= {}

def func(f,i):
    return eval(f%i)

def toTypeTable(name, liste):
    sortie= liste.pop()
    #print("name:", name)
    #print("entree:", liste)
    #print("sortie:", sortie)
    typeTable[name]= [liste,sortie]
    print(typeTable)


# _                       
#| |    _____  _____ _ __ 
#| |   / _ \ \/ / _ \ '__|
#| |__|  __/>  <  __/ |   
#|_____\___/_/\_\___|_|   
                         
tokens = [
    'OB',
    'CB',
    'COMA',
    'NAME',
    'DOT'
        ]

t_OB= r'\['
t_CB= r'\]'
t_COMA= r'\,'
t_DOT= r'\.'

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
    print("Illegal characters! ", t)
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
    exp : NAME OB exp CB next
    '''
    toTypeTable(p[1], p[3])
    p[0] = ""

def p_exp_more(p):
    '''
    exp : exp more
    '''
    p[0] = p[1]+p[2]

def p_exp_int(p):
    '''
    exp : NAME
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

def p_next_empty(p):
    '''
    next : DOT
    '''
    p[0] = "" 

def p_next_exp(p):
    '''
    next : DOT exp
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
