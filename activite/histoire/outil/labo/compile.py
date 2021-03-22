import ply.lex as lex
import ply.yacc as yacc
import sys
from module_union import *
from module_db import *

typeTable= {}
d= Data()

def match(l1,l2):
    res= False
    for l in l1:
        if l in l2:
            res= True
    return res

def getVariables(exp):
    final= []
    for e in exp:
        if e in ["A","B","C"]:
            final.append(e)
    return final

def setAND(exp, varList):
    for i in range(len(varList)-1):
        if match(varList[i],varList[i+1]):
            exp= exp.replace("AND","NATURAL JOIN",1)
        else:
            exp= exp.replace("AND","CROSS JOIN",1)
    return exp

def setORAND(exp, varList):
    final= []
    tabOR= exp.split(" OR ")
    index= 0
    for t in tabOR:
        num= len(t.split(" AND "))
        final.append(setAND(t, varList[index:index+num]))
        index += num
    return " UNION ".join(final)
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
        "rules" : "RULES"
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
    print(p[1])
    print("+--------------+")

def p_exp_exp1_ADD(p):
    '''
    exp : ADD modify
    '''
    p[0] = "value added"

def p_exp_exp1_DELETE(p):
    '''
    exp : DELETE fact2
    '''
    exp= p[2][0]
    sql= "delete from facts "+exp[exp.index("where"):-1]
    d.sqlModify(sql)
    p[0] = "value deleted"

def p_exp_delete_rules(p):
    '''
    exp : DELETE RULES numlist 
    '''
    sql= "delete from facts where id in ("+str(p[3])+");"
    d.sqlModify(sql)
    p[0] = "values deleted"

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
    exp= "select * from "+setORAND(p[2][0], p[2][1])+";"
    p[0] = d.sqlQuery(exp)

def p_exp_check_rule(p):
    '''
    exp : CHECK RULES
    '''
    exp= "select * from rules;"
    p[0] = d.sqlQuery(exp)



def p_exp_modify_fact(p):
    '''
    modify : fact
    '''
    d.sqlModify("insert into facts (subject,link,goal) values ('%s','%s','%s')" % tuple(p[1]))
    p[0] = p[1]

def p_exp_modify_rule(p):
    '''
    modify : rule
    '''
    d.sqlModify("insert into rules (premises,conclusion) values ('%s','%s')" % tuple(p[1]))
    p[0] = p[1]

def p_exp_fact(p):
    '''
    fact : ENT ENT ENT
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
    exp= p[1][0]+p[2][0]
    p[2][1].insert(0, p[1][1])
    p[0] = [exp, p[2][1]]

def p_exp_more(p):
    '''
    more : op fact2 more
    '''
    exp = " "+p[1]+" "+p[2][0]+p[3][0]
    p[3][1].insert(0, p[2][1])
    p[0] = [exp, p[3][1]]

def p_exp_more2(p):
    '''
    more2 : op2 fact3 more2
    '''
    p[0] = p[1]+" "+p[2]

def p_exp_more_empty(p):
    '''
    more : 
    '''
    p[0] = ["", []]

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
    p[0] = p[1]

#def p_exp_conj(p):
    #'''
    #conj : fact2 moreconj
    #'''
    #p[0] = p[1]+p[2]

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

#def p_exp_AND(p):
    #'''
    #moreconj : AND fact2 moreconj
    #'''
    #p[0] = p[1].upper()+p[2]+p[3]

#def p_exp_moreconj(p):
    #'''
    #moreconj : 
    #'''
    #p[0] = "" 

def p_exp_predicat(p):
    '''
    fact2 : el el el
    '''
    varList= getVariables(p[1:])
    p[0] = ["("+union(p[1:])+")", varList]

def p_exp_fact3(p):
    '''
    fact3 : el el el
    '''
    p[0] = " ".join(p[1:])

def p_exp_term(p):
    '''
    el : ENT
       | VAR
    '''
    p[0] = p[1]

def p_error(p):
    print("Error")

parser= yacc.yacc()

print("<!>Starting the server<!>")

while True:
    try:
        s = input('')
    except EOFError:
        break
    parser.parse(s)
