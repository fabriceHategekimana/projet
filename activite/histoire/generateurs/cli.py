from cmd import Cmd
from generator import *

class MyPrompt(Cmd):
    logo= ""+"|"
    prompt = logo+'number> '
    intro = "<!>Starting the server<!>"
    use_raw_input= False
    generator = "number"

    def do_exit(self, inp):
        return True

    def do_change(self, inp):
        gen= ["pays"]
        if inp in gen:
            self.prompt = self.logo+'%s> ' % inp
            self.generator= inp
        else:
            print("There is no generator with this name")
            print("Availiable generator: "+" ".join(gen))

    def default(self, inp):
        try:
            num= int(inp)
            for i in range(num):
                print(generate(self.generator))
        except:
            print(generate(self.generator))

MyPrompt().cmdloop()
