from scipy.interpolate import interp1d
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange

dx=np.array([ 1.0, 2.5, 3.5, 4.0, 1.1, 1.8, 2.2, 3.7],dtype=float) 
dy=np.array([6.008,15.722, 27.13, 33.772,5.257, 9.549, 11.098, 28.828],dtype=float)  
xw = np.arange(1.0, 4.2)


plt.subplot(2,1,1)
f=interp1d(dx, dy,kind='linear')
plt.plot(dx, dy,'o')
plt.plot(xw, f(xw))



plt.subplot(2,1,2)
f2=interp1d(dx, dy,kind='quadratic')
plt.plot(dx, dy,'o')
plt.plot(xw, f2(xw))
plt.show()
