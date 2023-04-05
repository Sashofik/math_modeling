import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

h = np.arange(0, 6377, 1)
#h = np.flip(h, axis=None)
#print(h)

def function(v, h):
    dvdh  = (C-m*g/R)**(1/2)
   # print(v)
    return dvdh

v_0 = 0
C = 299792458 
R = 6377
g = 9.80665
m = 3000

v_h = odeint(function, v_0, h)
print(v_h)
plt.plot(h, v_h[:,0])
plt.xlabel('Высота, метры')
plt.ylabel('Скорость')
plt.title('Метеорит')
plt.savefig('d_1.png')