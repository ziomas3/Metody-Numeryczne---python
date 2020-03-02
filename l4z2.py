import scipy.optimize as sop

def sqrt5(x):
	if(x <= 0):
		return False
	return sop.newton(lambda a: a**5 - x, 1.)

print("sqrt5 z 23: ", sqrt5(23.))
print("sqrt5 z 3: ", sqrt5(3.))
