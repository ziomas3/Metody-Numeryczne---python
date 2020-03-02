import numpy as np
from scipy.misc import derivative as deri
from scipy.interpolate import lagrange
from scipy.interpolate import interp1d
xi=np.array([0.0,0.1,0.2,0.3,0.4])
yi=np.array([0.0,0.078348,0.13891, 0.192916, 0.244981])
intp = lagrange(xi, yi)
kubik = interp1d(xi, yi, kind='cubic')
lagr=deri(intp, 0.2, dx=0.2, order=5)
kubi=deri(kubik, 0.2, dx=0.01, order=5)
cent=(yi[0] -8*yi[1] + 8*yi[3] - yi[4])/1.2
print("lagranż:\t%12.10f \ncubic spline:\t%12.10f \ncentralna:\t%12.10f" %(lagr,kubi,cent))