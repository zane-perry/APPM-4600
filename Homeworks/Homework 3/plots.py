import numpy as np
import matplotlib.pyplot as plt

def driver():

    x = np.linspace(-2,9,1000)
    f = lambda x: x - 4 * np.sin(2 * x) - 3
    y = f(x)

    plt.plot(x,y)
    plt.hlines(0, -2, 9, colors="red", linestyles="dashed")
    plt.xlabel('x')
    plt.xticks(np.arange(-2, 10, 1))
    plt.ylabel('y')
    plt.title('Plot of f(x)')
    plt.show()


driver()