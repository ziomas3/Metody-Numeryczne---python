import numpy as np 
from scipy.linalg import eigh_tridiagonal

A=np.array([[1,0,0,1],[2,2,1,0],[0,2,3,0],[2,-5,0,2]])
w1,v1=eigh_tridiagonal(A)
print("wartości")
print(w1)
