import numpy as np
import matplotlib.pyplot as plt

def myPlot(x, y, text):
    plt.plot(x, y)
    plt.title(text, fontsize=20)
    plt.show()

def extendInterval(x, start, end):
    delta= np.max(x)-np.min(x)
    nb_point= len(x)
    step= delta/(nb_point-1)
    new_delta= end-start
    new_nb_point= int((new_delta/step)+1)
    return np.linspace(start, end, num= new_nb_point)

def diracComb(f, T, t, k=5):
    l= np.linspace(-k, k, k*2)
    val= np.max(t)+(k*T)
    n_t= extendInterval(t,-val,val)
    res= np.zeros(len(n_t))
    for i in l:
        res += f(n_t-(i*T))
    return n_t, res

def h(t):
    a= (np.abs(t) <= 1)
    return  a-(a*np.abs(t))

def a():
    x= np.linspace(-5,5,num=101)
    for T in [1,1.5,2,4]:
        myPlot(x,h(x-T), "h(x) with T=%d" % (T))
        n_x,y= diracComb(h,T,x)
        myPlot(n_x,y, "h(x)*diracComb with T=%d" % (T))

a()
