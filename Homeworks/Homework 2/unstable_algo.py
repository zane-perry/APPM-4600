import numpy as np
import math


def driver():


    x = 9.999999995000000e-10

    y = (math.e ** x) - 1

    #y = x + ((x**2) / 2)
    print('The answer is {0:.16f}'.format(y))


driver()