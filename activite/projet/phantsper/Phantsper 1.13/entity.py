from options import *

class Entity(): # entity herite de la classe Sprite de pygame
    def __init__(self, window, mode, x, y, walkspeed, jumpspeed, HP):
        """ Initialisation de l'entite """

        self.window = window
        self.mode = mode
        self.x = x # position x ou apparait l'entite
        self.y = y # position y ou apparait l'entite
        self.walkspeed = walkspeed # vitesse de l'entite lorsqu'elle marche
        self.jumpspeed = jumpspeed # vitesse de l'entite quand elle saute
        self.HP = HP
 
        # self.standing = sprite[0]
        # self.moveRight = sprite[1]
        # self.moveLeft = sprite[2]

        self.image = pygame.Surface((77, 100))
        self.rect = self.image.get_rect()

        self.hitbox = (self.x - self.rect.width / 2, self.y - self.rect.width / 2, self.rect.width, self.rect.height) # tuple (liste non modifiable)

        self.vx = 0
        self.vy = 0

        self.falling = True

    def set_move(self):
        if (self.mode == GameInfo.Platformer) and self.falling:
            self.vy += g * uTime * uDist
            self.y += self.vy * uTime

        self.x += self.vx * uTime
        self.y += self.vy * uTime

        self.x_center = self.x + self.rect.width / 2
        self.y_center = self.y + self.rect.height / 2

    def jump(self):
        self.falling = True
        self.vy = -self.jumpspeed * uDist

    def update_hitbox(self):
         """ Update la hitbox """
         self.hitbox = (self.x, self.y, self.rect.width, self.rect.height)
         # position then width and height

    def draw(self):
        """ Dessine l'entite """

        # joueur
        # if self.walkCount + 1 >= 24:
         #  self.walkCount = 0
        # if self.isMoveRight:    
          #  self.window.blit(self.moveRight[self.walkCount // 3], (self.x, self.y))
            # self.walkCount += 1
       # elif self.isMoveLeft:
          #  self.window.blit(self.moveLeft[self.walkCount // 3], (self.x, self.y))
          #  self.walkCount += 1
        #else:
           # self.window.blit(self.standing, (self.x, self.y))

        # dessiner la hitbox selon la collision

        if self.colliding:
            pygame.draw.rect(self.window, BLUE, self.hitbox, 0)
        else:
            pygame.draw.rect(self.window, GREEN, self.hitbox, 0)
