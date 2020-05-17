from entity import *
from options import *

class Item(Entity):
    def __init__(self, window, x, y, sprite):
       Entity.__init__(self, window, x, y, 0, 0, 0, sprite) # une lanterne qui drop ne bouge pas XD
       self.walkCount = 0
       self.isMoveRight = False
       self.isMoveLeft = False