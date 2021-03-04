import numpy as np
from module import *

def a():
    t= np.linspace(-10, 10, num=201)
    y1= sha(t,1)
    y2= sha(t,0.5)
    y3= sha(t,2)
    myScatter(t,y1)
    myScatter(t,y2)
    myScatter(t,y3)

