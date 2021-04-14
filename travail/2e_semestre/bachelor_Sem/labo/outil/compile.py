import ply.lex as lex
import ply.yacc as yacc
import sys

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
                                            
function_dict= {"add": "%s+%s", "sub":"%s-%s", "mul":"%s*%s", "div":"%s/%s", "concat":"concat(%s,%s)", "set":"set(%s,%s,%s)", "get": "%s[%s]", "insert":"insert(%s,%s)", "append":"append(%s,%s)", "remove":"remove(%s,%s)", "removeLast":"removeLast(%s)", "pop":"%s.pop()"}

def removeLast(l):
    l.pop()
    return l

def remove(l, p):
    del l[p]
    return l

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
        "calc" : "CALC",
        "check" : "CHECK",
        "split" : "SPLIT",
        "isList" : "ISLIST",
        "isNumber" : "ISNUMBER",
        "token" : "TOKEN",
        "state" : "STATE"
        }

tokens = [
    'NUM',
    'OP',
    'CP',
    'OSB',
    'CSB',
    'COMA',
    'SEMICOLON',
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
t_SEMICOLON= r'\;'
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
    r'[a-z_][a-zA-Z_0-9]+'
    t.type = reserved.get(t.value,'NAME')
    return t

def t_VAR(t):
    r'[A-Z][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'VAR')
    return t

def t_error(t):
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
          | SPLIT split
          | ISNUMBER isnumber
          | ISLIST list
          | TOKEN token
          | STATE state_exp
    '''
                               
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
    write(p[1]+"--"+p[4])
    p[0]= "okay"

def p_check2(p):
    '''
    check2 : MINUS MINUS c_conclusion
    '''
    write("--"+p[3])
    p[0]= "okay"

def p_premisses1(p):
    '''
    c_premises : c_statement COMA c_premises
    '''
    p[0] = p[1]+";"+p[3]

def p_premisses2(p):
    '''
    c_premises : c_statement
    '''
    p[0] = p[1]

def p_statement(p):
    '''
    c_statement : c_exp c_right_statement
    '''
    p[0] = p[1]+p[2]

def p_right_statement(p):
    '''
    c_right_statement : MINUS SUP VAR
                      | comparator c_term_var
    '''
    p[0] = "".join(p[1:])

def p_right_statement2(p):
    '''
    c_right_statement : IN NAME
    '''
    p[0] = "&in&"+p[2]

def p_c_term_var(p):
    '''
    c_term_var : c_term
               | VAR
    '''
    p[0] = "".join(p[1:])

def p_c_conclusion(p):
    '''
    c_conclusion : c_state_exp EQUAL c_exp
    '''
    p[0] = p[1]+p[2]+p[3]

def p_c_state_exp1(p):
    '''
    c_state_exp : c_list c_exp
    '''
    p[0] = p[1]+p[2]

def p_c_state_exp2(p):
    '''
    c_state_exp : c_exp
    '''
    p[0] = p[1]

def p_c_exp1(p):
    '''
    c_exp : NAME OP c_exp CP
    '''
    p[0] = "".join(p[1:])

def p_c_exp2(p):
    '''
    c_exp : c_term
          | VAR
          | NAME
    '''
    p[0] = p[1]

def p_c_exp3(p):
    '''
    c_exp : c_exp COMA c_exp
    '''
    p[0] = p[1]+";"+p[3]

def p_c_term(p):
    '''
    c_term : NUM
           | c_list
    '''
    p[0]= str(p[1])

#def p_list1(p):
    #'''
    #c_list : OSB c_morelist CSB
    #'''
    #p[0] = str("["+p[2]+"]")

def p_list1(p):
    '''
    c_list : OSB exp CSB
    '''
    p[0] = str("["+p[2]+"]")

#def p_list2(p):
    #'''
    #c_morelist : c_term_var COMA c_morelist
    #'''
    #p[0] = str(p[1]+","+p[3])

#def p_list3(p):
    #'''
    #c_morelist : c_term_var
    #'''
    #p[0] = str(p[1])

def p_list4(p):
    '''
    c_list : OSB CSB
    '''
    p[0] = "[]"

def p_list5(p):
    '''
    c_morelist : c_exp
    '''
    p[0] = p[1]

#def p_list6(p):
    #'''
    #c_list : INF c_morelist SUP
    #'''
    #p[0] = str("<"+p[2]+">")

def p_list6(p):
    '''
    c_list : INF c_exp SUP
    '''
    p[0] = str("<"+p[2]+">")

#           _            _       _             
#  ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
# / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
#| (_| (_| | | (__| |_| | | (_| | || (_) | |   
# \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   

                                              
def p_calc(p):
    '''
    calc : exp
    '''
    write(str(p[1]))
    p[0]= "okay"
    
def p_calc2(p):
    '''
    calc : condition
    '''
    write(str(eval(p[1])))
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
             | NUM SEMICOLON morelist
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
         | SEMICOLON exp more
    '''
    p[0] = ";"+p[2]+p[3]

def p_more_empty(p):
    '''
    more : COMA exp
         | SEMICOLON exp
    '''
    p[0] = ";"+p[2]

           #_ _ _   
 #___ _ __ | (_) |_ 
#/ __| '_ \| | | __|
#\__ \ |_) | | | |_ 
#|___/ .__/|_|_|\__|
    #|_|            

def p_split(p):
    '''
    split : s_exp
    '''
    write(p[1])
    p[0]= "okay"

def p_s_exp1(p):
    '''
    s_exp : NAME OP s_subexp CP
    '''
    p[0] = "".join(p[1:])

def p_s_exp2(p):
    '''
    s_exp : s_term
          | VAR
    '''
    p[0] = p[1]

def p_s_exp3(p):
    '''
    s_exp : s_exp SEMICOLON s_exp
          | s_exp COMA s_exp
    '''
    p[0] = p[1]+";;"+p[3]

def p_s_term(p):
    '''
    s_term : NUM
           | c_list
    '''
    p[0]= str(p[1])

def p_s_subexp1(p):
    '''
    s_subexp : NAME OP s_subexp CP
    '''
    p[0] = "".join(p[1:])

def p_s_subexp2(p):
    '''
    s_subexp : s_term
             | VAR
    '''
    p[0] = p[1]

def p_s_subexp3(p):
    '''
    s_subexp : s_subexp SEMICOLON s_subexp
    '''
    p[0] = p[1]+";"+p[3]

 #_        _              
#| |_ ___ | | _____ _ __  
#| __/ _ \| |/ / _ \ '_ \ 
#| || (_) |   <  __/ | | |
 #\__\___/|_|\_\___|_| |_|
# token

def p_token(p):
    '''
    token : t_statement
          | t_exp
          | t_conclusion
    '''
    write(p[1])

def p_t_statement(p):
    '''
    t_statement : t_exp t_right_statement
    '''
    p[0] = p[1]+"&&"+p[2]

def p_t_right_statement(p):
    '''
    t_right_statement : MINUS SUP VAR
                      | IN NAME
                      | comparator c_term_var
    '''
    p[0] = "&&".join(p[1:])

def p_t_exp1(p):
    '''
    t_exp : NAME OP t_exp CP
    '''
    p[0] = "&&".join(p[1:])

def p_t_exp2(p):
    '''
    t_exp : t_term
          | VAR
          | NAME
    '''
    p[0] = p[1]

def p_t_exp3(p):
    '''
    t_exp : t_exp COMA t_exp
          | t_exp SEMICOLON t_exp
    '''
    p[0] = p[1]+"&&;&&"+p[3]

def p_term(p):
    '''
    t_term : NUM
           | t_list
    '''
    p[0]= str(p[1])

def p_t_conclusion(p):
    '''
    t_conclusion : t_state_exp EQUAL t_exp
    '''
    p[0] = p[1]+"&&"+p[2]+"&&"+p[3]

def p_t_state_exp1(p):
    '''
    t_state_exp : t_list t_exp
    '''
    p[0] = p[1]+"&&"+p[2]

def p_t_state_exp2(p):
    '''
    t_state_exp : t_exp
    '''
    p[0] = p[1]

def p_t_list1(p):
    '''
    t_list : OSB t_exp CSB
    '''
    p[0] =  "[&&"+p[1]+"&&]"

def p_t_list2(p):
    '''
    t_list : INF t_exp SUP
    '''
    p[0] =  "<&&"+p[2]+"&&>"

# isnumber

def p_isnumber(p):
    '''
    isnumber : NUM
    '''
    write("True")
    p[0]="okay"

#     _        _       
# ___| |_ __ _| |_ ___ 
#/ __| __/ _` | __/ _ \
#\__ \ || (_| | ||  __/
#|___/\__\__,_|\__\___|
#state
                      
def p_state_exp(p):
    '''
    state_exp : state exp_or_name
    '''
    write(p[1]+p[2])
    p[0]="okay"

def p_state(p):
    '''
    state : INF c_morelist SUP
    '''
    p[0]= p[2]

def p_exp_or_name1(p): # if it's an expression with some argument, get the arguments
    '''
    exp_or_name : NAME OP c_exp CP
    '''
    p[0]= ","+p[3]

def p_exp_or_name2(p): #when there is juste name() or name, send nothing
    '''
    exp_or_name : NAME OP CP
                | NAME
    '''
    p[0]= ""

def p_error(p):
    if p:
        tok = parser.token()
        if tok:
            write("&Error near "+p.value+" "+tok.value)
        else:
            write("&Error near "+p.value)
    else:
        write("&Syntax error at EOF")

parser= yacc.yacc(start='start')
