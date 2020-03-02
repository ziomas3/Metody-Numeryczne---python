import numpy as np
from scipy.misc import derivative
from scipy.interpolate import lagrange
x = [-2.2, -.3, .8, 1.9]
y = [-15.8, 10.962, 1.92, -2.04]
f = lagrange(x, y)
print("f'(0) = %12.10f \t f''(0) = %12.10f" %(derivative(f, 0.), derivative(f, 0., n=2)))