
import pygame

class GameInfo: # il s'agit d'un enum, un peu comme dans C
    RPG = 1
    Platformer = 2

""" FENETRE """

TITLE = "Phantsper"
WIDTH = 1000
HEIGHT = 600
WINDOW = (WIDTH, HEIGHT)

""" JEU """

FPS = 60

""" PHYSIQUE """

g = 9.80665

""" IMAGES """

SPRITESHEET = 'img/spritesheet.png'
TEXTURE = "img/walls.png"
BACKGROUND = "img/floor.png"

""" COULEURS """

TRANSPARENT = (0, 0, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (128, 128, 128)