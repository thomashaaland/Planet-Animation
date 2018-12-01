import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class Planet:
    def __init__(self,
                 init_state = [[0,0],[0,0]],
                 m = 1.):
        self.init_state = np.asarray(init_state, dtype='float')
        self.m = m
        self.time_elapsed = 0
        self.state = self.init_state

    def position(self):
        # Gives the position of the specific planet
        x = self.state[0][0]
        y = self.state[0][1]
        return x, y
    def velocity(self):
        # Gives velocity of the planet
        vx = self.state[1][0]
        vy = self.state[1][1]
                 

    def mass(self):
        # Gives mass of the planet
        return self.m

    def force(self, X, M):
        # Use this to calculate the force between two planets
        G = 1
        r = np.array([X[0] - self.state[0][0], X[1] - self.state[0][1]])
        r_sq = np.dot(r,r)
        F = G * self.m * M / (r_sq) * r
        return F

    def step(self, F, dt):
        # use F to find changed position one stet at a time
        self.state[1] = self.state[1] + F * dt / self.m
        self.state[0] = self.state[0] + self.state[1]*dt
        self.time_elapsed += dt
                 

#---------------------------------------
# set up initial values and global variables
planetA = Planet(init_state = np.array([[0.,0.],[0.,0.]]), m = 2.)
planetB = Planet(init_state = np.array([[2.,0.],[0.,1]]), m = 0.0001)
planetC = Planet(init_state = np.array([[-1.,-1.],[0.,0.9]]), m = 0.0002)
dt = 1./30  # 30 fps

#--------------------------------------
# set up figure and animation
fig = plt.figure()
ax = fig.add_subplot(111, xlim=(-3,3), ylim=(-2,2),
                     aspect = 'equal', autoscale_on=False)
ax.grid()

lineA, = ax.plot([], [], 'o')
lineB, = ax.plot([], [], 'o')
lineC, = ax.plot([], [], 'o')

def init():
    # Initialize animation
    lineA.set_data([],[])
    lineB.set_data([],[])
    lineC.set_data([],[])
    return lineA, lineB

def animate(i):
    # Perform animation step
    global planetA, planetB, dt
    FA = planetA.force(planetB.position(), planetB.mass()) + planetA.force(planetC.position(), planetC.mass())
    FB = planetB.force(planetA.position(), planetA.mass()) + planetB.force(planetC.position(), planetC.mass())
    FC = planetC.force(planetA.position(), planetA.mass()) + planetC.force(planetB.position(), planetB.mass())
    planetA.step(FA, dt)
    planetB.step(FB, dt)
    planetC.step(FC, dt)
    
    lineA.set_data(planetA.position())
    lineB.set_data(planetB.position())
    lineC.set_data(planetC.position())
    return lineA, lineB, lineC
                   
# Choose the interval based on dt and the time to animate one step
from time import time
t0 = time()
animate(0)
t1 = time()
interval = 1000 * dt - (t1 - t0)

ani = animation.FuncAnimation(fig, animate, frames=300,
                              interval= interval, blit = True, init_func=init)

plt.show()
