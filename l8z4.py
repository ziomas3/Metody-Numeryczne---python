import numpy as np
from scipy.sparse import diags
from scipy.sparse.linalg import eigsh
import matplotlib.pyplot as plt

print("Dla m=100")
h100 = 0.092
g100 = -.5/h100**2 * np.ones(98)
d100 = np.fromfunction(lambda i:1/h100**2+0.5*(-4.6+(i+1)*h100)**2+.2*(-4.6+(i+1)*h100)**4 ,(99,),dtype=float)
data=[d100.tolist(),g100.tolist(),g100.tolist()]
positions=[0,1,-1]
Hm100=diags(data,positions,(98,98)).tocsc()
eH100,vH100=eigsh(Hm100,k=4,sigma=0.0,which='LM')

print("4 pierwsze wartości własne:")
print(eH100) #wygladają sensownie

iksow100 = np.arange(h100-4.6,4.6-h100,h100)

for i in range(4):
    unormowanie = 1/np.sqrt(h100*(vH100[:,i]**2)).sum()
    plt.plot(iksow100, unormowanie*vH100[:, i])
    plt.show()

print("A teraz dla m=1000")
h1000 = 0.0092
g1000 = -.5/h1000**2 * np.ones(998)
d1000 = np.fromfunction(lambda i:1/h1000**2+0.5*(-4.6+(i+1)*h1000)**2+.2*(-4.6+(i+1)*h1000)**4 ,(999,),dtype=float)
data=[d1000.tolist(),g1000.tolist(),g1000.tolist()]
positions=[0,1,-1]
Hm1000=diags(data,positions,(998,998)).tocsc()
eH1000,vH1000=eigsh(Hm1000,k=4,sigma=0.0,which='LM')

print("4 pierwsze wartości własne:")
print(eH1000) #także wyglądają sensownie, choć widać różnice na 2 miejscu po przecinku

iksow1000 = np.arange(h1000-4.6,4.6-h1000,h1000)

for i in range(4):
    unormowanie = 1/np.sqrt(h1000*(vH1000[:,i]**2)).sum()
    plt.plot(iksow1000, unormowanie*vH1000[:, i])
    plt.show()