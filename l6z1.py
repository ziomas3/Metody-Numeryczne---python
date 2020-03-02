from scipy.misc import derivative	
import numpy as np
x=0.2
h=0.1
def f(x):
    return np.log(np.tanh(x/(x**2+1)))
for i in range(9):
    h/=10
    np1_5=derivative(f, x, dx=h,n=1,order=5)
    np2_5=derivative(f, x, dx=h,n=2,order=5)
    np3_5=derivative(f, x, dx=h,n=3,order=5)
    print("h=%7.1e   %16.12f %16.12f %16.12f " %(h,np1_5,np2_5,np3_5))
#f'=5 f''=3  f'''=4
