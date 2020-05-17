from options import *

"""
Cette classe concerne specifiquement la camera (update tous les sprites selon leur position relative, on essaye de garder toujours le joueur au milieu)
"""
class Camera:
    """ Initialisation de la camera """
    def __init__(self, window):
        self.camera = pygame.Rect(0, 0, 0, 0)

    """ Application d'un rect sur la camera """
    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    """ Update la camera """
    def update(self, target):
        x = int(WIDTH / 2) - target.rect.centerx
        y = int(HEIGHT / 2) - target.rect.centery

        self.camera = pygame.Rect(x, y, self.camera.width, self.camera.height)