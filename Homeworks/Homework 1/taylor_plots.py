import math
import matplotlib.pyplot as plt
import numpy as np


def driver():

    x1 = math.pi
    x2 = 10**6

    delta = np.logspace(-16, 0, num=17)

    taylor1 = lambda x: -x * np.sin(x1) + ((x**2)/2)
    taylor2 = lambda x: -x * np.sin(x2) + ((x**2)/2)

    new1 = lambda x: -2 * np.sin((x / 2) + x1) * np.sin(x)
    new2 = lambda x: -2 * np.sin((x / 2) + x2) * np.sin(x)

    expr1 = new1(delta) - taylor1(delta)
    expr2 = new2(delta) - taylor2(delta)

    plt.plot(delta, expr2)
    plt.xscale('log')
    plt.xlabel('delta')
    plt.ylabel('y')
    plt.title('Difference between expressions at x = 10^6')
    plt.show()



driver()