import numpy as np
from scipy.integrate import quad
from scipy.special import gamma
import math


def driver():

    f = lambda t,x: (t**(x-1)) * np.exp(-t)
    fg = lambda t,x: (t**(x-1))
    numEvals = 5
    
    n = 850
    a = 0
    b = 35

    xvals = np.arange(2, (numEvals * 2 + 1), 2)
    xevals = np.zeros(numEvals)
    relError = np.zeros(numEvals)


    quadEvals = np.zeros(numEvals)
    quadNums = np.zeros(numEvals)
    quadError = np.zeros(numEvals)

    gaussVals = np.zeros(numEvals)
    gaussNums = np.zeros(numEvals)

    realVals = np.zeros(numEvals)
    
    
    for i in range(numEvals):
        x = xvals[i]

        xevals[i] = compositeTrapezoid(f,n,a,b,x)

        [quadVal, msg, info] = quad(f, a, b, args=(x), full_output=1)
        quadEvals[i] = quadVal
        quadNums[i] = info['neval']

        [gaussVals[i], gaussNums[i]] = evaluateGauss(fg,x)

        realVals[i] = gamma(x)

        relError[i] = abs(xevals[i] - realVals[i]) / realVals[i]
        quadError[i] = abs(quadEvals[i] - realVals[i]) / realVals[i]

    print('Values from Composite Trapezoid:')
    for i in range(numEvals):
        print('x = ', xvals[i], ': ', xevals[i], '  Number of evaluations required: ', n, '  Relative error: ', relError[i])

    print('Values from Quad Routine:')
    for i in range(numEvals):
        print('x = ', xvals[i], ': ', quadEvals[i], '  Number of evaluations required: ', quadNums[i], '  Relative error:', quadError[i])

    print('Values from Gaussian:')
    for i in range(numEvals):
        print('x = ', xvals[i], ': ', gaussVals[i], '  Number of evaluations required: ', gaussNums[i])

    print('Values from Scipy:')
    for i in range(numEvals):
        print('x = ', xvals[i], ': ', realVals[i])


def compositeTrapezoid(f,n,a,b,x):

    tvals = np.linspace(a,b,n+1)
    h = (b - a) / n

    sum = f(tvals[0], x)
    sum += f(tvals[n], x)

    for j in range(1, n):
        sum += 2 * f(tvals[j], x)

    return (h / 2) * sum


def evaluateGauss(f,x):

    deg = math.ceil(x/2)
    [tvals,weights] = np.polynomial.laguerre.laggauss(deg)

    sum = 0

    for i in range (deg):
        sum += (f(tvals[i], x) * weights[i])

    return sum, deg

driver()