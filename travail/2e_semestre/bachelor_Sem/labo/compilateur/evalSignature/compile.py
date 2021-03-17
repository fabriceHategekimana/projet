import ply.lex as lex
import ply.yacc as yacc
import sys

#Signature= {'and': [['bool', 'bool'], 'bool'],'or': [['bool', 'bool'], 'bool'], 'not': [['bool'], 'bool'], 'false': [['empty'], 'bool'], 'true': [['empty'], 'bool']} 

Signature= {'true': [['empty'], 'bool'], 'not': [['bool'], 'bool'], 'and': [['bool', 'bool'], 'bool'], 'false': [['empty'], 'bool'], 'or': [['bool', 'bool'], 'bool']}

def func(name,entree):
    try:
        tab= Signature[name]
        if tab[0] == entree:
            return [tab[1]]
        else:
             print('error: '+str(tab[0])+' expected but found '+entree+' instead')
             exit(1)
    except:
     print('error: operator \''+name+str(tuple(entree))+'\' not defined')

def checkName(name):
    try:
        tab= Signature[name]
        if tab[0] == ['empty']:
            return tab[1]
        else:
             print('error: '+str(['empty'])+' expected but found '+tab[0]+' instead')
             exit(1)
    except:
        print('error: operator \''+name+'\' not defined')
# _                       
#| |    _____  _____ _ __ 
#| |   / _ \ \/ / _ \ '__|
#| |__|  __/>  <  __/ |   
#|_____\___/_/\_\___|_|   
                         
tokens = [
    'OP',
    'CP',
    'COMA',
    'NAME',
    'DOUBLESEMICOLON',
        ]

t_OP= r'\('
t_CP= r'\)'
t_COMA= r'\,'
t_DOUBLESEMICOLON= r'\;;'

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

# ____                          
#|  _ \ __ _ _ __ ___  ___ _ __ 
#| |_) / _` | '__/ __|/ _ \ '__|
#|  __/ (_| | |  \__ \  __/ |   
#|_|   \__,_|_|  |___/\___|_|   
                               

def p_calc(p):
    '''
    calc : exp next
    '''
    print(p[1])

def p_exp_operator(p):
    '''
    exp : NAME OP exp CP 
    '''
    p[0] = func(p[1], p[3])

def p_exp_more(p):
    '''
    exp : exp more
    '''
    p[0] = p[1]+p[2]

def p_exp_name(p):
    '''
    exp : NAME 
    '''
    p[0] = [checkName(p[1])]

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
    next : DOUBLESEMICOLON
    '''
    p[0] = "" 

def p_next_exp(p):
    '''
    next : DOUBLESEMICOLON calc
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
