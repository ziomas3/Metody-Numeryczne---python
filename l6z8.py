import numpy as np
from scipy.integrate import dblquad

def fxy(x,y):
    return np.sin(np.pi*x)*np.sin(np.pi*(y-x))

def hx(x):
    return x
wdxy=dblquad(fxy,0,1,0,hx)
print(wdxy)