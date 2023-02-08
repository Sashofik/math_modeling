import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Пределы изменения переменной величины
# В данной задаче переменной величиной является время
t = np.arange(0, 10**6, 100)

# Запись диф. уравнения в виде функции
def bact(n, t):
    dndt = k * n
    k = n/dndt
    return dndt

# Определение начальных условий и параметров
n_0 = 10

n_t = odeint(bact, n_0, t)

plt.plot(t, n_t[:,0], label='Рост бактерий')
plt.xlabel('Время, секунды')
plt.ylabel('Функция роста')
plt.title('Рост бактерий')
plt.legend()


plt.savefig('o.1.png')