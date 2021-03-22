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
        if e in ["A","B","C"]:
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
    column= ["subject","link","goal"]
    tab= command
    for i in range(len(tab)):
        if tab[i] in ["A","B","C"]:
            variables.append(column[i])
        else:
            values.append(column[i])
            values.append(tab[i])
    return tuple(variables), tuple(values)

def createUnionQuery(command):
    variables, values = variableIndex(command)
    if len(variables) == 2:
        tvalue= "%s='%s'" % values
        tvariable= "%s,%s" % variables
    elif len(variables) == 1:
        tvariable= "%s" % variables
        tvalue= "%s='%s' and %s='%s'" % values
    sql= "(select "+tvariable+" from facts where "+tvalue+")"
    return sql

def convert(exp):
    exp= exp.split(" ")
    res= []
    if isComplet(exp):
        t= tuple(exp)
        sql= "(select * from facts where subject='%s' and link='%s' and goal='%s'" % t+")"
        return sql
    else:
        sql= createUnionQuery(exp)
        #val= d.sqlQuery(sql)
        return sql

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
    index= 0
    for t in tabOR:
        varList= []
        tabAND= t.split(" AND ")
        subexp= ""
        for i in range(len(tabAND)):
            var= getVariables(tabAND[i])
            subexp += convert(tabAND[i])+" AND "
            varList.append(var)
        subexp= subexp[:-5]
        num= len(t.split(" AND "))
        final.append(setAND(subexp, varList))
        index += num
    return " UNION ".join(final)

#PROPAGATION
#if val == []:
    #return []
#elif:
    #for v in val:
        #newCommand= complete(v, command)
        #res += union(newCommand)
    #return res

#cmd="francois dans classe1"
#print(union(cmd))
