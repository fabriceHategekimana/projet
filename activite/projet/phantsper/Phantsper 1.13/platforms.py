from options import *

"""
Cette classe concerne les plateformes (les murs si on est en mode RPG)
"""
class Platform(pygame.sprite.Sprite):
    """ Initialisation d'une plateforme """
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