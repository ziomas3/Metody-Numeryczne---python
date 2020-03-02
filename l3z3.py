import numpy as np
import scipy as sc
from scipy import linalg 
A=np.array([[0,0,2,1,2],[0,1,0,2,-1],[1,2,0,-2,0],[0,0,0,-1,1],[0,1,-1,1,-1]])
b=np.array([1,1,-4,-2,-1])
print(linalg.solve(A, b))