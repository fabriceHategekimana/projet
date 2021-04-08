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

#------------------------------------------

f = open("test.fa", "r")
count= 0
for line in f:
    count += 1
    res= syntaxChecking(line).replace(" ", "")
    #res= line[:-1]
    print("syntaxChecking: ", res)
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
#-- fact(1) = 1
#N > 1 -- fact(N) = mul(N,fact(sub(N,1)))
#evaluateExpression("fact(1)", RULES)
#print(RULES)
#evaluateExpression("fact(2)", RULES)
#evaluateExpression("fact(4)", RULES)

#liste
#evaluateExpression("get([1,2,3],2)", RULES)
#evaluateExpression("len([1])", RULES)

#f.close()
