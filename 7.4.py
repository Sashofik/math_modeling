import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
frac, = plt.plot([], [], 'o', color='purple')

x0 = 0.1
y0 = 0.1
C = 0.3
D = 0.33
frames = 100

xn = x0**2 - y0**2 + C
yn = 2*x0 * y0 + D

x = []
y = []


for i in range(100):
    
    x.append(xn)
    y.append(yn)
    

    xn = xn1
    yn = yn1


plt.axis('equal')
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)

def animate(i):
    frac.set_data(x[:i], y[:i])
    
ani = animation.FuncAnimation(fig, animate, frames=frames, interval=30)

ani.save('7.4.gif')
