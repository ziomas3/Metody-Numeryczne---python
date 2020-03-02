from scipy.interpolate import interp1d
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange

dx=np.array([ 0.2, 2., 20., 200., 2000., 20000.],dtype=float) 
dy=np.array([103., 13.9, 2.72, 0.8, 0.401, 0.433],dtype=float)

xw = np.arange(0.2, 20000.1)

wiel = np.poly1d(lagrange(dx, dy)) #tworzy  wielomian fituje lagrangem
plt.plot(xw, wiel(xw),'-',dx, dy,'o')
plt.show()
