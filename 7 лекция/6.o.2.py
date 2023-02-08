# Создать функцию, строящую графики кривых второго порядка, заданных явно:
# Парабола
# Гипербола
# на вход, функции подаются: пределы изменения переменной (xa, xb), количество точек N, на которое разбиваются соответствующие пределы, необходимые параметры a, b, c, … и название графика.
# x**2/a**2 - y**2/b**2 = 1
# c = sqrt(a**2+b**2)
import matplotlib.pyplot as plt
import numpy as np

def gip(a, b, c, naz, xa, xb, N):
  if naz == 'Гипербола':
    x = np.linspace(xa, xb, N)
    y = np.sqrt(((x**2)*(b**2))/a**2-b**2)
    plt.title('Гипербола')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.plot(x, y)
    plt.show()
  else:
    return
xa = int(input('Введите пределы x (Начало): '))
xb = int(input('Введите пределы x (Конец): '))
N = int(input('Введите кол-во точек: '))
a = np.random.sample(N)
b = np.random.sample(N)
c = np.sqrt(a**2+b**2)
# naz = str(input('Введите название:'))
naz = 'Гипербола'
gip(a, b, c, naz, xa, xb, N)