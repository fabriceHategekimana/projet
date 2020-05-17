from options import *

"""
Cette classe concerne les decors (des parties de map ?)
Pour l'instant, ce sont juste des plateformes sans collision avec le joueur.
"""
class Background(pygame.sprite.Sprite):
    """ Initialisation d'un decor """
    def __init__(self, game, sprite, x, y, width, height):
        self.groups = game.textures
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.game = game
        self.sprite = sprite
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        self.image = pygame.image.load(sprite).convert()
        self.rect = pygame.Rect(x, y, width, height)
