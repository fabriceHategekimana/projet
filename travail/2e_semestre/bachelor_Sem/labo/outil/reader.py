from evaluation import *

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
    RULES.append([entete, tab[0], tab[1]])

def evaluateInstruction(inst):
    #EVALUATION
    print("[retour]> "+str(evaluateExpression(inst, RULES)))

    #test typage natif
    #print("[retour]> "+evaluateExpression("eval(1)", RULES))
    #print("[retour]> "+evaluateExpression("eval([])", RULES))
    #Num in number -- eval(Num) = True
    #Li in list -- eval(Li) = True

    #factorielle
    #print("[retour]> "+evaluateExpression("fact(3)", RULES))
    #print("[retour]> "+evaluateExpression("fact(2)", RULES))
    #print("[retour]> "+evaluateExpression("fact(3)", RULES))

    #liste
    #print("[retour]> "+evaluateExpression("get([1,2,3],2)", RULES))
    #print("[retour]> "+evaluateExpression("len([23,2,3,4])", RULES))


#------------------------------------------

f = open("test.fa", "r")
count= 0
error= False
for line in f:
    count += 1
    res= syntaxChecking(line)
    if res[0] == "&":
        print("Error in line "+ str(count)+": '"+line[:-1]+"' \n"+res[1:])
        error= True
        break
    else:
        res= res.replace(" ", "")
        decompose(res)
if error == False:
    evaluatenstruction("maxL([1,2,12,4,5])")
