import numpy as np
from scipy.special import roots_legendre

def f(x):
	return np.log(x)/(x**2-2*x+2)
D_2 = 0.
D_4 = 0.
xi2, ai2 = roots_legendre(2)
xi4, ai4 = roots_legendre(4)

for i in range(len(ai2)):
	D_2 += (np.pi - 1.)/2.*ai2[i]*f((np.pi+1.)/2. + (np.pi - 1.)/2.*xi2[i])
for i in range(len(ai4)):
	D_4 += (np.pi - 1.)/2.*ai4[i]*f((np.pi+1.)/2. + (np.pi - 1.)/2.*xi4[i])

print("2 węzłów: " + str(D_2))
print("4 węzłów: " + str(D_4))