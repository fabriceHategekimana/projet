from cmd import Cmd
from module_compile import *
import re
from module_rules import *
from module_network import *

class MyPrompt(Cmd):
    prompt = '>'
    use_raw_input= False
    state= ""
    STATIC_RULES= []
    RULES= []
    STACK= []
    ERROR= False
    exp= ""

    def do_exit(self, inp):
        return True

    def do_append(self, inp):
        self.stackAppend(inp)
        tab= d.sqlQuery("select * from links;")
        print(tab)

    def do_display(self, inp):
        tab= d.sqlQuery("select * from links;")
        displayNetwork(tab)

    def do_step(self, inp):
        if self.RULES == []:
           print("rules selection")
           rules= getRules() #On prend les règles enregistrées dans la base de données
           self.RULES= getSelection(self.exp, rules)
           self.STATIC_RULES= self.RULES.copy()
        else:
           r= self.RULES.pop(0)
           rules= getRules()
           self.stackAppend(r[1]+"--"+r[2])
           newExp= applyRule2(self.exp, r) 
           self.stackAppend(newExp)
           print("exp: ", newExp)
           if newExp != "error":
               self.ERROR= False
               self.RULES= []
               self.exp= newExp
           else:
               self.ERROR= True
               self.stackPop()

    def do_state(self, inp):
        print("--------------------------------------")
        print("selected_rules:", self.STATIC_RULES)
        if self.RULES != []:
            print("next rule:", self.RULES[0])
        else:
            print("next rule:")
        print("expression:", self.exp)
        print("state: ", self.state)
        print("--------------------------------------")

    def do_apply(self, inp):
        if isNumber(inp):
            inp= int(inp)
            if inp <= self.STATIC_RULES:
                rule= self.STATIC_RULES[inp]
            else:
                rules= "unknow"
        else:
            rule= formatRule(inp)
            tempRULES= sefl.STATIC_RULES.copy()
            tempRULES.append(rule)
            print("tempRULES: ", tempRULES)

    def do_set(self, inp):
        self.RULES= []
        tab= inp.split(" ")
        if len(tab) == 2:
            d.sqlModify("delete from links;")
            self.STACK= [tab[1]]
            if tab[0] == "exp":
                self.exp= tab[1]
            if tab[0] == "state":
                self.state= tab[1]

    def do_import(self, inp):
        try:
            importRules(inp)
            print("%s imported!" % inp)
        except:
            print("can't find the file '%s'" % inp)

    def do_end(self, inp):
        while(True):
            self.do_step("")
            if (self.ERROR == True and self.RULES == []) or isTerminal(self.exp):
                break

    def default(self, inp):
        print("action inconnue")

    def stackAppend(self, string):
       self.STACK.append(string)
       self.createLink()

    def createLink(self):
        goal= self.STACK.pop()
        subject= self.STACK.pop()
        d.sqlModify("insert into links(subject,link,goal) values ('%s','%s','%s')" % (subject, " ", goal))
        self.STACK.append(subject)
        self.STACK.append(goal)

    def stackPop(self):
        self.STACK.pop()
        self.STACK.pop()

MyPrompt().cmdloop()
