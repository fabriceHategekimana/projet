import ply.lex as lex
import ply.yacc as yacc
import sys

function_dict= {"add": "%s+%s", "sub":"%s-%s", "succ":"%s+1", "concat":"concat(%s,%s)", "set":"set(%s,%s,%s)", "get": "%s[%s]", "insert":"insert(%s,%s)", "append":"append(%s,%s)"}

def append(gauche, droite):
    if not isinstance(droite, list) and isinstance(gauche, list):
        gauche.append(droite)
    else:
        gauche= None
    return gauche

def insert(gauche, droite):
    if not isinstance(gauche, list) and isinstance(droite, list):
        droite.insert(0,gauche)
    else:
        droite= None
    return droite

def concat(gauche, droite):
    if not isinstance(gauche, list):
        gauche= [gauche]
    if not isinstance(droite, list):
        droite= [droite]
    return gauche+droite

def set(tab, index, value):
    tab[index]= value
    return tab

def func(f,i):
    return str(eval(f%i))

def write(content):
    f = open("res.txt", "w")
    f.write(content)
    f.close()

# _                       
#| |    _____  _____ _ __ 
#| |   / _ \ \/ / _ \ '__|
#| |__|  __/>  <  __/ |   
#|_____\___/_/\_\___|_|   
                         
tokens = [
    'NUM',
    'OP',
    'CP',
    'OSB',
    'CSB',
    'COMA',
    'LT',
    'GT',
    'NAME'
        ]

t_OP= r'\('
t_CP= r'\)'
t_OSB= r'\['
t_CSB= r'\]'
t_COMA= r'\,'
t_LT= r'\<'
t_GT= r'\>'

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
    write(str(p[1]))

def p_exp_operator(p):
    '''
    exp : NAME OP exp CP
    '''
    mt= tuple(p[3].split(";"))
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
    p[0] = str(p[1])

def p_exp_list(p):
    '''
    exp : list
    '''
    p[0] = str(p[1])

def p_exp_list1(p):
    '''
    list : OSB morelist CSB
    '''
    p[0] = str("["+p[2]+"]")

def p_exp_list2(p):
    '''
    morelist : NUM COMA morelist
    '''
    p[0] = str(p[1]+","+p[3])

def p_exp_list3(p):
    '''
    morelist : NUM
    '''
    p[0] = str(p[1])

def p_exp_list4(p):
    '''
    list : OSB CSB
    '''
    p[0] = "[]"

def p_exp_list5(p):
    '''
    list : LT morelist GT
    '''
    p[0] = str("["+p[2]+"]")

def p_more_exp(p):
    '''
    more : COMA exp more
    '''
    p[0] = ";"+p[2]+p[3]

def p_more_empty(p):
    '''
    more : COMA exp
    '''
    p[0] = ";"+p[2]


def p_error(p):
    write("Error")

parser= yacc.yacc()

#while True:
    #try:
        #s = input('')
    #except EOFError:
        #break
    #parser.parse(s)
