import numpy as np
from module import *

def f_of_t(t):
    return np.sin(t+(np.pi/4))

def a():
    t= np.linspace(-10, 10, num=201)
    y1= f_of_t(t)*sha(t,1)
    y2= f_of_t(t)*sha(t,0.5)
    y3= f_of_t(t)*sha(t,2)
    myScatter(t,y1)
    myScatter(t,y2)
    myScatter(t,y3)

def d():
    t= np.linspace(-10, 10, num=201)
    ft= f_of_t(t)
    e= Even(f_of_t, t)
    o= Odd(f_of_t, t)
    eo= Even(f_of_t, t)+Odd(f_of_t, t)
    plt.plot(ft)
    plt.show()
    plt.plot(e)
    plt.show()
    plt.plot(o)
    plt.show()
    plt.plot(eo)
    plt.show()

d()
