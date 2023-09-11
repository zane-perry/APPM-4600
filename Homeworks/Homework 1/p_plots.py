import math
import matplotlib.pyplot as plt
import numpy as np


def driver():

    x1 = np.arange(1.920, 2.081, 0.001)

    p_expanded = lambda x: x**9 - 18*(x**8) + 144*(x**7) - 672*(x**6) + 2016*(x**5) - 4032*(x**4) + 5376*(x**3) - 4608*(x**2) + 2304*x - 512
    p_binomial = lambda x: (x-2)**9

    p1 = p_expanded(x1)
    p2 = p_binomial(x1)


    plt.plot(x1, p2)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Evaluating p using binomial form')
    plt.show()


driver()