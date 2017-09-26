"""
Animated experimental evidence of
Central limit theorem
"""
import random
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()


def random_generator(min=0, max=1):
    return lambda : random.uniform(min, max)
    #return lambda: random.expovariate(2. / max)


MIN, MAX, BIN = 0, 100, 0.01
NUM_TRIALS = 8000

x = np.arange(MIN, MAX, BIN)

def generate_y(num_distributions, generator=random_generator()):
    i = 0
    y = np.zeros(shape=x.shape)
    while i < NUM_TRIALS:
        i += 1
        value = 0
        for _ in range(num_distributions):
            value += generator()
        idx = np.searchsorted(x, value)
        if idx >= y.shape[0]:
            idx = -1
        y[idx] += 1
    return y

line, = ax.plot(x, generate_y(1))


def animate(i):
    line.set_ydata(generate_y(i))
    return line,


def init():
    line.set_ydata(np.ma.array(x, mask=True))
    ax.set_ylim(0, 20)
    return line,

ani = animation.FuncAnimation(fig, animate, np.arange(1, 100), init_func=init,
                              interval=1, blit=True)

plt.show()
