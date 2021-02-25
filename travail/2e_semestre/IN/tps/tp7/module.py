import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return np.power(x,2)

#prend une fonction f et une période T
def myScatter(f, T):
    x= np.linspace(-10,10,201)
    plt.scatter(x,f(x))
    plt.show()




