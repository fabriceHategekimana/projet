from compile import parser1
#from evaluation import evaluateExpression, symbol

RULES= []

def syntaxChecking(exp):
    parser1.parse(exp, debug=False)
    f = open("res.txt", "r")
    res= f.readline()
    f.close()
    return res

def decompose(exp):
    tab= exp.split(" -- ")
    entete= tab[1].split(symbol(tab[1]))[0]
    print([entete, tab[0], tab[1]])
    RULES.append([entete, tab[0], tab[1]])

f = open("test.fa", "r")
count= 0
for line in f:
    count += 1
    #res= syntaxChecking(line)
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

#f.close()
