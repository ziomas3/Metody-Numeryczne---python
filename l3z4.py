import numpy as np
import scipy as sc
from scipy import linalg 
A=np.array([[1,0,0,0,0],[1,1,1,1,1],[1,3,9,27,81],[1,5,25,125,625],[1,6,36,216,1296]])
b=np.array([-1,1,3,2,-2])
print(linalg.solve(A, b))