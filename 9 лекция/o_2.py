import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 48, 1)

def function(i, t):
    didt =  -k * i * t
    return didt

i_0 = 1000
k = 0.08

i_t = odeint(function, i_0, t)

plt.plot(t, i_t[:,0], label='Инвестиции')
plt.xlabel('Время, месяцы')
plt.ylabel('деньги')
plt.title('Инвестиции')
plt.legend()
plt.savefig('o_2.png')

sum = 0
for i in range(len(i_t)):
    sum += float(i_t[i])
print(sum)

