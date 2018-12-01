# Inspired by tutorial from
# https://jakevdp.github.io/blog/2012/08/18/matplotlib-animation-tutorial

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure, axis and the plot elements to be animated

fig = plt.figure()
ax = plt.axes(xlim=(-2, 2), ylim=(-2,2))
line, = ax.plot([], [], 'o')

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,

# animation function, called sequentially
def animate(i):
    #x = np.linspace(0,2,1000)
    #y = np.sin(2 * np.pi * (x - 0.01 * i))
    omega = 2*2*np.pi/200.*30 # Degrees per second
    t = i / 30. # one second passes after 30 frames
    x = np.cos(omega * t)
    y = np.sin(omega * t)
    line.set_data(x,y)
    return line,

# call the animator. blit=True means only re-draw the parts that have changed
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=20, blit=True)

anim.save('basic_animation_circle.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()
