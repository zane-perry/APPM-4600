import numpy as np
import math
from numpy.linalg import inv 
from numpy.linalg import norm



def driver():

    x0 = np.array([1,0])
    Nmax = 100
    tol = 1e-10

    [p,error,count] =  Newton(x0,tol,Nmax)
    print('The number of iterations was: ', '%d' % count)
    print('The approximate root is: ', p)
    print('The error message reads: ', '%d' % error)


def evalF(x): 

    F = np.zeros(2)
    
    F[0] = (4 * (x[0]**2)) + (x[1]**2) - 4
    F[1] = x[0] + x[1] - np.sin(x[0] - x[1])
    return F
    
def evalJ(x, h): 

    f = lambda x,y: (4*(x**2)) + (y**2) - 4
    g = lambda x,y: x + y - np.sin(x-y)
    
    J = np.array([[(f(x[0] + h, x[1]) - f(x[0],x[1])) / h, (f(x[0], x[1] + h) - f(x[0],x[1])) / h],
                  [(g(x[0] + h, x[1]) - g(x[0],x[1])) / h, (g(x[0], x[1] + h) - g(x[0],x[1])) / h]])
    return J


def Newton(x0,tol,Nmax):

    ''' inputs: x0 = initial guess, tol = tolerance, Nmax = max its'''
    ''' Outputs: xstar= approx root, ier = error message, its = num its'''

    for count in range(Nmax):

        h = norm(x0) * 1e-3
        #h = norm(x0) * 1e-7
        #h = norm(x0) * 1e-10
        J = evalJ(x0, h)
        Jinv = inv(J)
        F = evalF(x0)
       
        x1 = x0 - Jinv.dot(F)
       
        if (norm(x1-x0) < tol):
            p = x1
            error = 0
            return[p, error, count]
           
        x0 = x1
    
    p = x1
    count = 1
    return[p,error,Nmax]


driver()