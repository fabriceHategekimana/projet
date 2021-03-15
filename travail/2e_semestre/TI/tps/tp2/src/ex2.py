import numpy as np
import matplotlib.pyplot as plt

mean= np.array([0,0])
cov= np.array([[1, 0.8], [0.8, 1]])

Sigma= [0.1, 0.5, 1.2, 10]

X= np.random.multivariate_normal(mean, cov)

for s in  Sigma:
    points= np.array([[0], [0]])
    for i in  range(1000):
        covNoise= np.array([[s, 0.8], [0.8, s]])
        Z= np.random.multivariate_normal(mean, covNoise)
        Y= np.array([X+Z])
        points= np.concatenate((points, Y.T), axis=1)
    plt.scatter(points[0], points[1])
    plt.show()

