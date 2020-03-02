from scipy.interpolate import interp1d
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange

dx=np.array([ 0, 1.525, 3.05, 4.575, 6.1, 7.625, 9.150],dtype=float) #h
dy=np.array([1., 0.8617, 0.7385, 0.6292, 0.5328, 0.4481, 0.3741],dtype=float)   #ro 

xw = np.arange(.0, 12.2, 0.001)

aw_1 = np.polyfit(dx, dy, 2)

paw_1=np.poly1d(aw_1)
plt.plot(dx, dy,'o')
plt.plot(xw, paw_1(xw))
plt.legend(['dane', 'aproks.'], loc='best')
plt.show()

print(paw_1(10.5))