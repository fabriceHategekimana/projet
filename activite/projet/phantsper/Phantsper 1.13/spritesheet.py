from options import *

"""
Cette classe concerne la spritesheet (cad une image contenant tous les sprites, en gros elle selectionne juste le sprite qu'elle a besoin)
"""
class Spritesheet:
    """ Initialisation de la spritesheet """
    def __init__(self, filename):
        self.spritesheet = pygame.image.load(filename).convert()

    """ Pour selectionner uniquement la partie dont on a besoin """
    def get_image(self, x, y, width, height):
        image = pygame.Surface((width, height))
        image.blit(self.spritesheet, (0, 0), (x, y, width, height))

        return image
