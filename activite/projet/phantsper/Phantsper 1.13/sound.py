from options import *

"""
Cette classe permet de gérer la musique du jeu et le sons spéciaux
"""

def playMusic(music, volume):
    source= "sound/background/"
    music = pygame.mixer.music.load(source+music)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(-1) #-1 veut dire que la music se répétera en boucle

def playFX(fx, volume):
    source= "sound/fx/"	
    son = pygame.mixer.Sound(source+fx)
    son.set_volume(volume)
    son.play()
	
