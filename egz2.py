
from scipy.integrate import fixed_quad
import numpy as np
def f(x):
    return (np.sin(x)**3)/x

for i in range (2,20,2):
    it3=fixed_quad(f,-1,1,n=i)[0]
    print("%4d  %18.15f" %(i,it3))