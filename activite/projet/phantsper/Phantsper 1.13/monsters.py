from runtime import *
from entity import *
from options import *

class Monsters(Entity): # Monsters hérite de Entity
    def __init__(self, window, x, y, walkspeed, jumpspeed, HP, sprite):
       Entity.__init__(self, window, x, y, walkspeed, jumpspeed, HP, sprite)
       self.runtime = Runtime() # on définit le chrono ici
       self.walkCount= 0 
       self.isMoveRight= False
       self.isMoveLeft= False

       #Pour savoir la distance entre la position de départ
       self.x_init=self.x
       #print(self.x_init)
       self.y_init=self.y

       self.max_dist=200

       #pour la direction
       self.direction = 1 #pour aller à droite
   
    def move(self):
        """ Mouvements du monstres, vu que c'est un bot, le joueur ne va pas
            le contrôler"""

        #test pour la direction
        if (self.x-self.x_init)==0: #bouge à droite
            #print(self.x_init)
            self.direction = 1
            self.isMoveRight=True
            self.isMoveLeft= False

            self.jump()

        #print(self.x) 
        if (self.x-self.x_init)>=self.max_dist: #bouge à gauche
            self.direction = -1
            self.isMoveLeft=True
            self.isMoveRight=False

            self.jump()
        
        #disons qu'il part à droite au tout début et qu'il ne bouge pas en y pour l'instant
        self.vx = self.direction * self.walkspeed * uDist
        
        self.x += self.vx * uTime
        self.y += self.vy * uTime

    def detect_player(self, player, radius):#on devrait rajouté un paramètre quel type de monstres etc.
        """the monster detects the player within a radius, using geometry"""
        self.player=player
        #center of the monster ?
        #à modifier plus tard car cela dépend de l'hitbox des monstres et de la taille de l'image
        #ici l'image fait 77x100
        self.x_center=self.x+38.5 #77/2, on va travailler avec des réels ?
        self.y_center=self.y+50

        self.radius=radius

        #juste des maths ^^
        if (abs(self.x_center-self.player.x_center)**2 + abs(self.y_center-self.player.y_center)**2)**(1/2) <= self.radius:
            print("DETECT")
        else:
            print("no")

    def draw(self):
        Entity.draw(self)

        pygame.draw.circle(self.window, MAGENTA, (int(self.x_center),int(self.y_center)), RADIUS, 2)
