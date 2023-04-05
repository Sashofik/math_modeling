import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t = np.arange(-5, 5, 0.01)

def diff_func(z, t):
    y, m = z

    dydt = m
    dmdt = -4*m-5*y
    return dydt, dmdt

y0 = 4
m0 = -1

z0 = y0, m0

s = odeint(diff_func, z0, t)

plt.plot(t, s[:, 1], 'b')
plt.savefig('o_4.png')