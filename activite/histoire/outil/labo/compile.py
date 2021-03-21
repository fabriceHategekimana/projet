
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
    'NUM',
    'VAR',
    'ENT',
    'ADD',
    'DELETE',
    'CHECK',
    'DISPLAY',
    'AND',
    'OR'
        ]

t_ADD= r'add'
t_DELETE= r'delete'
t_CHECK= r'check'
t_DISPLAY= r'display'
t_AND= r'and'
t_OR= r'or'
t_COMA= r'\,'
t_DOT= r'\.'

t_ignore = r' '

def t_NUM(t):
    r'\d+'
    t.value = str(t.value)
    return t

def t_ENT(t):
    r'[a-zA-Z][a-z0-9]+'
    t.type = 'ENT'
    return t

def t_VAR(t):
    r'[A-C]'
    t.type = 'VAR'
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

def p_exp_exp1(p):
    '''
    exp : ADD modify
        | DELETE modify
    '''
    p[0] = p[1] #on l'envoie dans la base sql

def p_exp_exp2(p):
    '''
    exp : CHECK query
        | DISPLAY query
    '''
    p[0] = p[1]+p[2] #on l'envoie dans la base sql

def p_exp_modify(p):
    '''
    modify : fact
           | rule
    '''
    p[0] = p[1]

def p_exp_fact(p):
    '''
    fact : ENT ENT ENT
    '''
    p[0] = p[1]+p[2]+p[3] #C'est là où on fait l'union

def p_exp_rule(p):
    '''
    rule : if logalg then conj
    '''
    p[0] = p[1]+p[2]

def p_exp_logalg(p):
    '''
    logalg : fact2 more
    '''
    p[0] = p[1]+p[2]

def p_exp_more(p):
    '''
    more : op fact2 more
    '''
    p[0] = p[1]+p[2]

def p_exp_op(p):
    '''
    op : AND
       | OR
    '''
    p[0] = p[1]

def p_exp_conj(p):
    '''
    conj : fact2 moreconj
    '''
    p[0] = p[1]+p[2]

def p_exp_AND(p):
    '''
    moreconj : AND fact2 moreconj
             | empty
    '''
    p[0] = p[1]+p[2]+p[3]

def p_exp_predicat(p):
    '''
    fact2 : el ENT el
    '''
    p[0] = p[1] #C'est là où doit se faire l'union partielle

def p_exp_term(p):
    '''
    el : ENT
       | VAR
    '''
    p[0] = p[1]

def p_error(p):
    print("Error")

parser= yacc.yacc()

while True:
    try:
        s = input('')
    except EOFError:
        break
    parser.parse(s)
