from module_rules import *

def evaluateProgram(state, prog):
    tab= prog.split(";;")
    for inst in tab:
        state= evaluateInstruction(state+inst)
    print("return>", state)

#EVALUATION DU PROGRAMME
importRules("data/factorielle.fa")
prog= "estPair(15)"
state=""
evaluateProgram(state, prog)
