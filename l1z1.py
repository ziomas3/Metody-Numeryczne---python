import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 1.5,0.001)
y = np.cos(x)-3*np.sin(np.tan(x)-1)

plt.grid(True)
plt.plot(x,y)

plt.show()
