import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
toch, = plt.plot([], [], color='red')
toch1, = plt.plot([], [], color='blue')
ball, = plt.plot([], [], color='black')

t = np.arange(-2*np.pi, 2*np.pi, 0.1)
R = 6
R1 = 4
x, y = [], []
x1, y1 = [], []

edge = 40
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def move(R, t):
    x = R * (t - np.sin(t))
    y = R * (1 - np.cos(t))
    return x-37.5, y

def move1(R1, t):
    x1 = R1 * np.sin(t)
    y1 = R1 * np.cos(t)
    return x1, y1    

def circle_move(R, t, vx = 4.6):
    x0 = vx * t
    y0 = 5
    alpha = np.arange(0, 2*np.pi, 0.1)
    x = x0 + R*np.cos(alpha)
    y = y0 + R*np.sin(alpha)
    return x-32.5, y

def animate(i):
    xs = R * (t - np.sin(t))
    ys = R * (1 - np.cos(t))
    plt.plot(xs, ys, ls='--', lw=3, color = 'green')
    xs1 = R1 * np.sin(t)
    ys1 = R1 * np.cos(t)
    plt.plot(xs1, ys1, ls='--', lw=3, color = 'green')

    x.append(move(R, t = i)[0])
    y.append(move(R, t = i)[1])
    toch.set_data(x, y)
    x1.append(move1(R1, t = i)[0])
    y1.append(move1(R1, t = i)[1])
    toch1.set_data(x1, y1)
    ball.set_data(circle_move(R=6.5, t = i))
    #ctrelka.set_data(ctrelka_move(R=12.5, t = i))
	

ani = animation.FuncAnimation(fig, animate, frames=np.arange(0, 4*np.pi, 0.6), interval=600)

ani.save('7.d1.gif')


