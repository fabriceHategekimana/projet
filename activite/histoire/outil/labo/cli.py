from cmd import Cmd
from mycompile import *
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

    def do_completion(self, inp):
        print(self.COMPLETIONLIST)

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

    def sql(self,inp):
        try:
            print(d.sqlQuery(inp))
        except:
            print("Error this is not a sql query")

    def union(self, inp):
        try:
            print(union(inp))
        except:
            print("Error this is not a predicat")

    def normal(self,inp):
            tab= inp.split(" ")
            m = self.p.match(tab[0]) #si c'est un nombre
            if m:
                i= int(m.group())
                self.repeate(i, tab[1:])
            else:
                parser.parse(inp)
                self.completion()

    def completion(self):
        for val in VALUES:
            for v in val:
                if v not in completionList:
                    self.COMPLETIONLIST.append(v)

    def completedefault(self, text, line, begidx, endidx):
        if not text:
            completions = self.COMPLETIONLIST[:]
        else:
            completions = [ f
                            for f in self.COMPLETIONLIST
                            if f.startswith(text)
                            ]
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



MyPrompt().cmdloop()
