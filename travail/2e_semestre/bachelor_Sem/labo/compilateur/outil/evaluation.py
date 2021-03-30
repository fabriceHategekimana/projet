def find(state):
    return "<d> -- <d>"

def evaluate(state):
    rules= find(state)
    for r in rules:
        #[premise,entete,conclusion]
        dico= union(state, r[1])
        res, dico= check(r[0], dico)
        if res:
            state= complete(r[2], dico)
            return state
    return false

def union(exp1, exp2):
    exp1= exp1.replace("<","").replace(">","")
    exp2= exp2.replace("<","").replace(">","")
    tab1= exp1.split(",")
    tab2= exp2.split(",")
    res= []
    for i in range(len(tab1)):
        res.append([tab1[i], tab2[i]])
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

print(complete("A+C",union("<A,B,C>","<un,[0;0],3")))
