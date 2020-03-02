import scipy.optimize as sop
import numpy as np
import matplotlib.pyplot as plt

def f(x):
	return -2*np.sin(x)+3*np.cos(np.tan(x)-3)

x = np.arange(0., 1.5, 0.01)

plt.plot(x, f(x))
plt.grid(True)
plt.show()

zero = []
zero.append(sop.ridder(f, 1.0, 1.2))    
zero.append(sop.ridder(f, 1.2, 1.4))
zero.append(sop.ridder(f, 1.44, 1.46)) 
zero.append(sop.ridder(f, 1.46, 1.48)) 

print("Miejsca zerowe funkcji: ")

for i in zero:
	print(i)
