import numpy as np
from module import *

def f_of_t(t):
    return np.sin(t+(np.pi/4))

def a():
    text= "Sampling f(t)=sin(t+pi/4) with T="
    t= np.linspace(-10, 10, num=201)
    y1= f_of_t(t)*sha(t,1)
    y2= f_of_t(t)*sha(t,0.5)
    y3= f_of_t(t)*sha(t,2)
    myScatter(t,y1, text+str(1))
    myScatter(t,y2, text+str(0.5))
    myScatter(t,y3, text+str(2))

def d():
    t= np.linspace(-10, 10, num=201)
    ft= f_of_t(t)
    e= Even(f_of_t, t)
    o= Odd(f_of_t, t)
    eo= Even(f_of_t, t)+Odd(f_of_t, t)

    plt.plot(ft)
    plt.plot(e)
    plt.legend(["f(t)", "Even[f(t)]"])
    plt.show()

    plt.plot(ft)
    plt.plot(o)
    plt.legend(["f(t)", "Odd[f(t)]"])
    plt.show()

    plt.plot(ft)
    plt.plot(eo)
    plt.legend(["f(t)", "Even[f(t)]+Odd[f(t)]"])
    plt.show()

d()
