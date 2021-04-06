from cmd import Cmd
from compile import *
import re

class MyPrompt(Cmd):
    prompt = '>'
    use_raw_input= False

    def do_exit(self, inp):
        return True

    def default(self, inp):
        parser.parse(inp,debug=False)
        #parser.parse(inp)
        f = open("subEval.txt", "r")
        for line in f:
            print(line)


MyPrompt().cmdloop()
