import numpy as np
import math
from numpy.linalg import inv 
from numpy.linalg import norm



def driver():

    #x0 = np.array([1,-1])
    x0 = np.array([0,1,1])
    Nmax = 100
    tol = 1e-6

    [p,error,count, p_iterations] =  Newton(x0,tol,Nmax)
    print('The number of iterations was: ', '%d' % count)
    print('The approximate root is: ', p)
    print('The error message reads: ', '%d' % error)
    print('Iterations: ')
    for it in range(count + 1):
        #print('x value: ', '%16.16e' % p_iterations[it][0], 'y value: ', '%16.16e' % p_iterations[it][1])
        print('x value: ', '%16.16e' % p_iterations[it][0], 'y value: ', '%16.16e' % p_iterations[it][1], 'z value: ', '%16.16e' % p_iterations[it][2])

    print(evalF(p))



def evalF(x): 

    ##F = np.zeros(2)
    #F[0] = (x[0]**2) + (x[1]**2) - 4
    #F[1] = np.exp(x[0]) + x[1] - 1

    F = np.zeros(3)
    F[0] = x[0] + np.cos(x[0]*x[1]*x[2]) - 1
    F[1] = ((1-x[0])**(1/4)) + x[1] + (0.05 * (x[2]**2)) - (0.15 * x[2]) - 1
    F[2] = -(x[0]**2) - (0.1 * (x[1]**2)) + (0.01 * x[1]) + x[2] - 1
    return F
    
def evalJ(x): 

    
    #J = np.array([[2*x[0], 2*x[1]],
                  #[np.exp(x[0]), 1]])

    J = np.array([[1-(x[1]*x[2]*np.sin(x[0]*x[1]*x[2])), -x[0]*x[2]*np.sin(x[0]*x[1]*x[2]), -x[0]*x[1]*np.sin(x[0]*x[1]*x[2])],
                   [(-1/4)*((1-x[0])**(-3/4)), 1, (0.1*x[2]) - 0.15],
                   [-2*x[0], (-0.2*x[1]) + 0.01, 1]])
    return J


def Newton(x0,tol,Nmax):

    ''' inputs: x0 = initial guess, tol = tolerance, Nmax = max its'''
    ''' Outputs: xstar= approx root, ier = error message, its = num its'''

    #p_iterations = np.zeros([Nmax, 2])
    p_iterations = np.zeros([Nmax, 3])
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