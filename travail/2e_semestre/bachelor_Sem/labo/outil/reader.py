from module_rules import *

importRules("data/compteur.fa")
exp= "<25>plus"
print(evaluateInstruction(exp))
