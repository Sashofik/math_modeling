import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

h = np.arange(1, 300, 1)

def function(v, h):
    dvdh =  (2 * y * R * v * (1 - R/h))*(1/2)
    return dvdh

v_0 = 0
R = 6377
y = 9.80665

v_h = odeint(function, v_0, h)

plt.plot(h, v_h[:,0])
plt.xlabel('Высота, метры')
plt.ylabel('Скорость')
plt.title('Метеорит')
plt.savefig('d_1.png')
#print(len(s_h))
#print(s_t[len(-1)])