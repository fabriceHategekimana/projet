import ply.lex as lex
import ply.yacc as yacc
import math as m
import csv
from module_union import *
from module_db import *
from module_propagation import *

typeTable= {}
VALUES= []
d= Data()

def writeCSV(tab, fname="res.txt"):
    with open(fname, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(tab)

def write(exp, fname="res.txt"):
    f= open(fname, "w")
    f.write(exp)
    f.close()

def completeAnonymousVariables(exp):
    if exp.find("$VAR$") > -1:
        alphabet= ["_A","_B","_C","_D","_E","_F","_G","_H","_I","_J","_K","_L","_M","_N","_O","_P"]
        if exp.find(" &and& ") > -1:
            tab= exp.split("$VAR$")
            #print("tab:", tab)
            chosenLetters= alphabet[:len(tab)]
            #print("chosenLetters:", chosenLetters)
            exp=""
            for i in range(len(tab)-1):
                exp+= tab[i]+chosenLetters[m.floor(i/2)]
            exp += tab[len(tab)-1]
        else:
            exp= exp.replace("$VAR$", "_A")
    return exp

# _                       
#| |    _____  _____ _ __ 
#| |   / _ \ \/ / _ \ '__|
#| |__|  __/>  <  __/ |   
#|_____\___/_/\_\___|_|   

reserved = { 
        "add" : "ADD",
        "check" : "CHECK",
        "and" : "AND",
        "or" : "OR",
        "if" : "IF",
        "then" : "THEN",
        "not" : "NOT",
        "contains" : "CONTAINS",
        "macro" : "MACRO"
        }
                         
tokens = [
    'NUM',
    'VAR',
    'NAME',
    'STRING',
    'SUP',
    'INF',
    'EQUAL',
    'MINUS',
    'PLUS',
    'DOT'
        ]+list(reserved.values())

t_INF= r'\<'
t_SUP= r'\>'
t_EQUAL= r'\='
t_MINUS= r'\-'
t_PLUS= r'\+'
t_DOT= r'\.'

t_ignore = r' '

def t_NUM(t):
    r'\d+'
    t.value = str(t.value)
    return t

def t_NAME(t):
    r'[a-zA-ZéèêàâïùçÀô][a-zA-Z0-9_éèêàâïùçÀô][a-zA-Z0-9_éèêàâïùçÀô]*'
    t.type = reserved.get(t.value,'NAME')
    return t

def t_VAR(t):
    r'_?[A-Z$]'
    t.type = 'VAR'
    return t

def t_STRING(t):
    r'"([^"\n])*"'
    t.type = reserved.get(t.value,'STRING')
    t.value= t.value[1:-1]
    return t

def t_error(t):
    write("&Error: Illegal characters! ", t)
    t.lexer.skip(1)

lexer= lex.lex()

#----------------------------------

#Parser

def p_start(p):
    '''
    start : ADD add
          | CHECK check
    '''
    print("+--------------+")

def p_add(p):
    '''
    add : fact
        | rule
        | macro
    '''
    write(p[1])

def p_fact(p):
    '''
    fact : ent ent ent_string
    '''
    p[0] = "&&".join(p[1:])

def p_fact_not(p):
    '''
    fact : NOT ent ent ent_string
         | ent NOT ent ent_string
         | ent ent NOT ent_string
    '''
    p[0] = "not("+"&&".join(p[1:]).replace("not&&", "").replace("&&not&&", "").replace("&&not", "")

def p_ent(p):
    '''
    ent : NAME
        | NUM
    '''
    p[0] = p[1]

def p_ent_string(p):
    '''
    ent_string : ent
               | STRING
    '''
    p[0] = p[1]

def p_check(p):
    '''
    check : logalg
    '''
    #print("p[1]:", p[1])
    res= completeAnonymousVariables(p[1])
    #print("res:", res)
    write(res)

def p_logalg1(p):
    '''
    logalg : logalg log_op logalg
    '''
    p[0] = p[1]+" &"+p[2]+"& "+p[3]

def p_logalg2(p):
    '''
    logalg : ent_var ent_var ent_var_string
           | ent_var check_op ent_string
    '''
    p[0] = "&&".join(p[1:])

def p_logalg2_not(p):
    '''
    logalg : NOT ent_var ent_var ent_var_string
           | ent_var NOT ent_var ent_var_string
           | ent_var ent_var NOT ent_var_string
    '''
    p[0] = "not("+"&&".join(p[1:]).replace("not&&", "").replace("&&not&&", "").replace("&&not", "")

def p_logalg_short1(p):
    '''
    logalg : ent_var ent_var
    '''
    p[0] = "&&".join(p[1:])+"&&$VAR$" #add an anonimous variable

def p_logalg_short2(p):
    '''
    logalg : ent_var DOT tail
    '''
    p[0] = p[1]+"&&"+p[3]

def p_logalg_short3(p):
    '''
    logalg : ent_var ent_var check_op ent_string 
    '''
    p[0] = p[1]+"&&"+p[2]+"&&$VAR$ &and& $VAR$&&"+p[3]+"&&"+p[4]

def p_logalg_tail1(p):
    '''
    tail : ent tail
    '''
    p[0] = p[1]+"&&$VAR$ &and& $VAR$&&"+p[2] #combine with a chain of anonimous variables

def p_logalg_tail2(p):
    '''
    tail : ent
    '''
    p[0] = p[1]+"&&$VAR$"

def p_logalg_tail3(p):
    '''
    tail : ent VAR
    '''
    p[0] = p[1]+"&&"+p[2]

def p_ent_var_string(p):
    '''
    ent_var_string : ent_string
                   | VAR
    '''
    p[0] = p[1]

def p_ent_var(p):
    '''
    ent_var : ent
            | VAR
    '''
    p[0] = p[1]

def p_log_op(p):
    '''
    log_op : AND
           | OR
    '''
    p[0] = p[1]

def p_check_op(p):
    '''
    check_op : INF
             | SUP
             | EQUAL
             | INF EQUAL
             | SUP EQUAL
             | MINUS CONTAINS
    '''
    p[0] = "".join(p[1:])

def p_rule(p):
    '''
    rule : IF logalg_rule THEN logalg_rule
    '''
    p[0] = p[2].replace("&&", " ")+"&&rule&&"+p[4].replace("&&", " ")

def p_logalg_rule1(p):
    '''
    logalg_rule : logalg_rule log_op logalg_rule
    '''
    p[0] = p[1]+" &"+p[2]+"& "+p[3]

def p_logalg_rule2(p):
    '''
    logalg_rule : ent_var ent_var ent_var
                | ent_var check_op ent
    '''
    p[0] = "&&".join(p[1:])

def p_macro(p):
    '''
    macro : MACRO
    '''
    p[0] = p[1]

def p_error(p):
    write("&Error bad syntax")

parser= yacc.yacc()
