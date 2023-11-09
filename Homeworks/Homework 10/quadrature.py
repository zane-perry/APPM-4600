import numpy as np
from scipy.integrate import quad


def driver():

    f = lambda x: 1 / (1 + (x**2))
    a = -5
    b = 5
    n1 = 1291
    n2 = 1156

    trapezoidalQuad = compositeTrapezoid(f,n1,a,b)
    simpsonQuad = compositeSimpsons(f,n2,a,b)

    [scipyQuad4, msg4, info4] = quad(f,-5,5, epsabs=1e-4, full_output=1)
    [scipyQuad6, msg6, info6] = quad(f,-5,5, epsabs=1e-6, full_output=1)

    print('Value obtained from composite trapezoidal:', trapezoidalQuad)
    print('Number of function evaluations required:', n1)
    print('Value obtained from composite simpsons:', simpsonQuad)
    print('Number of function evaluations required:', n2)
    print('Value obtained from scipy routine (tolerance of 10^-4):', scipyQuad4)
    print('Number of function evaluations required:', info4['neval'])
    print('Value obtained from scipy routine (tolerance of 10^-6):', scipyQuad6)
    print('Number of function evaluations required:', info6['neval'])




def compositeTrapezoid(f,n,a,b):

    xvals = np.linspace(a,b,n+1)
    h = (b - a) / n

    sum = f(xvals[0])
    sum += f(xvals[n])

    for i in range(1, n):
        sum += 2 * f(xvals[i])

    return (h / 2) * sum

def compositeSimpsons(f,n,a,b):

    #n must be even

    xvals = np.linspace(a,b,n+1)
    h = (b-a) / n

    sum = f(xvals[0])

    for j in range(1, n, 2):
        sum += 4 * f(xvals[j])
        sum += 2 * f(xvals[j + 1])

    sum -= f(xvals[n])

    return (h / 3) * sum

driver()