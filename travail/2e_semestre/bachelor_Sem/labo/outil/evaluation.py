from compile import parser
import re

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
    if statement.find("->") > -1:
        res="->"
    elif statement.find("in") > -1:
        res="in"
    elif statement.find("=") > -1:
        res= "="
    elif statement.find(">") > -1:
        res=">"
    elif statement.find(">=") > -1:
        res=">="
    elif statement.find("<") > -1:
        res="<"
    elif statement.find("<=") > -1:
        res="<="
    return res

def test(expression, substitution, data):
    res= False
    expression= complete(expression, substitution)
    print("expression à tester: ", expression)
    sym= symbol(expression)
    if sym in ["=",">",">=","<","<="]:
        if sym =="=":
            expression= expression.replace("=","==")
        val= subEval(expression)
        print("résultat du test de comparaison: ", val)
        if val == "True":
            res = substitution
    elif sym == "in":
        val= evalNativeType(expression)
        print("résultat du test in 1: ", val)
        if val == False:
            print("on continue")
            #val= evaluateExpression(expression)
            #print("résultat du test in 2: ", val)
            #if val != "False":
                #res= val"
        else:
            res= True
    elif sym == "->":
        tab= expression.split("->")
        res= evaluateExpression(tab[0], data)
        print("résultat du test -> : ", res)
        substitution.append([tab[1], res])
        res= substitution
    return res

def evalNativeType(exp):
    res= False
    if exp.find("in number") > 0:
        res= isNumber(exp.replace(" in number", ""))
    elif exp.find("in list") > 0:
        res= isList(exp.replace(" in list", ""))
    return res

def evaluateExpression(expression, data):
    print("------------------------EVAL")
    print("subEval de l'expression: ", expression)
    res= subEval(expression) 
    if not isTerminal(res):
        res= evaluateExpressionHelper(expression, data)
    print("résultat rendu par l'interpréteur: ", res)
    return res

def evaluateExpressionHelper(expression, data):
    print("------------------------EE")
    print("expression: ", expression)
    final= ""
    selection= getSelection(expression, data)
    print("selection: ", selection)
    for rule in selection:
        res= applyRule(expression, rule, data)
        if res != False:
            final= res
            break
    return final

def applyRule(expression, rule, data):
    print("--------------------RULE")
    print("règle choisie: ", rule)
    final= ""
    allTrue= True
    substitution= union(rule[0], expression) 
    if substitution == False: # if false the fact doesn't match go to the next rule/fact
        print("Le fait ne match pas, on passe à la suite")
        allTrue= False
        final= False
    elif substitution == True: # if true the fact match go directly to the conclusion
        print("Le fait match")
    else: # if this is an array of substitution, go check the premises
        print("substitution obtenue: ", substitution)
        if rule[1] != "":
            for premise in rule[1].split(";"): #loop: premises
                print("premisse obtenue: ", premise)
                res= test(premise, substitution, rule)
                print("res: ",res)
                if res == False:
                    print("règle non accomplie")
                    allTrue= False
                    break
                else:
                    print("règle accomplie")
                    substitution= res
    if allTrue == True:
        if substitution != True: # on fait les dernière substitutions si le tableau n'est pas vide
            conclusion= complete(rule[2],substitution).split(symbol(rule[2]))[1]
        else:
            conclusion= rule[2].split(symbol(rule[2]))[1]
        print("conclusion: ", conclusion)
        final= evaluateExpression(conclusion, data)
    return final

def getSelection(exp, data):
    final= []
    name= getName(exp)
    for rule in data:
        if getName(rule[0]) == name:
            final.append(rule)
    return final

def getName(exp):
    name= re.findall("\w+\(", exp)
    if name == []:
        name = [""]
    return name[0]
        
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
    #exp1 is the rule union, exp2 is the user union
    res= False
    exp1= exp1[exp1.find("(")+1:exp1.rfind(")")] #on enlève les parenthèses en trop
    exp2= exp2[exp2.find("(")+1:exp2.rfind(")")]
    tab1= splitByExpression(exp1)
    tab2= splitByExpression(exp2)

    print("tab1", tab1)
    print("tab2", tab2)

    final= []
    if len(tab1) == len(tab2): #si les tables font la même longueur
        for i in range(len(tab1)): #on explore
            if isTerminal(tab1[i]): #si si l'élément à gauche est fini
                res1= subEval(tab1[i])
                res2= subEval(tab2[i])
                print("res1: ",res1)
                print("res2: ",res2)
                if res1 != res2:
                    final= False
                    break
            else:
                final.append([tab1[i], tab2[i]])
        if final == []:
            final = True
    print("résultat de l'union: ", final)
    return final

def splitByExpression(exp):
    return myParser("split "+exp).split(";;")

def isNumber(exp):
    res= myParser("isNumber "+exp)
    if res != "error":
        res = True
    else:
        res = False
    print("isNumber de "+exp+": "+str(res))
    return res

def isList(exp):
    res = False
    try:
        if eval("isinstance(%s, list)" % (exp)):
            res = True
    except:
        pass
    print("isList de "+exp+": "+str(res))
    return res

def isTerminal(exp):
    res= False
    if isNumber(exp) or isList(exp):
        res= True
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

def subEval(exp):
    res= myParser("calc "+exp)
    if res == "error":
        print("subEval a échoué")
        res= exp
    return res

def myParser(exp):
    parser.parse(exp)
    f = open("res.txt", "r")
    res= f.readline()
    f.close()
    return res

#print(complete("A+C",union("<A,B,C>","<un,[0;0],3")))
