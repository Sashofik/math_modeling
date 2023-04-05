import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(1, 24, 1)
def function(s, t):    
   # dsdt  = (400**2)/(np.cos((np.pi*t)/12)+9)**2
   # dsdt = 2*k*(np.pi*s)**(1/2)*s*np.cos(np.pi*(t-12)/t)
    dsdt = k*k*2*np.pi/np.pi**(1/2)*s*s**(1/2)*np.cos(np.pi/12*(t-12))
  #  print(s)
    return dsdt

s_0 = 1600 #0
s_k = 2500 #12
k = 1.959

s_t = odeint(function, s_0, t)
plt.plot(t, s_t[:,0])
plt.xlabel('Время, часы')
plt.ylabel('Площадь')
plt.title('Кувшинка')
plt.savefig('d_2.png')