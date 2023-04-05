import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t = np.arange(-5, 5, 0.01)

def diff_func(z, t):
    y, m = z

    dydt = m
    dmdt = np.sin(x)+np.cos(x)
    return dydt, dmdt

y0 = 3
m0 = 0

x = 120

z0 = y0, m0

s = odeint(diff_func, z0, t)

plt.plot(t, s[:, 1], 'b')
plt.savefig('o_3.png')