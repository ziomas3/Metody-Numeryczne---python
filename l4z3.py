import scipy.optimize as sop
import math

def f(t):
	return 2510.*math.log(2.8e6/(2.8e6 - 13.3e3*t)) - 9.81*t - 335.

print(sop.newton(f, 1.))
