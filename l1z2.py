import matplotlib.pyplot as plt
import numpy as np

x=[0.1]
for y in range(0,100):
    x.append(3.5*x[y]*(1-x[y]))
plt.grid(True)
a=range(len(x))
plt.scatter(a,x)

plt.show()
