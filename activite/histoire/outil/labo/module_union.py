from module_db import *
d= Data()
ENTETE=[]

def isComplet(tab):
    res= True
    for t in tab:
        if t.count('A') + t.count('B') + t.count('C') > 0:
           res= False 
    return res

def getVariables(exp):
    final= []
    for e in exp:
        if e in ["A","B","C"] and e not in final:
            final.append(e)
    return final

def match(l1,l2):
    res= False
    for l in l1:
        if l in l2:
            res= True
    return res

def variableIndex(command):
    variables= []
    values= []
    column= ["","subject","","link","","goal"]
    tab= command
    for i in range(len(tab)): # on explore les éléments de la commande
        if tab[i] in ["not",""]: # si on tombe sur un 'not' ou pas on l'ajoute par défaut
            values.append(tab[i])
        elif tab[i] in ["A","B","C"]: # si on trouve une variable
            variables.append(column[i]+" as "+tab[i]) # on l'ajoute à la table des variables
            values.pop() # on retire le 'not' ou le '' ajouté précédement dans values
        else: # sinon on ajoute le nom de la column et la valeur
            values.append(column[i])
            values.append(tab[i])
    return tuple(variables), tuple(values)

def createUnionQuery(command):
    command= completeNot(command)
    variables, values = variableIndex(command)
    if len(variables) == 2:
        tvariable= "%s,%s" % variables
        tvalue= "%s %s='%s'" % values
    elif len(variables) == 1:
        tvariable= "%s" % variables
        tvalue= "%s %s='%s' and %s %s='%s'" % values
    sql= "(select "+tvariable+" from facts where "+tvalue+")"
    return sql

def convert(exp):
    exp= exp.split(" ")
    res= []
    if isComplet(exp):
        exp= completeNot(exp)
        t= tuple(exp)
        sql= "(select * from facts where %s subject='%s' and %s link='%s' and %s goal='%s'" % t+")"
        #else:
            #t= tuple(exp)
            #sql= "(select * from facts where subject='%s' and link='%s' and goal='%s'" % t+")"
        return sql
    else:
        sql= createUnionQuery(exp)
        return sql

def hasNot(exp):
    return "not" in exp

def completeNot(exp):
    if hasNot(exp):
        pos= exp.index("not") 
        if pos == 0:
            exp.insert(2, "")
            exp.insert(4, "")
        elif pos == 1:
            exp.insert(0, "")
            exp.insert(4, "")
        elif pos == 2:
            exp.insert(0, "")
            exp.insert(2, "")
    else:
        exp.insert(0, "")
        exp.insert(2, "")
        exp.insert(4, "")
    return exp

def setAND(exp, varList):
    for i in range(len(varList)-1):
        if match(varList[i],varList[i+1]):
            exp= exp.replace("AND","NATURAL JOIN",1)
        else:
            exp= exp.replace("AND","CROSS JOIN",1)
    return exp

def union(exp):
    final= []
    tabOR= exp.split(" OR ")
    for t in tabOR:
        varList= []
        tabAND= t.split(" AND ")
        subexp= ""
        for i in range(len(tabAND)): # on converti chaque conjonction
            var= getVariables(tabAND[i])
            subexp += convert(tabAND[i])+" AND "
            varList.append(var)
        subexp= subexp[:-5] # on enlève le " AND " en trop
        num= len(t.split(" AND "))
        final.append(setAND(subexp, varList))
    #dernier traitement des parenthèses à côté des or
    for i in range(1,len(final)):
        final[i]= final[i].replace("(","",1).replace(")","",1)
    return " UNION ".join(final)
        
