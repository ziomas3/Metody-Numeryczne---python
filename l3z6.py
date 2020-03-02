import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import scipy as sc
from scipy import linalg 
from numpy import linalg as linalg2

H5=linalg.hilbert(5)
H10=linalg.hilbert(10)
H20=linalg.hilbert(20)
print ('\nnorma(H5)=',linalg.norm(H5,np.inf))
print ('k(H5)=',linalg2.cond(H5,np.inf))

print ('\nnorma(H10)=',linalg.norm(H10,np.inf))
print ('k(H10)=',linalg2.cond(H10,np.inf))

print ('\nnorma(H220)=',linalg.norm(H20,np.inf))
print ('k(H20)=',linalg2.cond(H20,np.inf))
