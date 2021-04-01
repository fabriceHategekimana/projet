import ply.lex as lex
import ply.yacc as yacc
import sys

def write(content):
    f = open("res.txt", "w")
    f.write(content)
    f.close()

# _                       
#| |    _____  _____ _ __ 
#| |   / _ \ \/ / _ \ '__|
#| |__|  __/>  <  __/ |   
#|_____\___/_/\_\___|_|   

reserved = {
        "in" : "IN",
        }
                         
tokens = [
    'NUM',
    'OP',
    'CP',
    'OSB',
    'CSB',
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
t_OSB= r'\['
t_CSB= r'\]'
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
    #print("Illegal characters!")
    t.lexer.skip(1)

lexer= lex.lex()

#----------------------------------

#Parser

def p_lang(p):
    '''
    lang : premises MINUS MINUS conclusion
    '''
    write(p[1][:-1]+" -- "+p[4])

def p_premisses1(p):
    '''
    premises : statements
    '''
    p[0] = " ".join(p[1:])

def p_premisses2(p):
    '''
    premises : 
    '''
    p[0] = ""

def p_statements1(p):
    '''
    statements : statement more
    '''
    p[0] = " ".join(p[1:])

def p_statements2(p):
    '''
    statements : 
    '''
    p[0] = ""

def p_more1(p):
    '''
    more : COMA statement more
    '''
    p[0] = ";"+p[2]+p[3]

def p_more2(p):
    '''
    more : 
    '''
    p[0] = ""

def p_statement(p):
    '''
    statement : exp sym exp
    '''
    p[0] = " ".join(p[1:])

def p_sym(p):
    '''
    sym : EQUAL
        | MINUS SUP
        | IN
    '''
    p[0] = "".join(p[1:])

def p_conclusion(p):
    '''
    conclusion : statement
    '''
    p[0] = p[1]

def p_operator(p):
    '''
    exp : NAME OP exp CP
    '''
    p[0] = " ".join(p[1:])

def p_more(p):
    '''
    exp : exp moreexp
    '''
    p[0] = p[1]+p[2]

def p_int(p):
    '''
    exp : NUM
        | VAR
    '''
    p[0] = str(p[1])

def p_term(p):
    '''
    term : NUM
         | VAR
         | list
    '''
    p[0]= str(p[1])

def p_list(p):
    '''
    exp : list
    '''
    p[0] = str(p[1])

def p_list1(p):
    '''
    list : OSB morelist CSB
    '''
    p[0] = str("["+p[2]+"]")

def p_list2(p):
    '''
    morelist : term COMA morelist
    '''
    p[0] = str(p[1]+","+p[3])

def p_list3(p):
    '''
    morelist : term
    '''
    p[0] = str(p[1])

def p_list4(p):
    '''
    list : OSB CSB
    '''
    p[0] = "[]"

def p_list5(p):
    '''
    list : INF morelist SUP
    '''
    p[0] = str("["+p[2]+"]")

def p_more_expexp(p):
    '''
    moreexp : COMA exp moreexp
    '''
    p[0] = ";"+p[2]+p[3]

def p_more_coma_exp(p):
    '''
    moreexp : COMA exp
    '''
    p[0] = ";"+p[2]

def p_error(p):
    write("error")

parser1= yacc.yacc(start='lang')

#s="plus(1,2) = element -- <d,empty> -> <d>"
#s="plus(1,2)"
#parser.parse(s)

#while True:
    #try:
        #s = input('')
    #except EOFError:
        #break
    #parser.parse(s)
