import numpy as np
import matplotlib.pyplot as plt

def myPlot(x, y, text):
    plt.plot(x, y)
    plt.title(text, fontsize=20)
    plt.show()

def myPlot2(y, text):
    plt.plot(y)
    plt.title(text, fontsize=20)
    plt.show()

def mySubplot1(num, x, y, text):
    plt.subplot(num)
    plt.plot(y)
    plt.title(text, fontsize=20)

def mySubplot2(num, y, text):
    plt.subplot(num)
    plt.plot(y)
    plt.title(text, fontsize=20)

def a():
    #f= np.array([1,2,4,8])
    f= np.array([1,2,1,2])
    #FFT
    print(np.fft.fft(f))

def fourierDefinition(F):
    #real part
    Fr= np.real(F)
    mySubplot2(221, Fr, "plot of F real part")
    #imaginary part
    Fi= np.imag(F)
    mySubplot2(222, Fi, "plot of F imaginary part")
    #magnitude
    Fm= np.sqrt((Fr**2)*(Fi**2))
    mySubplot2(223, Fm, "plot of F magnitude")
    #phase
    Fp= np.arctan(Fi/Fr)
    mySubplot2(224, Fp, "plot of F phase")
    plt.show()

def b():
    #part1
    t= np.linspace(-2,2,num=101)
    f= np.exp(-10*(t**2))
    #part2
    myPlot(t, f, "plot of f according t")
    myPlot2(f, "plot of f without t (from 0 to 200)")
    #part3
    f_sym= np.roll(f,51)
    myPlot2(f_sym, "plot of f_sym")
    #part4
    F= np.fft.fft(f_sym)
    myPlot2(f_sym, "plot of F")
    #part5
    fourierDefinition(F)
    #part6
    F= np.fft.fftshift(F)
    fourierDefinition(F)


#a()
b()
