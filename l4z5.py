import scipy.optimize as sop
import numpy as np
import math

g=9.81
#(10/(x[0]*math.cos(x[1])))-tf

#x[0]*math.cos(x[1])+(x[0]*math.sin(x[1])-g*tf)
#x[0]*math.sin(x[1])*tf-g*math.pow(tf,2)/2+3
def fun(x):
	return [x[0]*math.cos(x[1])+(x[0]*math.sin(x[1])-g*(10./(x[0]*math.cos(x[1])))),x[0]*math.sin(x[1])*(10./(x[0]*math.cos(x[1])))-g*math.pow((10./(x[0]*math.cos(x[1]))),2)/2.+3.]
wynik=sop.fsolve(fun,[10.,1.])
print(wynik)
print(math.degrees(wynik[1]))
print(fun(wynik))
