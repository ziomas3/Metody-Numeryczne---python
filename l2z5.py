import math
x=[1,1]
print(1,x[1])
from scipy.integrate import quad
def fpodcalk(x,n):
    return x**n*math.exp(x)

for n in range(2, 21):
    x.append(math.exp(1)-n*x[n-1])
    print(n,x[n],quad(fpodcalk,0,1,args=(n)))
