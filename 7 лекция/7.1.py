import matplotlib.pyplot as plt
import numpy as np

t = np.arange(-2*np.pi, 2*np.pi, 0.1)
R = 6

x = R * (t - np.sin(t))
y = R * (1 - np.cos(t))

plt.plot(x, y, ls='--', lw=3)

plt.axis('equal')

R = 4
x = R * np.sin(t)
y = R * np.cos(t)

plt.plot(x, y, ls='--', lw=3)

plt.axis('equal')

plt.savefig('7.1.png')