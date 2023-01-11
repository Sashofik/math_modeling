import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
sinu1, = plt.plot([], [], color='red')
sinu2, = plt.plot([], [], color='red')
tochki, = plt.plot([], [], color='black')

edge = 60
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

F = 0.5
A = 12
x, y = [], []
mas1x, mas1y = [], []

class Tochk(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

def toch(x, y):
    for i in range(x):
        mas1x.append(i)
    for i in range(y):
        mas1y.append(i)
    return mas1x, mas1y

def move1(f, t, a):
    x = f * t
    y = a * np.sin(f * t)
    return x-45, y


def animate(i):
    plt.grid(True)
    x.append(move1(f = F, t = i, a = A)[0])
    y.append(move1(f = F, t = i, a = A)[1])
    sinu1.set_data(x, y)
    toch(x = x, y = y)

ani = animation.FuncAnimation(fig, animate, frames=45, interval=200)

ani.save('7.d2.gif')    