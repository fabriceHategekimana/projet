from cmd import Cmd
from mycompile import *
import re

class MyPrompt(Cmd):
    logo= ""+"|"
    prompt = logo+'normal> '
    intro = "<!>Starting the server<!>"
    use_raw_input= False
    mode = "normal"
    p = re.compile(r'\d+')

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
            m = self.p.match(tab[0])
            if m:
                i= int(m.group())
                self.repeate(i, tab[1:])
            else:
                parser.parse(inp)


MyPrompt().cmdloop()
