import numpy as np
import matplotlib.pyplot as plt


def driver():


    theta = np.linspace(0, 2 * np.pi, 1000)

    for i in range(10):
        p = np.random.uniform(low=0,high=2)
        x = x_param(i, 0.05, 2 + i, p, theta)
        y = y_param(i, 0.05, 2 + i, p, theta)
        plt.plot(x,y)





    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Plot 2')
    plt.show()




def x_param(R, delta_r, f, p, theta):

    vals = R * (1 + (delta_r * np.sin((f * theta) + p))) * np.cos(theta)

    return vals


def y_param(R, delta_r, f, p, theta):

    vals = R * (1 + (delta_r * np.sin((f * theta) + p))) * np.sin(theta)

    return vals


driver()