from module import *

def f_of_z(z):
    return np.power(z, 3)-1

x = np.linspace(-2, 2, num=100, dtype=complex)
y = np.linspace(-2, 2, num=100, dtype=complex)
xv, yv = np.meshgrid(x, y)
z= xv + (yv*1j)
w= f_of_z(z)

#d
m= np.abs(w)
plt.imshow(m, cmap='hsv')
plt.colorbar()
plt.title("visualize |w|", fontsize=20)
plt.show()

#e
m= np.log(1+np.abs(w))
plt.imshow(m, extent=(-30,70,100,0), cmap='hsv')
plt.colorbar()
plt.title("visualize m= log(1+|w|)", fontsize=20)
plt.show()

#f
plt.imshow(w.real, extent=(-30,70,100,0), cmap='hsv')
plt.colorbar()
plt.title("visualize real part", fontsize=20)
plt.show()

plt.imshow(w.imag, extent=(-30,70,100,0), cmap='hsv')
plt.colorbar()
plt.title("visualize imaginery part", fontsize=20)
plt.show()

#h
plt.imshow(np.angle(w), extent=(-30,70,100,0), cmap='hsv')
plt.colorbar()
plt.title("visualize angle", fontsize=20)
plt.show()

