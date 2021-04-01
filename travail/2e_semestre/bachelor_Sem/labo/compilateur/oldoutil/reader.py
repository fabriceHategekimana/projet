from compile import *

RULES= []

def subeval(exp):
    parser.parse(exp, debug=False)
    f = open("res.txt", "r")
    res= f.readline()
    f.close()
    return res

def symbol(statement):
    if statement.find(" = ") > -1:
        res= " = "
    elif statement.find(" -> ") > -1:
        res= " -> "
    elif statement.find(" in ") > -1:
        res= " in "
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
    res= subeval(line)
    if res == "error":
        print("Error in line "+ str(count)+": '"+line[:-1]+"'")
        break
    else:
        decompose(res)
    
#parser.parse(exp, debug=False)
f.close()
