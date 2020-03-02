import scipy.optimize as sop
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return [x[0] + np.exp(-x[0]) + x[1]**3, x[0]**2 + 2*x[0]*x[1] - x[1]**2 + np.tan(x[0])]
wyniki = []
wynikx = []
wyniky = []
x=np.arange(-2., 2.1, 0.3)
for i in x:
    for j in x:
        sol = sop.root(f, [i, j])
        if(sol.x[0]**2 + sol.x[1]**2 < 4):
            wyniki.append([sol.x[0], sol.x[1]])
            wynikx.append(sol.x[0])
            wyniky.append(sol.x[1])

print(wyniki)
plt.scatter(wynikx,wyniky)
plt.grid(True)
plt.show()
for x in wyniki:
	if (f(x)[0]>0 or f(x)[1]>0):
		
		print (x,f(x))
