from cmd import Cmd
from mycompile import *
from module_network import *
import re
import csv


class MyPrompt(Cmd):
    logo= ""+"|"
    prompt = logo+'normal> '
    intro = "<!>Starting the server<!>"
    use_raw_input= False
    mode = "normal"
    p = re.compile(r'\d+')
    COMPLETIONLIST= []

    def do_exit(self, inp):
        return True

    def do_mode(self, inp):
        if inp in ["normal","union","sql"]:
            self.prompt = self.logo+'%s> ' % inp
            self.mode= inp
        else:
            print("This is note a mode")
            print("Availiable modes: normal, union, sql")

    def do_logo(self, inp):
        self.logo= inp+"|"
        self.prompt = self.logo+'%s> ' % self.mode

    def do_apply(self, inp):
        tab= inp.split(" ")
        if len(tab) >= 2:
            if tab[0] == "rules":
                res= d.sqlQuery("select * from rules where id in ("+",".join(tab[1:])+");")
            else:
                print("Error bad syntax")
        elif len(tab) == 1:
            if tab[0] == "rules":
                res= d.sqlQuery("select * from rules;")
        print("rules selected: ", res)
        for r in res:
            retroPropagation(r[1:])

    def repeate(self, num, tab):
        if tab[0] == "add" and len(tab) == 2:
            for i in range(1,num+1):
                parser.parse("add "+tab[1]+str(i)+" est "+tab[1])
        else:
            print("Error bad syntax")

    def default(self, inp):
        if self.mode == "normal":
            self.normal(inp)
        elif self.mode == "union":
            self.union(inp)
        elif self.mode == "sql":
            self.sql(inp)
        else:
            print("ce mode ne produit rien")


    def do_export(self, inp):
        tab= inp.split(" ")
        if len(tab) == 3 and tab[0] == "to" and tab[1] in ["csv", "gephy"]:
            if inp.find(".csv") == -1:
                inp += ".csv"
            self.toCSV(tab[2],tab[1])
        else:
            print("Bad sytax. \nRight format: 'export to [format] [name]'")
            print("[format]: csv or gephy")

    def do_import(self, inp):
        self.fromCSV(inp) 

    def do_insert(self, inp):
        d.sqlQuery(inp)

    def do_clear(self, inp):
        d.sqlModify("delete from facts")
        tab= inp.split(" ")
        if len(tab) == 2 and tab[1] == "all":
            d.sqlModify("delete from rules")
        print("database cleared!")

    def do_rename(self, inp):
        #["nodes or links", "old", "new"]
        tab= inp.split(" ")
        if len(tab) == 3:
            if tab[0] == "nodes":
                d.sqlModify("update facts set subject='"+tab[2]+"' where subject='"+tab[1]+"'")
                d.sqlModify("update facts set goal='"+tab[2]+"' where goal='"+tab[1]+"'")
            elif tab[0] == "links":
                d.sqlModify("update facts set link='"+tab[2]+"' where link='"+tab[1]+"'")
            else:
                print("Bad syntax. It should be: 'rename [target] [oldname] [newname]")
                print("[target]= nodes or links")

    def do_display(self, inp):
        parser.parse("display "+inp)
        tabInp= self.splitOneDimension(inp)
        with open("res.txt") as f:
            reader = csv.reader(f)
            tab = list(reader)
        facts=[]
        for inp in tabInp:
            for ligne in tab:
                res= self.completeDisplay(ligne, inp).split(" ")
                facts.append(res)
        displayNetwork(facts)
        write(facts, "append.csv")

    def do_append(self, inp):
        parser.parse("display "+inp)
        tabInp= self.splitOneDimension(inp)
        with open("res.txt") as f:
            reader = csv.reader(f)
            tab = list(reader)
        with open("append.csv") as f:
            reader = csv.reader(f)
            oldFacts = list(reader) # cette table est déjà formatée
        facts=[]
        for inp in tabInp:
            for ligne in tab:
                res= self.completeDisplay(ligne, inp).split(" ")
                facts.append(res)
        facts += oldFacts
        displayNetwork(facts)
        write(facts, "append.csv")

    def completeDisplay(self, ligne, inp):
        substitution= ["A","B","C"]
        res= inp.replace("not ","")
        for i in range(len(ligne)):
            res= res.replace(substitution[i], ligne[i])
        return res

    def splitOneDimension(self, inp):
        final= []
        tab1= inp.split(" or ")
        for t1 in  tab1:
            tab2= t1.split(" and ")
            for t2 in tab2:
                final.append(t2)
        return final

    def sql(self,inp):
        try:
            print(d.sqlQuery(inp))
        except:
            print("Error this is not a sql query")

    def union(self, inp):
        print(union(inp))
        #try:
            #print(union(inp))
        #except:
            #print("Error this is not a predicat")

    def normal(self,inp):
            tab= inp.split(" ")
            m = self.p.match(tab[0]) #si c'est un nombre
            if m:
                i= int(m.group())
                self.repeate(i, tab[1:])
            else:
                parser.parse(inp)

    def completedefault(self, text, line, begidx, endidx):
        sql= "select distinct subject from facts where subject like '"+text+"%' union select distinct link from facts where link like '"+text+"%' union select distinct goal from facts where goal like '"+text+"%'"
        completions= self.simpleList(d.sqlQuery(sql))
        return completions

    def toCSV(self, name, csvFormat):
        if csvFormat == "gephy":
            tab= d.sqlQuery("select subject,goal,link from facts;")
            tab.insert(0, ["source","target","link"])
        else:
            tab= d.sqlQuery("select * from facts;")
            tab.insert(0, ["subject","link","goal"])
        with open(name, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(tab)

    def fromCSV(self, name):
        with open(name) as f:
            reader = csv.reader(f)
            tab = list(reader)
        try:
            if len(tab[0]) == 3 and tab[0]:
                entete= tab.pop(0)
                print("entete: ", entete)
                if entete == ["subject","target","link"]: # pour gephy
                    for t in tab:
                        addFact(" ".join([t[0],t[2],t[1]]))
                elif entete == ["subject","link","goal"]:
                    for t in tab:
                        addFact(" ".join(t))
        except:
            print("The csv file has not the good format: ('subject,target,link' or 'subject,goal,link')")

    def simpleList(self, list2d):
        final= []
        for element in list2d:
            final.append(element[0])
        return final

MyPrompt().cmdloop()
