import ply.lex as lex
import ply.yacc as yacc
import sys


# _                       
#| |    _____  _____ _ __ 
#| |   / _ \ \/ / _ \ '__|
#| |__|  __/>  <  __/ |   
#|_____\___/_/\_\___|_|   

reserved = {
        "and" : "AND"
        }
                         
tokens = [
    'NUM',
    'OP',
    'CP',
    'OB',
    'CB',
    'COMA',
    'EQUAL',
    'INF',
    'SUP',
    'MINUS',
    'VAR',
    'NAME'
        ]+list(reserved.values())

t_OP= r'\('
t_CP= r'\)'
t_OB= r'\['
t_CB= r'\]'
t_COMA= r'\,'
t_INF= r'\<'
t_SUP= r'\>'
t_MINUS= r'\-'
t_EQUAL= r'\='

t_ignore = r' '

def t_NUM(t):
    r'\d+'
    t.value = str(t.value)
    return t

def t_NAME(t):
    r'[a-z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'NAME')
    return t

def t_VAR(t):
    r'[A-Z][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'VAR')
    return t

def t_error(t):
    print("Illegal characters!")
    t.lexer.skip(1)

lexer= lex.lex()

#----------------------------------

#Parser

def p_calc(p):
    '''
    calc : premises MINUS MINUS conclusion
    '''
    print(" ".join(p[1:]))

#def p_calc(p):
    #'''
    #calc : exp 
    #'''
    #print(" ".join(p[1:]))

def p_exp_premisses(p):
    '''
    premises : fact following
    '''
    p[0] = " ".join(p[1:])

def p_exp_fact1(p):
    '''
    fact : transition
    '''
    p[0] = p[1]

def p_exp_fact2(p):
    '''
    fact : equality
    '''
    p[0] = p[1]

def p_exp_transition(p):
    '''
    transition : term MINUS SUP term
    '''
    p[0] = " ".join(p[1:])

def p_exp_term1(p):
    '''
    term : exp
    '''
    p[0] = p[1]

def p_exp_term2(p):
    '''
    term : state
    '''
    p[0] = p[1]

def p_exp_state(p):
    '''
    state : INF suite SUP
    '''
    p[0] = " ".join(p[1:])

def p_exp_suite1(p):
    '''
    suite : exp next
    '''
    p[0] = " ".join(p[1:])

def p_exp_suite2(p):
    '''
    suite : NAME next
    '''
    p[0] = " ".join(p[1:])

def p_exp_suite3(p):
    '''
    suite : VAR next
    '''
    p[0] = " ".join(p[1:])

def p_exp_suite4(p):
    '''
    suite : list next
    '''
    p[0] = " ".join(p[1:])

def p_exp_list1(p):
    '''
    list : OB exp CB
    '''
    p[0] = " ".join(p[1:])

def p_exp_list2(p):
    '''
    list : OB suite CB
    '''
    p[0] = " ".join(p[1:])

def p_exp_next1(p):
    '''
    next : COMA suite
    '''
    p[0] = " ".join(p[1:])

def p_exp_next2(p):
    '''
    next : 
    '''
    p[0] = ""

def p_exp_equality(p):
    '''
    equality : exp EQUAL exp
    '''
    p[0] = " ".join(p[1:])

def p_exp_following1(p): #ici
    '''
    following : COMA fact following 
    '''
    p[0] = " ".join(p[1:])

def p_exp_following2(p):
    '''
    following : 
    '''
    p[0] = ""

def p_exp_conclusion(p):
    '''
    conclusion : transition
    '''
    p[0] = p[1]

def p_exp_operator(p):
    '''
    exp : NAME OP exp CP
    '''
    p[0] = " ".join(p[1:])

def p_exp_more(p):
    '''
    exp : exp more
    '''
    p[0] = " ".join(p[1:])

def p_exp_int(p):
    '''
    exp : NUM
    '''
    p[0] = p[1]

def p_exp_name(p):
    '''
    exp : NAME
    '''
    p[0] = p[1]

def p_exp_var(p):
    '''
    exp : VAR
    '''
    p[0] = p[1]

def p_more_exp(p):
    '''
    more : COMA exp more
    '''
    p[0] = " ".join(p[1:])

def p_more_empty(p):
    '''
    more : 
    '''
    p[0] = ""

def p_error(p):
    print("Error: ", p)

parser= yacc.yacc(start='calc')

#s="plus(1,2) = element -- <d,empty> -> <d>"
#s="plus(1,2)"
#parser.parse(s)

#while True:
    #try:
        #s = input('')
    #except EOFError:
        #break
    #parser.parse(s)
