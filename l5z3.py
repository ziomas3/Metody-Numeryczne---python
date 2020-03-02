from scipy.interpolate import CubicSpline
import numpy as np
import matplotlib.pyplot as plt
import math

xs=np.array([ 0.2, 2., 20., 200., 2000., 20000.],dtype=float) 
ys=np.array([103., 13.9, 2.72, 0.8, 0.401, 0.433],dtype=float)          

xlog = []
ylog = []
for i in xs:
    xlog.append(math.log10(i))

for j in ys:
    ylog.append(math.log10(j))

xw = np.arange(-1, 5,0.1)   
f = CubicSpline(xlog, ylog)
plt.plot(xlog, ylog,'o',xw,f(xw),'-')

plt.show()

