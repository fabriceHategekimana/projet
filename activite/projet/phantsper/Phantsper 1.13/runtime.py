from options import *

"""
Cette classe concerne le temps de jeu apres spawn du joueur (pas le temps de jeu tout court)
"""
class Runtime:
    def __init__(self):
        """ Initialisation du temps """
        self.timestart = 0 # ne devrait etre appele qu'une fois
        self.timeend = 0
        self.duration = 0
        self.timeplayed()

    def timeplayed(self):
        """ Update le temps """
        #sera update
        self.timeend = time.time()
        self.duration = self.timeend - self.timestart

    def afficher_temps(self):
        """ Affichage du temps, enlever le # et le pass pour activer """ 
        #print(self.duration)
        pass
