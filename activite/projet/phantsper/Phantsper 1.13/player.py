from options import *

"""
Cette classe concerne specifiquement le joueur (mouvements, animations, etc.)
"""
class Player(pygame.sprite.Sprite):
    """ Initialisation du joueur """
    def __init__(self, game, x, y, walkspeed, jumpspeed, HP, score):
        self.groups = game.sprites
        pygame.sprite.Sprite.__init__(self, self.groups) # on utilise la classe sprite.Sprite de pygame

        self.game = game
        self.x = x
        self.y = y
        self.walkspeed = walkspeed
        self.jumpspeed = jumpspeed
        self.HP = HP
        self.score = score

        self.mode = GameInfo.RPG # on intialise le joueur en mode RPG (pas de gravite, pas de sauts)
        self.falling = True

        self.load_images()
        self.frame = 0
        self.last_time = 0
        self.image = self.game.spritesheet.get_image(0, 0, 73, 164)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

        self.vx = 0
        self.vy = 0

    """ On load tous les sprites dans la Spritesheet """
    def load_images(self):
        self.walk_frames_r = [self.game.spritesheet.get_image(0, 0, 73, 164),
                            self.game.spritesheet.get_image(145, 0, 72, 165),
                            self.game.spritesheet.get_image(73, 165, 73, 166),
                            self.game.spritesheet.get_image(0, 331, 75, 166),
                            self.game.spritesheet.get_image(75, 331, 80, 166),
                            self.game.spritesheet.get_image(146, 165, 75, 166),
                            self.game.spritesheet.get_image(0, 165, 73, 166),
                            self.game.spritesheet.get_image(73, 0, 72, 165)] # ces frames sont les animations du joueur vers la DROITE

        self.walk_frames_l = [] # on inverse simplement toutes les frames selon l'axe (Oy) pour les animations du joueur vers la GAUCHE
        for frame in self.walk_frames_r:
            frame.set_colorkey(BLACK)
            self.walk_frames_l.append(pygame.transform.flip(frame, True, False))

    """ Pour obtenir toutes les touches qui sont actuellement pressees """
    def get_keys(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            self.vx = -self.walkspeed * self.game.ddist
        
        if keys[pygame.K_RIGHT]:
            self.vx = self.walkspeed * self.game.ddist

        if not(keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]):
            self.vx = 0

        if self.mode == GameInfo.Platformer: # si le jeu est en mode platformer, le joueur peut sauter avec la touche espace
            if keys[pygame.K_SPACE] and not(self.falling):
                self.jump()
        else: # sinon, le joueur peut aller en haut ou en bas si il le souhaite
            if keys[pygame.K_UP]:
                self.vy = -self.walkspeed * self.game.ddist
        
            if keys[pygame.K_DOWN]:
                self.vy = self.walkspeed * self.game.ddist
        
            if not(keys[pygame.K_UP] or keys[pygame.K_DOWN]):
                self.vy = 0

    """ Sauter (en mode platformer) """
    def jump(self):
        self.falling = True
        self.vy = -self.jumpspeed * self.game.ddist

    """ Update le joueur """
    def update(self):
        self.update_position()
        self.update_hitbox()
        # self.update_score()
        self.animate()

    """ Update la position """
    def update_position(self):
        if (self.mode == GameInfo.Platformer) and self.falling:
            self.vy += g * self.game.dtime * self.game.ddist
            self.y += self.vy * self.game.dtime

        self.x += self.vx * self.game.dtime
        self.y += self.vy * self.game.dtime

        if self.vx != 0 or self.vy != 0:
            self.walking = True
        else:
            self.walking = False

    """ Update la hitbox """
    def update_hitbox(self):
         self.rect = pygame.Rect(self.x, self.y, self.rect.width, self.rect.height)

    """ Update le score """
    def update_score(self):
        # Le score sanity diminue en fonction du temps (fonction affine)
        if self.score >= 0:
            self.score += slope * self.runtime.duration
        else:
            self.score = 0

    """ Animation du joueur (changement de frames...) """
    def animate(self):
        time = pygame.time.get_ticks()

        if self.walking:
            if time - self.last_time > 120: # on change de frame toutes les 120ms
                self.last_time = time
                
                self.frame = (self.frame + 1) % len(self.walk_frames_l)
                if self.vx >= 0:
                    self.image = self.walk_frames_r[self.frame]
                else:
                    self.image = self.walk_frames_l[self.frame]
