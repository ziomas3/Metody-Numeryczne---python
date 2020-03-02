import scipy.optimize as sop
import numpy as np
import matplotlib.pyplot as plt

def f(x):
	return 2*x**4+24*x**3+61*x**2-16*x+1

x = np.arange(-10., 2.5, 0.01)

plt.plot(x, f(x))
plt.grid(True)
plt.show()

zero = []
zero.append(sop.ridder(f, -9., -7.))
zero.append(sop.ridder(f, -5., -3.5))
#zero.append(sop.ridder(f, -1., 1.)) 

print("Miejsca zerowe funkcji: ")

for i in zero:
	print(i)
