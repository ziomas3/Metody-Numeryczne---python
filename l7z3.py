import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def rownanko(t, x, oporek):
	modulik = np.sqrt(x[2]**2+x[3]**2)
	return [x[2], x[3], -oporek*x[2]*modulik, -oporek*x[3]*modulik - 9.81]

def hyc_o_podloge(t, x): #zarzuciłem używanie tego, gdyż przez to wcale nic nie całkowało
	return x[1] #gdy spadnie pod grunt

hyc_o_podloge.terminal = True

bezoporu1 = solve_ivp(lambda t, x: rownanko(t, x, 0.), [0., 20.], [0.,0.,5.,10.],max_step=.01)
bezoporu2 = solve_ivp(lambda t, x: rownanko(t, x, 0.), [0., 20.], [0.,0.,10.,10.],max_step=.01)
bezoporu3 = solve_ivp(lambda t, x: rownanko(t, x, 0.), [0., 20.], [0.,0.,10.,5.],max_step=.01)

plt.plot(bezoporu1.y[0], bezoporu1.y[1])
plt.plot(bezoporu2.y[0], bezoporu2.y[1])
plt.plot(bezoporu3.y[0], bezoporu3.y[1]) #wielkość piłki tu nie ma znaczenia
plt.ylim([0,10])
plt.xlim([0,24])
plt.show()

prawie_opor = .35*1.2/2.
zoporem_imasa1ipole1 = solve_ivp(lambda t, x: rownanko(t, x, prawie_opor), [0., 20.], [0.,0.,10,10.],max_step=.01)
zoporem_imasa2ipole1 = solve_ivp(lambda t, x: rownanko(t, x, prawie_opor/2), [0., 20.], [0.,0.,10.,10.],max_step=.01)
zoporem_imasa1ipole2 = solve_ivp(lambda t, x: rownanko(t, x, prawie_opor*2), [0., 20.], [0.,0.,10.,10],max_step=.01)
zoporem_imasa2ipole1ipredkoscipoczatkoweinne = solve_ivp(lambda t, x: rownanko(t, x, prawie_opor/2), [0., 20.], [0.,0.,10.,5.],max_step=.01)

plt.plot(zoporem_imasa1ipole1.t, zoporem_imasa1ipole1.y[1])
plt.plot(zoporem_imasa2ipole1.t, zoporem_imasa2ipole1.y[1])
plt.plot(zoporem_imasa1ipole2.t, zoporem_imasa1ipole2.y[1])
plt.plot(zoporem_imasa2ipole1ipredkoscipoczatkoweinne.t, zoporem_imasa2ipole1ipredkoscipoczatkoweinne.y[0])
plt.ylim([0,10])
plt.xlim([0,24])
plt.show()
