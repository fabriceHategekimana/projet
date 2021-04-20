from module_rules import *

def evaluateProgram(state, prog):
    tab= prog.split(";;")
    for inst in tab:
        state= evaluateInstruction(state+inst)
    print("return>", state)

#EVALUATION DU PROGRAMME
importRules("data/position.fa")
prog= "droite;;droite;;haut"
state="<0,0>"
evaluateProgram(state, prog)
