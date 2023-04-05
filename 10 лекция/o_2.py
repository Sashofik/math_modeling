import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t = np.arange(-1, 1, 0.01)

def diff_func(z, t):
    x, y = z

    dxdt = 3*x-2*y+((np.e**(3*t))/(np.e**t+1))
    dydt = x-((np.e**(3*t))/np.e**t+1)
    return dxdt, dydt

x0 = 5
y0 = -7
z0 = x0, y0

s = odeint(diff_func, z0, t)

plt.plot(t, sol[:, 1], 'b')
plt.savefig('o_2.png')