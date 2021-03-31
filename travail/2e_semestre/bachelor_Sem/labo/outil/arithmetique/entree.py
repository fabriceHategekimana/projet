from arithmetique.Acompile import *

def subEval(exp):
    exp= str(exp)
    print("expression à subEval: ", exp)
    parser.parse(exp, debug=False)
    f = open("subEval.txt", "r")
    res= f.readline()
    f.close()
    return res
