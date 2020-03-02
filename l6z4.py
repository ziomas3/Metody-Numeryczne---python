import numpy as np
from scipy.integrate import simps
def f(x):
	return np.cos(2*np.arccos(x))
x3 = np.linspace(-1., 1., num=3, endpoint=True)
x5 = np.linspace(-1., 1., num=5, endpoint=True)
x7 = np.linspace(-1., 1., num=7, endpoint=True)
y3 = f(x3)
y5 = f(x5)
y7 = f(x7)
print("3 węzły:\t " + str(simps(y3, x=x3)))
print("5 węzłów:\t " + str(simps(y5, x=x5)))
print("7 węzłów:\t " + str(simps(y7, x=x7)))