import numpy as np
import matplotlib.pyplot as plt


def f_tild(t):
    if (t + 1) % 4 < 2:
        return 1
    else:
        return -1


def a(k):
    if isinstance(k, int):
        if k % 2 == 1:
            return (-1) ** ((k - 1) * 4 / (2 * k * np.pi))
        else:
            return 0
    elif type(k) is np.ndarray:
        kk = k[k % 2 == 1]
        val = np.zeros(k.shape)
        val[k % 2 == 1] = (-1)**((kk-1)*4 / (2*kk*np.pi))
        return val


def fN(t, N):
    k = np.arange(0, N + 1)
    #if isinstance(t, (int, float)):
    return 1/2 * a(0) + np.sum(a(k) * np.cos(k*(np.pi/2)*t))
    #elif type(t) is np.ndarray:
        #return 1/2 * a(0) + (np.sum(a(k) * np.cos(k*(np.pi/2)*t)))


def display(t, f_tild, fN, title):
    plt.plot(t, f_tild, alpha=0.5)
    plt.plot(t, fN, alpha=0.5)
    plt.title(title)
    plt.show()

t = np.linspace(-5, 5, num=100)

tild_vect = np.vectorize(f_tild)
f_square = tild_vect(t)

fN_vect = np.vectorize(fN)
fN0 = fN_vect(t, 0)
fN1 = fN_vect(t, 1)
fN3 = fN_vect(t, 3)
fN5 = fN_vect(t, 5)
fN10 = fN_vect(t, 10)
fN100 = fN_vect(t, 100)

display(t, f_square, fN0, 'N = 0')
display(t, f_square, fN1, 'N = 1')
display(t, f_square, fN3, 'N = 3')
display(t, f_square, fN5, 'N = 5')
display(t, f_square, fN10, 'N = 10')
display(t, f_square, fN100, 'N = 100')


