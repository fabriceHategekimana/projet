from cmd import Cmd
from mycompile import *

class MyPrompt(Cmd):
    prompt = 'log> '
    intro = "<!>Starting the server<!>"
    use_raw_input= False

    def do_exit(self, inp):
        return True

    def default(self, inp):
        parser.parse(inp)

MyPrompt().cmdloop()
