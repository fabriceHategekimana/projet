import numpy as np

def c():
    f = np.array([1,2,3,4])
    g = np.array([1,-1])
    print(np.convolve(f, g))
    #circular with no padding
    f_circ= np.tile(f,3)
    print(np.convolve(f_circ,g)[4:9])
    #circular with zero padding
    f_circ2= np.array([0]+list(f)+[0])
    print(np.convolve(f_circ2,g)[1:-1])



c()
