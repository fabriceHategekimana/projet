from module_evaluation import *
from module_db import *

d = Data()

RULES= [
        ['add(N;O)', 'N->P;O->Q', 'add(P;Q)'],
        ['sub(N;O)', 'N->P;O->Q', 'sub(P;Q)'],
        ['mul(N;O)', 'N->P;O->Q', 'mul(P;Q)'],
        ['div(N;O)', 'N->P;O->Q', 'div(P;Q)'],
        ['get(L)', 'L->Lp', 'get(Lp)'],
        ['set(L,N)', 'Li->Lp;N->Np', 'set(Lp;Np)'],
        ['append(L,N)', 'L->Lp;N->Np', 'append(Lp;Np)'],
        ['insert(L,N)', 'L->Lp;N->Np', 'insert(Lp;Np)'],
        ['remove(L,N)', 'L->Lp;N->Np', 'remove(Lp;Np)'],
        ['removeLast(L)', 'L->Lp', 'removeLast(Lp)']
        ]

def formatRule(exp):
    res= syntaxChecking(exp)
    if res[0] == "&":
        res= "error"
    else:
        res= res.replace(" ", "")
        res= decompose(res)
    return res

def syntaxChecking(exp):
    parser.parse("check "+exp, debug=False)
    f = open("res.txt", "r")
    res= f.readline()
    f.close()
    return res

def decompose(exp):
    tab= exp.split("--")
    entete= tab[1].split(symbol(tab[1]))[0]
    print([entete, tab[0], tab[1]])
    return [entete, tab[0], tab[1]]

def evaluateInstruction(inst, rules):
    #EVALUATION
    print("[retour]> "+str(evaluateExpression(inst, rules)))

def getRules():
    return d.sqlQuery("select header,premises,conclusion from exp_rules;")

def insertRule(rule):
    d.sqlModify("insert into exp_rules(header, premises, conclusion) values('%s','%s','%s');" % tuple(rule))

def insertDefaultRules():
    for rule in RULES:
        insertRule(rule)

def importRules(name):
    #On vide les bases de données
    d.sqlModify("delete from exp_rules")
    d.sqlModify("delete from state_rules")
    insertDefaultRules()
    #On ouvre le fichier
    f = open(name, "r")
    count= 0
    error= False
    #Pour chaque ligne on test si la règle est juste puis on continue
    for line in f:
        count += 1
        res= syntaxChecking(line)
        if res[0] == "&":
            print("Error in line "+ str(count)+": '"+line[:-1]+"' \n"+res[1:])
            error= True
            break
        else:
            res= res.replace(" ", "")
            rule= decompose(res)
            #On insère la règle traitée
            insertRule(rule)
