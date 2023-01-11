import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
edge = 3
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)


planet, = plt.plot([], [], 'o', color='green')

#class Planet(object):
#    def __init__(self, R, angle_vel, sp):
#        self.R = R
#        self.angle_vel = angle_vel
#        self.sp = sp
#
   # def new_planet(self):
   #     self, = plt.plot([], [], 'o', color='green')
   #     return self
   # def planet_move(self, t):
   #     alpha = self.angle_vel * (np.pi/180) * t + self.sp
   #     x = self.R*np.cos(alpha)
   #     y = self.R*np.sin(alpha)
   #     return x, y

for i in range(1):
    globals()['planet' + str(i) + ','] = plt.plot([], [], 'o', color='green')
  #  globals()['planet' + str(i)] = Planet(R=2, angle_vel = 2, sp = ((180/52) * i))

def planet_move(R, angle_vel, t):
       alpha = angle_vel * (np.pi/180) * t #+ sp    sp = ((180/52) * i),
       x = R*np.cos(alpha)
       y = R*np.sin(alpha)
       return x, y

def animate(i):
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    for j in range(1):
        exec("planet{}.set_data(planet_move(R=2, angle_vel = 2, t = i))".format(j))
ani = animation.FuncAnimation(fig, animate, frames=45, interval=10)
ani.save('project.gif')