import random
import numpy as np
import matplotlib.pyplot as plt

"""L'avantage de ce type de réseau est que le nombre d'erreur de retransmission diminu graduellement quand on augmente le nombre de transmission"""

class Automate():

    def __init__(self, probabilite):
        self.etat=0
        self.probabilite= probabilite

    def transmission(self):
        val= random.random()
        if val < self.probabilite:
            self.etat += 1
        else:
            self.etat = 0

    def getEtat(self):
        return self.etat

proba = 0.9
a= Automate(proba)
transmission= 800

data= []
i= 0
while i < transmission:
    a.transmission()
    data.append(a.getEtat())
    i += 1

h = np.hstack(data)
plt.hist(h)
plt.show()
