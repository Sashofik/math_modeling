import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Пределы изменения переменной величины
# В данной задаче переменной величиной является время
t = np.arange(0, 10**6, 100)

# Запись диф. уравнения в виде функции
def radio_function(m, t):
    dmdt =  k * m *t

    # t = m/k*m
    return dmdt

# Определение начальных условий и параметров
m_0 = 10
k = 10 

# Решение дифференциального уравнения функцией odeint
m_t = odeint(radio_function, m_0, t)

# Построение решения в виде графика функции
plt.plot(t, m_t[:,0], label='Рост бактерий')
plt.xlabel('Время, секунды')
plt.ylabel('Функция роста')
plt.title('Рост бактерий')
plt.legend()

plt.savefig('o.1.png')