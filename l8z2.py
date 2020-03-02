from scipy import linalg
from scipy.linalg import eigh
import numpy as np 

H=linalg.hilbert(6)
print("wartosci")
h1,v1=eigh(H)
print(h1)

print("wektory")
print(v1)