import numpy as np
import matplotlib.pyplot as plt

def myPlot(x, y, text):
    plt.plot(x, y)
    plt.title(text, fontsize=20)
    plt.show()

def g(t, sigma=1):
    return (1/np.sqrt(2*np.pi*(sigma**2)))*np.exp(-(t**2)/(2*sigma**2))

def G(w, sigma= 1):
    return (np.sqrt(2)*np.pi/sigma) * g(w, 1/sigma)

def F(w):
    return (np.sin(w)/w)**2

def GF(w):
    return G(w)*F(w)

def a():
    x= np.linspace(-5,5,num=100)
    y= g(x)
    myPlot(x,y,"Gaussian g(t,sigma)")
    y= G(x)
    myPlot(x,y, "FT of Gaussian FT(g(t,sigma))")
    y= F(x)
    myPlot(x,y, "F(w)= sinc(w)^2")
    y= GF(x)
    myPlot(x,y, "G(w)*F(w)")

#---------------------------------------

def gabor(t, w0=10, sigma=1):
    return np.cos(w0*t)*g(t,sigma)

def Gabor(w, w0=10, sigma=1):
    return G(w-w0, 1/sigma)

def GaborF(w, w0=10, sigma=1):
    return Gabor(w,w0,sigma)*F(w)

def b():
    x= np.linspace(-5,5,num=100)
    y= gabor(x,)
    myPlot(x,y, "Gabor k(t)= cos(w_0t)*g(t,sigma)")
    y= Gabor(x)
    myPlot(x,y, "FT of Gabor FT(k(t))")
    y= F(x)
    myPlot(x,y, "F(w)= sinc(w)^2")
    y= GaborF(x)
    myPlot(x,y, "FT(k(t))*F(w)")

def delta(x):
    return np.zeros(len(x)) + (x == 0)

#unsharpened mask
def u(t, gamma=1.5, sigma=1):
    return (1+gamma)*delta(t) - gamma*G(t,sigma)

def U(w, gamma=1.5, sigma=1):
    return (1+gamma)-gamma*G(w,1/sigma)

def UF(w, gamma=1.5, sigma=1):
    return U(w,gamma,sigma)*F(w)

def c():
    x= np.linspace(-5,5,num=100)
    y= u(x)
    myPlot(x,y, "unsharp mask u(t)= (1+gamma)delta(t)-gamma g(t,sigma)")
    y= U(x)
    myPlot(x,y, "FT of unsharp FT(u(t))")
    y= F(x)
    myPlot(x,y, "F(w)= sinc(w)^2")
    y= UF(x)
    myPlot(x,y, "FT(u(t))*F(w)")

# 3 exercices => 3 function : a(), b() and c()

#a()
#b()
c()

