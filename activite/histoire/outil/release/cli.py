from cmd import Cmd
from mycompile import *

class MyPrompt(Cmd):
    prompt = 'normal> '
    intro = "<!>Starting the server<!>"
    use_raw_input= False
    mode = "normal"

    def do_exit(self, inp):
        return True

    def do_mode(self, inp):
            self.prompt = '%s> ' % inp
            self.mode= inp

    def default(self, inp):
        if self.mode == "normal":
            parser.parse(inp)
        elif self.mode == "debug":
            print(union(inp))
        elif self.mode == "sql":
            print(d.sqlQuery(inp))
        else:
            print("ce mode ne produit rien")

MyPrompt().cmdloop()
