import scipy.optimize as sop
import numpy as np
import matplotlib.pyplot as plt

def y(x):
    return np.tan(x) - 1

def f(x):
    return np.cos(x) - 3*np.sin(y(x))

dx = 0.001
x = np.arange(0., 1.5, dx)


zerowe = []
for i in x:
    if(np.sign(f(i)) != np.sign(f(i + dx))):
        temp = sop.ridder(f, i, i + dx)
        zerowe.append([temp, y(temp)])

print(zerowe)
plt.plot(x, f(x))
plt.grid(True)
plt.show()
