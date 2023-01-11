import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
sinu1, = plt.plot([], [], color='red')
sinu2, = plt.plot([], [], color='red')


edge = 40
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

F = 6
A = 4
x, y = [], []

def move1(f, t, a):
    x = t
    y = a * np.sin(f · t)
    return x, y


def animate(i):
    x.append(move1(F, t = i, a = A)[0])
    y.append(move1(F, t = i, a = A)[1])
    sinu1.set_data(x, y)

ani = animation.FuncAnimation(fig, animate, frames=np.arange(0, 4*np.pi, 0.6), interval=600)

ani.save('7.d2.gif')    