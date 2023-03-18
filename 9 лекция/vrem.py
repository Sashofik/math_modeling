import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Пределы изменения переменной величины
# В данной задаче переменной величиной является время
t = np.arange(0, 100, 1)

# Запись диф. уравнения в виде функции
def function(n, t):
    dndt =  k * n
    return dndt

# Определение начальных условий и параметров
n_0 = 2
k = 1/30

# Решение дифференциального уравнения функцией odeint
n_t = odeint(function, n_0, t)

# Построение решения в виде графика функции
plt.plot(t, n_t[:,0], label='Рост бактерий')
plt.xlabel('Время, секунды')
plt.ylabel('Функция роста')
plt.title('Рост бактерий')
plt.legend()

for i in range(len(n_t)):
    if n_t

plt.savefig('o.1.png')