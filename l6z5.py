import numpy as np
from scipy.integrate import simps
def podcalk(teta, teta0):
	return np.power(1.-np.power(np.sin(teta0/2),2.)*np.sin(teta),-0.5)
x = np.linspace(0., np.pi/2, num=7, endpoint=True) 

punkty15 = podcalk(x, 15*np.pi/360)
punkty30 = podcalk(x, 30*np.pi/360)
punkty45 = podcalk(x, 45*np.pi/360)

h15 = simps(punkty15, x=x)
h30 = simps(punkty30, x=x)
h45 = simps(punkty45, x=x)

print("15 stopni: %.8f\th0: %.8f" %(h15, h15*2/np.pi))
print("30 stopni: %.8f\th0: %.8f" %(h30, h30*2/np.pi))
print("45 stopni: %.8f\th0: %.8f" %(h45, h45*2/np.pi))
