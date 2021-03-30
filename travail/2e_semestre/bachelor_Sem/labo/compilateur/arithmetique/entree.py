from compile import *

def subeval(exp):
    parser.parse(exp, debug=False)
    f = open("res.txt", "r")
    res= f.readline()
    f.close()
    return res


print(subeval("[]"))
#print(subeval("concat([1,2,3],4)"))
