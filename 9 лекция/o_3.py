import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 48, 1)

def function(v, t):

    dvdt =  a - ((y*v**2)/m)
    return dvdt

v_0 = 0
y = 0.44
a = 2
m = 5

v_t = odeint(function, v_0, t)

plt.plot(t, v_t[:,0])
plt.xlabel('Время, минуты')
plt.ylabel('Скорость')
plt.title('Движение точки')
plt.savefig('o_3.png')