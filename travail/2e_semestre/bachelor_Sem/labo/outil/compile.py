import ply.lex as lex
import ply.yacc as yacc
import sys

def write(content):
    f = open("res.txt", "w")
    f.write(content)
    f.close()

            #_ _   _                    _   _      
  #__ _ _ __(_) |_| |__  _ __ ___   ___| |_(_) ___ 
 #/ _` | '__| | __| '_ \| '_ ` _ \ / _ \ __| |/ __|
#| (_| | |  | | |_| | | | | | | | |  __/ |_| | (__ 
 #\__,_|_|  |_|\__|_| |_|_| |_| |_|\___|\__|_|\___|
                                                  #
  #__                  _   _                 
 #/ _|_   _ _ __   ___| |_(_) ___  _ __  ___ 
#| |_| | | | '_ \ / __| __| |/ _ \| '_ \/ __|
#|  _| |_| | | | | (__| |_| | (_) | | | \__ \
#|_|  \__,_|_| |_|\___|\__|_|\___/|_| |_|___/
                                            
function_dict= {"add": "%s+%s", "sub":"%s-%s", "mul":"%s*%s", "div":"%s/%s", "concat":"concat(%s,%s)", "set":"set(%s,%s,%s)", "get": "%s[%s]", "insert":"insert(%s,%s)", "append":"append(%s,%s)"}

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
    res=""
    try:
        res= str(eval(f%i))
    except:
        res= "error"
    return res

def write2(content):
    f2 = open("subEval.txt", "w")
    f2.write(content)
    f2.close()


# _                       
#| |    _____  _____ _ __ 
#| |   / _ \ \/ / _ \ '__|
#| |__|  __/>  <  __/ |   
#|_____\___/_/\_\___|_|   

reserved = {
        "in" : "IN",
        "calc" : "CALC",
        "check" : "CHECK",
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

#____                          
#|  _ \ __ _ _ __ ___  ___ _ __ 
#| |_) / _` | '__/ __|/ _ \ '__|
#|  __/ (_| | |  \__ \  __/ |   
#|_|   \__,_|_|  |___/\___|_|   


def p_start(p):
    '''
    start : CALC calc
          | CHECK check
    '''
    #print("action: "+p[1])
                               
#      _               _             
#  ___| |__   ___  ___| | _____ _ __ 
# / __| '_ \ / _ \/ __| |/ / _ \ '__|
#| (__| | | |  __/ (__|   <  __/ |   
# \___|_| |_|\___|\___|_|\_\___|_|   

def p_check(p):
    '''
    check : check1
          | check2
    '''
    p[0]= p[1]
                                    
def p_check1(p):
    '''
    check1 : c_premises MINUS MINUS c_conclusion
    '''
    write(p[1][:-1]+" -- "+p[4])
    print(p[1][:-1]+" -- "+p[4])
    p[0]= "okay"

def p_check2(p):
    '''
    check2 : MINUS MINUS c_conclusion
    '''
    write(" -- "+p[3])
    print(" -- "+p[3])
    p[0]= "okay"

def p_premisses1(p):
    '''
    c_premises : c_statement
    '''
    p[0] = " ".join(p[1:])

def p_premisses2(p):
    '''
    c_premises : c_statement c_more
    '''
    p[0] = " ".join(p[1:])

def p_more1(p):
    '''
    c_more : COMA c_statement
    '''
    p[0] = "; "+p[2]

def p_more2(p):
    '''
    c_more : COMA c_statement c_more
    '''
    p[0] = "; "+p[2]+p[3]

def p_more3(p):
    '''
    c_more : NUM
    '''
    p[0] = p[1]

def p_statement(p):
    '''
    c_statement : c_exp c_sym c_statement2
    '''
    p[0] = " ".join(p[1:])

def p_statement2(p):
    '''
    c_statement2 : c_exp
    '''
    p[0] = " ".join(p[1:])
    #p[0] = str(p[1])

def p_sym(p):
    '''
    c_sym : EQUAL
          | MINUS SUP
          | IN
    '''
    p[0] = "".join(p[1:])

def p_conclusion(p):
    '''
    c_conclusion : c_statement
    '''
    p[0] = p[1]

def p_operator(p):
    '''
    c_exp : NAME OP c_subexp CP
          | c_term
    '''
    p[0] = " ".join(p[1:])

def p_more(p):
    '''
    c_subexp : c_subexp c_moreexp
    '''
    p[0] = p[1]+p[2]

def p_int(p):
    '''
    c_subexp : NUM
             | VAR
             | c_list
    '''
    p[0] = str(p[1])

def p_term(p):
    '''
    c_term : NUM
           | VAR
           | c_list
    '''
    p[0]= str(p[1])

#def p_list(p):
    #'''
    #c_exp : c_list
    #'''
    #p[0] = str(p[1])

def p_list1(p):
    '''
    c_list : OSB c_morelist CSB
    '''
    p[0] = str("["+p[2]+"]")

def p_list2(p):
    '''
    c_morelist : c_term COMA c_morelist
    '''
    p[0] = str(p[1]+","+p[3])

def p_list3(p):
    '''
    c_morelist : c_term
    '''
    p[0] = str(p[1])

def p_list4(p):
    '''
    c_list : OSB CSB
    '''
    p[0] = "[]"

def p_list5(p):
    '''
    c_list : INF c_morelist SUP
    '''
    p[0] = str("["+p[2]+"]")

def p_more_expexp(p):
    '''
    c_moreexp : COMA c_subexp c_moreexp
    '''
    p[0] = "; "+p[2]+p[3]

def p_more_coma_exp(p):
    '''
    c_moreexp : COMA c_subexp
    '''
    p[0] = "; "+p[2]

#           _            _       _             
#  ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
# / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
#| (_| (_| | | (__| |_| | | (_| | || (_) | |   
# \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   

                                              
def p_calc(p):
    '''
    calc : exp
    '''
    write2(str(p[1]))
    #print(str(eval(p[1])))
    p[0]= "calc"
    

def p_calc2(p):
    '''
    calc : condition
    '''
    write2(str(eval(p[1])))
    #print(str(eval(p[1])))
    p[0]= "calc"

def p_condition(p):
    '''
    condition : exp comparator exp
    '''
    p[0] = " ".join(p[1:])

def p_comparator(p):
    '''
    comparator : EQUAL EQUAL
               | SUP
               | SUP EQUAL
               | INF
               | INF EQUAL
    '''
    p[0]= "".join(p[1:])

def p_exp_operator(p):
    '''
    exp : NAME OP exp CP
    '''
    mt= tuple(p[3].split(";"))
    p[0] = func(function_dict.get(p[1], None), mt)

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
    list : INF morelist SUP
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
    write("error")
    write2("error")
    print("error")

parser= yacc.yacc(start='start')

#s="plus(1,2) = element -- <d,empty> -> <d>"
#s="plus(1,2)"
#parser.parse(s)

#while True:
    #try:
        #s = input('')
    #except EOFError:
        #break
    #parser.parse(s)
