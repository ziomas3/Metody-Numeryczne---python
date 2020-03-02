import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import lagrange

dx=[0.,3.,6.]    
dy=[1.225,0.905,0.652]    
xw = np.arange(.0, 7., 0.05)
wiel = np.poly1d(lagrange(dx, dy)) 
plt.scatter(dx, dy)
plt.plot(xw, wiel(xw))
plt.plot(dx,dy)
plt.show()
