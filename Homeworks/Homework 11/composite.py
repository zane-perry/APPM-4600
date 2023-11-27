import numpy as np
from scipy.integrate import quad


def driver():

    f = lambda t: np.cos(1/t) * t
    a = 0
    b = 1
    n = 4

    simpsonQuad = compositeSimpsons(f,n,a,b)

    print('Value obtained from composite simpsons:', simpsonQuad)
    print('Number of function evaluations required:', n)


def compositeSimpsons(f,n,a,b):

    #n must be even

    xvals = np.linspace(a,b,n+1)
    h = (b-a) / n

    # forced to be zero because limit goes to 0 but does not exist
    sum = 0

    for j in range(1, n, 2):
        sum += 4 * f(xvals[j])
        sum += 2 * f(xvals[j + 1])

    sum -= f(xvals[n])

    return (h / 3) * sum

driver()