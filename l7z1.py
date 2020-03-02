from scipy.integrate import solve_ivp
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def f(t, y):
    return np.sin(t*y)


y0 = [2]
y1 = [2.5]
y2 = [3]
y3 = [3.5]

wynik0 = solve_ivp(f, [0, 6], y0,max_step=0.01)
print('t=', wynik0.t)
print('y=', wynik0.y[0])


plt.plot(wynik0.t,wynik0.y[0])
plt.xlabel('czas')
plt.ylabel('sin(t)')
plt.show()
