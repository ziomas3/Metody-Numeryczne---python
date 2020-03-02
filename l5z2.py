import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.misc import derivative

x=np.array([1,1.25,1.5,1.75,2.,2.25,2.5,2.75,3.])
y=np.array([-0.5403,-0.0104,0.9423,0.17445,1.3073,-0.7718,-2.4986,-0.7903,2.7334])

cubspli=CubicSpline(x,y) #interpoluje 

pierwiastki=cubspli.roots(-2,5)
for a in pierwiastki:
    print("%12.8f %12.8e" %(a,cubspli(a)))

print('\n'," dla x=2.1 f'(x)= ",(derivative(cubspli,2.1)))
plt.plot(x,y,'x')
plt.plot(np.arange(0.8, 3.1, 0.05),cubspli(np.arange(0.8, 3.1, 0.05)),'-')
plt.show()
