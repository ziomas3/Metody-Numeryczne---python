from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt


def f(t, y, A):
    return [y[1],-y[1]/2-np.sin(y[0])+A*np.cos(t*2./3.)]
tmax=10
t1=np.arange(0.0,tmax,0.01)
y1=[0.01,0]
t2=np.arange(0.0,tmax,0.3)
y2=[0.3,0]
t3=np.arange(0.0,tmax,0.3)
y3=[0.3,0]
w1=solve_ivp(lambda t,y:f(t,y,0.5),[0,tmax],y1,method='Radau',t_eval=t1)
w2=solve_ivp(lambda t,y:f(t,y,0.5),[0,tmax],y2,method='Radau',t_eval=t2)
w3=solve_ivp(lambda t,y:f(t,y,1.35),[0,tmax],y3,method='Radau',t_eval=t3)
plt.plot(w1.t,w1.y[0])

plt.plot(w2.t,w2.y[0])

plt.plot(w3.t,w3.y[0])
plt.show()

plt.plot(w1.y[0],w1.y[1])

plt.plot(w2.y[0],w2.y[1])

plt.plot(w3.y[0],w3.y[1])
plt.show()