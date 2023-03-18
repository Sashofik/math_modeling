import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Пределы изменения переменной величины
# В данной задаче переменной величиной является время
t = np.arange(0, 48, 48)

# Запись диф. уравнения в виде функции
def radio_function(m, t):
    dmdt = h * m
    return dmdt

# Определение начальных условий и параметров
m_0 = 1000
h = 0.08  # Постоянная распада для Висмута 210

# Решение дифференциального уравнения функцией odeint
m_t = odeint(radio_function, m_0, t)

# Построение решения в виде графика функции
plt.plot(t, m_t[:,0], label='Распад Висмута 210')
plt.xlabel('Период распада, секунды')
plt.ylabel('Функция распада')
plt.title('Радиоактивный распад')
plt.savefig('o00000.1.png')