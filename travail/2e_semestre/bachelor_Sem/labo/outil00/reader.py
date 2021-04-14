from module_rules import *

importRules("data/factorielle.fa")
rules= getRules()
exp= "fact(1)"
evaluateInstruction(exp,rules)
