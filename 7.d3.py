import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
zvezda, = plt.plot([], [], color='orange')


edge = 60
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
                                      # X = x * np.cos(t) - x * np.cos(t)
#x = np.arange(-25, 25, 0.1)                                            # Y = y * np.sin(t) + y * np.sin(t)
#y = np.arange(-25, 25, 0.1)   

def move(t):
    x = 12 * np.cos(t) + 8 * np.cos(1.5 * t)
    y = 12 * np.sin(t) - 8 * np.sin(1.5 * t)
    return x, y


def animate(i):
    plt.grid(True)
    t = np.arange(0, 4*np.pi, 0.1)  
    x = 12 * np.cos(t) + 8 * np.cos(1.5 * t)
    y = 12 * np.sin(t) - 8 * np.sin(1.5 * t)
    X = x * np.cos(i) - y * np.sin(i)
    Y = y * np.cos(i) + x * np.sin(i)
    zvezda.set_data(X, Y)

ani = animation.FuncAnimation(fig, animate, frames=np.arange(0, 2*np.pi, 0.1), interval=200)

ani.save('7.d3.gif')    