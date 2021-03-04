import matplotlib.pyplot as plt
import numpy as np

#prend une fonction f et une période T
def myScatter(x, y):
    plt.scatter(x, y)
    plt.show()

def sha(t, T):
    changeIfPeriodic= lambda x: 1 if (x == 0 or x%T == 0) else 0
    val = np.array(list(map(changeIfPeriodic, t)))
    return val

def odd(f, n):
    return (f(n)-f(-n))/2

def even(f, n):
    return (f(n)+f(-n))/2


