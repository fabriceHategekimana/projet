import ply.lex as lex
import ply.yacc as yacc
import csv
from module_union import *
from module_db import *
from module_propagation import *

typeTable= {}
VALUES= []
d= Data()

def write(tab, fname):
    with open(fname, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(tab)

# _                       
#| |    _____  _____ _ __ 
#| |   / _ \ \/ / _ \ '__|
#| |__|  __/>  <  __/ |   
#|_____\___/_/\_\___|_|   

reserved = { 
        "add" : "ADD",
        "delete" : "DELETE",
        "check" : "CHECK",
        "display" : "DISPLAY",
        "and" : "AND",
        "or" : "OR",
        "if" : "IF",
        "then" : "THEN",
        "rules" : "RULES",
        "not" : "NOT",
        "links" : "LINKS",
        "nodes" : "NODES"
        }
                         
tokens = [
    'NUM',
    'VAR',
    'ENT'
        ]+list(reserved.values())

t_ignore = r' '

def t_NUM(t):
    r'\d+'
    t.value = str(t.value)
    return t

def t_ENT(t):
    r'[a-zA-Z][a-zA-Z0-9_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value,'ENT')
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
    write(p[1], "res.txt")
    for el in p[1]:
        print(el)
    print("+--------------+")

def p_exp_exp1_ADD(p):
    '''
    exp : ADD modify
    '''
    p[0] = ["value added"]

def p_exp_exp1_DELETE(p):
    '''
    exp : DELETE fact2
    '''
    exp= union(" ".join(p[2]))
    sql= "delete from facts "+exp[exp.index("where"):-1]
    d.sqlModify(sql)
    p[0] = ["value deleted"]

def p_exp_delete_rules(p):
    '''
    exp : DELETE RULES numlist 
    '''
    exp= p[3][:-1] # on retire la virgule en trop à droite
    sql= "delete from rules where id in ("+exp+");"
    d.sqlModify(sql)
    p[0] = ["values deleted"]

def p_exp_numlist(p):
    '''
    numlist : NUM numlist
    '''
    p[0]= p[1]+","+p[2]

def p_exp_numlist_void(p):
    '''
    numlist : 
    '''
    p[0]= ""

def p_exp_exp2(p):
    '''
    exp : CHECK logalg
        | DISPLAY logalg
    '''
    exp= p[2] #enlever l'espace en trop sur la droite
    sql= "select * from "+union(exp)+";"
    p[0] = d.sqlQuery(sql)
    #p[0] = []

def p_exp_check_rule(p):
    '''
    exp : CHECK RULES
    '''
    exp= "select * from rules;"
    p[0] = d.sqlQuery(exp)

def p_exp_check_links(p):
    '''
    exp : CHECK LINKS
    '''
    exp= "select distinct link from facts;"
    p[0] = d.sqlQuery(exp)

def p_exp_check_nodes(p):
    '''
    exp : CHECK NODES
    '''
    exp= "select distinct subject from facts inner join (select distinct goal from facts);"
    p[0] = d.sqlQuery(exp)

def p_exp_modify_fact(p):
    '''
    modify : fact
    '''
    d.sqlModify("insert or ignore into facts (subject,link,goal) values ('%s','%s','%s')" % tuple(p[1]))
    propagation(" ".join(p[1]))
    p[0] = p[1]

def p_exp_modify_rule(p):
    '''
    modify : rule
    '''
    if p[1][0][-1]  == ' ':
        premises= p[1][0][:-1] # enlever le dernier espace à droite
    else:
        premises= p[1][0]
    conclusion= p[1][1]
    d.sqlModify("insert or ignore into rules (premises,conclusion) values ('%s','%s')" % tuple([premises,conclusion]))
    retroPropagation([premises,conclusion]) 
    ENTETE= []
    p[0] = p[1]

def p_exp_fact(p):
    '''
    fact : ENT ENT ENT
         | NOT ENT ENT ENT
         | ENT NOT ENT ENT
         | ENT ENT NOT ENT
    '''
    p[0] = p[1:]

def p_exp_rule(p):
    '''
    rule : IF logalg2 THEN conj2
    '''
    p[0] = [p[2],p[4]]

def p_exp_logalg2(p):
    '''
    logalg2 : fact3 more2
    '''
    p[0] = p[1]+" "+p[2]

def p_exp_logalg(p):
    '''
    logalg : fact2 more
    '''
    p[0] = " ".join(p[1])+p[2]

def p_exp_more(p):
    '''
    more : op fact2 more
    '''
    p[0] = " "+p[1]+" "+" ".join(p[2])+p[3]

def p_exp_more2(p):
    '''
    more2 : op2 fact3 more2
    '''
    p[0] = p[1]+" "+p[2]

def p_exp_more_empty(p):
    '''
    more : 
    '''
    p[0] = ""

def p_exp_more2_empty(p):
    '''
    more2 : 
    '''
    p[0] = ""

def p_exp_op(p):
    '''
    op : AND
       | OR
    '''
    p[0] = p[1].upper()

def p_exp_op2(p):
    '''
    op2 : AND
        | OR
    '''
    p[0] = p[1].upper() #mark

def p_exp_conj2(p):
    '''
    conj2 : fact3 moreconj2
    '''
    p[0] = p[1]+p[2]

def p_exp_AND2(p):
    '''
    moreconj2 : AND fact3 moreconj2
    '''
    p[0] = p[1]+p[2]+p[3]

def p_exp_moreconj2(p):
    '''
    moreconj2 : 
    '''
    p[0] = "" 

def p_exp_predicat(p):
    '''
    fact2 : el el el
    '''
    #varList= getVariables(p[1:])
    #p[0] = ["("+union(p[1:])+")", varList]
    #p[0] = ["("+" ".join(p[1:])+")", varList]
    p[0] = p[1:]

def p_exp_fact3(p):
    '''
    fact3 : el el el
    '''
    p[0] = " ".join(p[1:])

def p_exp_term(p):
    '''
    el : ENT
       | NOT ENT
       | VAR
    '''
    p[0] = " ".join(p[1:])

def p_error(p):
    print("Error bad syntax")

parser= yacc.yacc()


#s1= "add if A est B then A est bleu"
#parser.parse(s1)

#s2= "add if A est comme then A est bleu"
#parser.parse(s2)
