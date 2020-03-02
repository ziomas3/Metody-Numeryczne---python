import matplotlib.pyplot as plt
import numpy as np
import scipy as sc

from scipy import linalg 

H=linalg.hilbert(4)
print('\n',H)
print(linalg.inv(H))
H2=linalg.hilbert(8)
print('\n',H2)
print(linalg.inv(H2))

x=[]
for n in range(5,20):
    x.append(linalg.det(linalg.hilbert(n)))
print(x)


a=range(len(x))
plt.semilogy(a,x)
plt.show()
