import matplotlib.pyplot as plt
import numpy as np

#prend une fonction f et une période T
def myScatter(f, T):
    x= np.linspace(-10,10,201)
    plt.scatter(x,f(x))
    plt.show()

def sha(t, T):
    val= 0
    if t == 0 or T%t == 0:
        val = 1
    return val

def odd(f, n):
    return (f(n)-f(-n))/2

def even(f, n):
    return (f(n)+f(-n))/2


