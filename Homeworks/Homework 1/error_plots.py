import math
import matplotlib.pyplot as plt
import numpy as np


def driver():

    x1 = math.pi
    x2 = 10**6

    delta = np.logspace(-16, 0, num=17)

    orig1 = lambda x: np.cos(x1 + x) - np.cos(x)
    orig2 = lambda x: np.cos(x2 + x) - np.cos(x)

    new1 = lambda x: -2 * np.sin((x / 2) + x1) * np.sin(x)
    new2 = lambda x: -2 * np.sin((x / 2) + x2) * np.sin(x)

    expr1 = new1(delta) - orig1(delta)
    expr2 = new2(delta) - orig2(delta)

    plt.plot(delta, expr2)
    plt.xscale('log')
    plt.xlabel('delta')
    plt.ylabel('y')
    plt.title('Difference between expressions at x = 10^6')
    plt.show()



driver()