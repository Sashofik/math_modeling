import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
#r = α · t
fig, ax = plt.subplots()
circle, = plt.plot([], [], 'o', color='g', label='circle')

def circle_move(R):
    alpha = np.arange(0, 2*np.pi, 0.1)
    x = R*np.cos(alpha)
    y = R*np.sin(alpha)
    return x, y

edge = 150
def animate(R):
    circle.set_data(circle_move(R)) 

ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
    
ani = animation.FuncAnimation(fig, animate, frames=100, interval=30)

ani.save('7.2.gif')