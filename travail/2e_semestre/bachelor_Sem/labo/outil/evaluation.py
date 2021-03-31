from arithmetique.entree import subEval

def find(state):
    return "<d> -- <d>"

def evaluateState(state):
    rules= find(state)
    for r in rules:
        #[premise,entete,conclusion]
        dico= union(state, r[1])
        res, dico= check(r[0], dico)
        if res:
            state= complete(r[2], dico)
            return state
    return false

def symbol(statement):
    res= ""
    if statement.find(" = ") > -1:
        res= " = "
    elif statement.find(" > ") > -1:
        res= " > "
    elif statement.find(" >= ") > -1:
        res= " >= "
    elif statement.find(" < ") > -1:
        res= " < "
    elif statement.find(" <= ") > -1:
        res= " <= "
    elif statement.find(" -> ") > -1:
        res= " -> "
    elif statement.find(" in ") > -1:
        res= " in "
    return res

def test(expression, substitution):
    res= False
    expression= complete(expression, substitution)
    sym= symbol(expression)
    if sym in [" = ", " > ", " >= ", " < ", " <= "]:
        if sym == " = ":
            expression= expression.replace(" = ", " == ")
        if subEval(expression) == "True":
            res = substitution
            print("le subEval donne True")
        else:
            print("le subEval donne False")
    elif sym == " in ":
        val= evalNativeType(expression)
        if val == "False":
            val= evaluateExpression(expression)
            if val != "False":
                res= val
    elif sym == " -> ":
        res= evaluateExpression(expression)
    #tab= expression.split(sym)
    return res

def evaluateExpression(expression, data):
    print("expression: ", expression)
    final= []
    selection= [data[0]]
    for rule in selection:
        print("règle choisie: ", rule)
        allTrue= True
        substitution= union(rule[0], expression)
        print("substitution obtenue: ", substitution)
        for premise in rule[1].split(";"): #loop: premises
            print("premisse obtenue: ", premise)
            res= test(premise, substitution)
            if res == False:
                allTrue= False
                break
            else:
                substitution= res
        if allTrue == True:
            #conclusion= test(rule[2], substitution)
            conclusion= complete(rule[2],substitution).split(symbol(rule[2]))[1]
            final.append(conclusion)
    print(final)
        

def union(exp1, exp2):
    if exp1[0] == "<":
        res= unionState(exp1, exp2)
    else:
        res= unionExpression(exp1, exp2)
    return res

def unionState(exp1, exp2):
    exp1= exp1.replace("<","").replace(">","")
    exp2= exp2.replace("<","").replace(">","")
    tab1= exp1.split(",")
    tab2= exp2.split(",")
    res= []
    for i in range(len(tab1)):
        res.append([tab1[i], tab2[i]])
    return res

def unionExpression(exp1,exp2):
    res= False
    exp1= exp1[exp1.find("(")+1:exp1.rfind(")")] #pour enlever les espaces en trop du parser
    exp2= exp2[exp2.find("(")+1:exp2.rfind(")")]
    tab1= exp1.split(";")
    tab2= exp2.split(";")

    if len(tab1) == len(tab2):
        final= []
        for i in range(len(tab1)):
            final.append([tab1[i], tab2[i]])
        res= final
    return res

def check(exp, dico):
    tab= exp.split(",")
    for t in tab:
        sub= complete(t,dico)
        res, dico = verifiable(sub,dico)
        if res == False:
           return False, dico 
    return True,dico

def verifiable(exp,dico):
    res= False
    if exp.find("->") > -1:
        #évaluation
        tab= exp.split("->")
        state= evaluate(tab[0])
        if state != False:
            newdico= union(state,tab[1])
            dico += newdico
            res = True
    else:
        #égalité
        tab= exp.split("=")
        for i in range(len(tab)):
            t[i]= myeval(t[i])
        if tab in dico:
            res= True
    return res, dico

def complete(exp, dico):
    for d in dico:
        exp= exp.replace(d[0], d[1])
    return exp

def myeval(exp):
    #utilise mes fonctions définies
    return exp

#print(complete("A+C",union("<A,B,C>","<un,[0;0],3")))
