import matplotlib.pyplot as plt
import scipy.optimize as optimize
import numpy as np

# data
F1=np.array([0.1, 1., 10., 100., 1000.],dtype=float) #x
t1=np.array([100.5, 10.5, 1.5, 0.6, 0.51],dtype=float) 

plt.plot(t1, F1, 'ro', label="original data")

# curvefit

def func(t, a, b):
    return a + b * np.log(t)

popt, pcov = optimize.curve_fit(func, t1, F1, maxfev=1000000)
t = np.linspace(1, 3600 * 24 * 28, 13)
plt.plot(t, func(t, *popt), label="Fitted Curve")
plt.legend(loc='upper left')
plt.show()