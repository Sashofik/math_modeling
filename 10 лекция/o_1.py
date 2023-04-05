import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
x = np.arange(-5, 5, 0.01)

def diff_func(k, x): 
    y, z = k
	
    dydx = y**2*z 

    dzdx = z/x-y*z**2
    return dydx, dzdx

y0 = 1
z0 = -3
k0 = y0, z0

s = odeint(diff_func, k0, x)

plt.plot(x, sol[:, 1], 'b')
plt.savefig('o_1.png')