from options import *
from runtime import *
from spritesheet import *
from camera import *
from player import *
from platforms import *
from background import *
from sound import *
from dialogBox import *

"""La classe Game est la main principale qui execute le jeu.
Les options (taille de la fenetre, nombre de FPS...) sont importees et peuvent etre modifiees depuis 'options.py'.
"""
class Game:
    """ Initialisation du jeu """
    def __init__(self):
        pygame.init()
        pygame.mixer.init() # mixer est utilise pour les sons / musiques

        self.window = pygame.display.set_mode(WINDOW) # nouvelle fenetre
        pygame.display.set_caption(TITLE)

        self.clock = pygame.time.Clock() # nouveau timer
        # self.runtime = Runtime() a fixer
        playMusic("grotte.wav", 0.5)

    """ Load les images / donnees du jeu """
    def load_data(self):
        self.spritesheet = Spritesheet(SPRITESHEET)

    """ Commence un nouveau jeu """
    def new(self):
        self.sprites = pygame.sprite.LayeredUpdates() # group sprite de pygame (mieux ?)
        self.textures = pygame.sprite.Group() # group sprite de pygame

        self.background = Background(self, BACKGROUND, 0, 0, 1000, 600) # init un simple decor

        self.platforms = [] # init des plateformes
        self.platforms.append(Platform(self, TEXTURE, 0, 300, 250, 300))
        self.platforms.append(Platform(self, TEXTURE, 500, 250, 300, 60))
        self.platforms.append(Platform(self, TEXTURE, 300, 500, 300, 60))
        self.platforms.append(Platform(self, TEXTURE, 0, 0, 1000, 30))

        self.player = Player(self, 150, 50, 5, 5, 100, 100) # 100 HP puis 100 sanity score
        self.camera = Camera(self.window) # camera

        self.ddist = 62.5

        # self.runtime.timestart = time.time()
        self.run()

    """ Methode principale """
    def run(self):
        self.running = True
        while self.running:
            self.dtime = self.clock.tick(FPS) / 1000
            self.events()

            # JOUEUR 
            self.player.get_keys()
            self.player.update()
            self.check_collisions(self.player)

            if self.player.mode == GameInfo.RPG:
                self.draw_text('Mode RPG', WIDTH / 2, 10, 'arial', 32, WHITE)
                self.draw_dialog('Et nous maintienne à dedans. Il lui faut une majorité exeptionnelle pour pouvoir réussire dans son entreprise. Il y aura donc un second référundum et on attend de voir comment cela va se passer. La tension est à son comble!')
            else:
                self.draw_text('Mode Platformer', WIDTH / 2, 10, 'arial', 32, WHITE)
            self.update() 
            self.draw()

    """ Simple procedure qui s'execute lorsqu'on veut quitter le jeu """
    def quit(self):
        pygame.quit()

    """ Nouvel event / action. Le joueur veut fermer la fenetre ? Attaque d'un monstre ? """
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.running:
                    self.running = False
                    self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.running:
                        self.running = False
                        self.quit()
                if event.key == pygame.K_x:
                    playFX('os04.wav', 0.5);
                    if self.player.mode == GameInfo.Platformer:
                        self.player.mode = GameInfo.RPG
                    else:
                        self.player.mode = GameInfo.Platformer

    """ Pour verifier une collision entre joueur / plateforme """
    def check_collisions(self, entity):
        self.entity = entity
        self.entity.colliding = False

        for platform in self.platforms:  
            colliding_x = (self.entity.rect[0] + self.entity.rect[2] >= platform.rect[0]) and (self.entity.rect[0] <= platform.rect[0] + platform.rect[2])
            colliding_y = (self.entity.rect[1] + self.entity.rect[3] >= platform.rect[1]) and (self.entity.rect[1] <= platform.rect[1] + platform.rect[3])
            
            if (colliding_x and colliding_y):
               self.entity.colliding = True
               self.collide(self.entity, platform)
           
        if not(self.entity.colliding):
            self.entity.falling = True

    """ Repondre en cas de collision (cad empecher le joueur d'aller dans la plateforme) """
    def collide(self, entity, platform):
        t_collision = entity.rect[1] + entity.rect[3] - platform.rect[1]
        b_collision = platform.rect[1] + platform.rect[3] - entity.rect[1]
        l_collision = entity.rect[0] + entity.rect[2] - platform.rect[0]
        r_collision = platform.rect[0] + platform.rect[2] - entity.rect[0]

        if (t_collision < b_collision and t_collision < l_collision and t_collision < r_collision): # Collision depuis le haut
            entity.falling = False
            entity.vy = 0
            entity.y = platform.rect[1] - entity.rect[3]

        if (b_collision < t_collision and b_collision < l_collision and b_collision < r_collision): # Collision depuis le bas
            entity.y = platform.rect[1] + platform.rect[3]
            
        if (l_collision < r_collision and l_collision < t_collision and l_collision < b_collision): # Collision depuis la gauche
            entity.vx = 0
            entity.x = platform.rect[0] - entity.rect[2]

        if (r_collision < l_collision and r_collision < t_collision and r_collision < b_collision): # Collision depuis la droite
            entity.vx = 0
            entity.x = platform.rect[0] + platform.rect[2]

    """ Dessiner la fenetre, puis les textures, puis les sprites """
    def draw(self):
        self.window.fill(GRAY) # tout l'arriere plan est en gris

        for texture in self.textures: # dessiner toutes les textures
            self.window.blit(texture.image, self.camera.apply(texture), texture)

        for sprite in self.sprites: # dessiner tous les sprites
            self.window.blit(sprite.image, self.camera.apply(sprite))

    """ Update les graphismes mais surtout la camera (qui est centree sur le joueur) """
    def update(self):
        self.camera.update(self.player)
        pygame.display.update()

    """ Simple methode pour ecrire du texte """
    def draw_text(self, text, x, y, font, size, color):
        font = pygame.font.Font(pygame.font.match_font(font), size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)

        self.window.blit(text_surface, text_rect)

    """ Simple methode pour ecrire du texte dans une boite de dialogue """
    def draw_dialog(self, text):
        drawDialog(self.window, text) #fonction importé de dialogBox

    

game = Game() # appelle directement __init__() (c'est a dire le constructeur)
game.load_data() # on load toutes les donnees
game.new() # on cree une nouvelle partie
