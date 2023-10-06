import numpy as np
import math
from numpy.linalg import inv 
from numpy.linalg import norm



def driver():

    x0 = np.array([1,1])
    Nmax = 100
    tol = 1e-10

    [p,error,count, p_iterations] =  Newton(x0,tol,Nmax)
    print('The number of iterations was: ', '%d' % count)
    print('The approximate root is: ', p)
    print('The error message reads: ', '%d' % error)
    print('Iterations: ')
    print('Iterations: ')
    for it in range(count + 1):
        print('x value: ', '%16.16e' % p_iterations[it][0], 'y value: ', '%16.16e' % p_iterations[it][1])



def evalF(x): 

    F = np.zeros(2)
    
    F[0] = (3*(x[0]**2)) - (x[1]**2)
    F[1] = (3 * x[0] * (x[1]**2)) - (x[0]**3) - 1
    return F
    
def evalJ(x): 

    
    J = np.array([[6*x[0], -(2 * x[1])],
                  [(3 * (x[1]**2)) - (3 * (x[0]**2)), 6*x[0]*x[1]]])
    return J


def Newton(x0,tol,Nmax):

    ''' inputs: x0 = initial guess, tol = tolerance, Nmax = max its'''
    ''' Outputs: xstar= approx root, ier = error message, its = num its'''

    p_iterations = np.zeros([Nmax, 2])
    p_iterations[0] = x0

    for count in range(Nmax):
        J = evalJ(x0)
        Jinv = inv(J)
        F = evalF(x0)
       
        x1 = x0 - Jinv.dot(F)
        p_iterations[count + 1] = x1
       
        if (norm(x1-x0) < tol):
            p = x1
            error = 0
            return[p, error, count + 1, p_iterations]
           
        x0 = x1
    
    p = x1
    count = 1
    return[p,error,Nmax, p_iterations]


driver()