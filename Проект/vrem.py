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

F = 16
A = 22
x, y = [], []

def move1(f, t, a):
    x = a * np.cos(f * t)
    y = a * np.sin(f * t)
    return x, y


def animate(i):
    plt.grid(True)
    x.append(move1(F, t = i, a = A)[0])
    y.append(move1(F, t = i, a = A)[1])
    sinu1.set_data(x, y)

ani = animation.FuncAnimation(fig, animate, frames=180, interval=500)

ani.save('vrem.gif')    