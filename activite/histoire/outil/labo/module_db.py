import sqlite3

class Data(): 
    nom="test.db"

    def __init__(self):
        self.conn= sqlite3.connect(self.nom)
        self.c= self.conn.cursor()

    def sqlQuery(self, sql):
        tab= []
        res= self.c.execute(sql)
        for ligne in res:
            tab.append(list(ligne))
        return tab

    def sqlModify(self, sql):
        res= self.c.execute(sql)
        self.conn.commit()

d= Data()

def isComplet(tab):
    res= True
    for t in tab:
        if t.count('A') + t.count('B') + t.count('C') > 0:
           res= False 
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
        tvalue= "%s=%s" % values
        tvariable= "%s,%s" % variables
    elif len(variables) == 1:
        tvariable= "%s" % variables
        tvalue= "%s='%s' and %s='%s'" % values
    sql= "select "+tvariable+" where "+tvalue
    return sql

def union(command):
    res= []
    if isComplet(command):
        t= tuple(command)
        sql= "select * from test where subject='%s' and link='%s' and goal='%s';" % t
        return sql
    else:
        sql= createUnionQuery(command)
        #val= d.sqlQuery(sql)
        return sql

#PROPAGATION
#if val == []:
    #return []
#elif:
    #for v in val:
        #newCommand= complete(v, command)
        #res += union(newCommand)
    #return res

def eval(s):
    exp= s.split(" ")
    if  exp[0] == "add":
        d.sqlModify("insert into test (subject,link,goal) values ('%s','%s','%s');" % tuple(exp[1:]))
        print("data added")
    if  exp[0] == "delete":
        d.sqlModify("delete from test where subject='%s'and link='%s'and goal='%s';" % tuple(exp[1:]))
        print("data removed")
    elif exp[0] == "check":
        final= union(exp[1:])
        print(final)
        #tab= d.sqlQuery("select * from test where subject='%s'and link='%s'and goal='%s';" % tuple(final))
        #print(tab)
    else:
        print("error: bad syntax")

print("<!>Starting the server<!>")
while True:
    try:
        s = input('')
    except EOFError:
        break
    eval(s)

