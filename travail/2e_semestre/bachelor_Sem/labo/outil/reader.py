#from compile import parser
from evaluation import *

RULES= [
        ['add(n,o)', 'n->m,o->p', 'add(m,p)'],
        ['sub(n,o)', 'n->m,o->p', 'sub(m,p)'],
        ['mul(n,o)', 'n->m,o->p', 'mul(m,p)'],
        ['div(n,o)', 'n->m,o->p', 'div(m,p)']
        ]

def syntaxChecking(exp):
    parser.parse("check "+exp, debug=False)
    f = open("res.txt", "r")
    res= f.readline()
    f.close()
    return res

def decompose(exp):
    if exp[0] == "-":
        tab= exp.split("-- ")
    else:
        tab= exp.split(" -- ")
    entete= tab[1].split(symbol(tab[1]))[0]
    print([entete, tab[0], tab[1]])
    RULES.append([entete, tab[0], tab[1]])

#------------------------------------------

f = open("test.fa", "r")
count= 0
for line in f:
    count += 1
    res= syntaxChecking("check "+line)
    res= line[:-1]
    if res == "error":
        print("Error in line "+ str(count)+": '"+line[:-1]+"'")
        break
    else:
        decompose(res)
    
#EVALUATION

#evaluateExpression("isVoid([])", RULES)
#evaluateExpression("isVoid([1])", RULES)
#evaluateExpression("isVoid([1,2,3])", RULES)

#test typage natif
#evaluateExpression("eval(1)", RULES)
#evaluateExpression("eval([])", RULES)
#Num in number -- eval(Num) = True
#Li in list -- eval(Li) = True

#factorielle
#evaluateExpression("fact(1)", RULES)
evaluateExpression("fact(2)", RULES)



#f.close()
