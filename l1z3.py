import matplotlib.pyplot as plt
import numpy as np
import scipy as sc

A=np.array([[4,-2,1],[-2,4,-2],[1,-2,4]])
B=np.array([[4,2,0],[2,5,2],[0,2,4]])
W=np.array([1,-2,3],dtype=float)
print('\n',A)
print('\n',B)
print('\n',W)
print('\n',A*B)
print('\n',A*W)
print('\n',B*(A*W))
from scipy import linalg 
print ('\n',linalg.det(A))
print ('\n',linalg.det(B))
print(linalg.inv(A))
print(linalg.inv(B))
