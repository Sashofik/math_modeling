import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(1, 1440, 1)print(t)

def function(s, t):
   # dsdt  = (400**2)/(np.cos((np.pi*t)/12)+9)**2
    dsdt = 2*sp*(np.pi*s)**(1/2)*s*np.cos(np.pi*(t-12)/t)
    print(t)
    return dsdt

s_0 = 1600 #0
s_k = 2500 #12
sp = 1.959

s_t = odeint(function, s_0, t)
plt.plot(t, s_t[:,0])
plt.xlabel('Время, минуты')
plt.ylabel('Площадь')
plt.title('Кувшинка')
plt.savefig('d_2.png')
