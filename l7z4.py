import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from scipy.optimize import newton

def rownanie(t, y):
    return [y[1], -1.-np.sin(y[0])]

def fun_strzelajaca(u):
    solucja = solve_ivp(rownanie, [0., np.pi], [0., u])
    return solucja.y[0, -1] #bierzemy to, co dał ostatni krok obliczen

#wyrysowuję by wiedzieć, gdzie celować w miejsce zerowe
uki = np.linspace(-5., 5., 50, endpoint=True)
plt.plot(uki, np.vectorize(fun_strzelajaca)(uki))
plt.show()
u_nasze = newton(fun_strzelajaca, 3.)

rozw = solve_ivp(rownanie, [0., np.pi], [0., u_nasze], max_step=0.1)
plt.plot(rozw.t, rozw.y[0])
plt.show()