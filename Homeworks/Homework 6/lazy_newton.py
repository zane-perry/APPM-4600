import numpy as np
import math
from numpy.linalg import inv 
from numpy.linalg import norm



def driver():

    x0 = np.array([1,-1])
    Nmax = 100
    tol = 1e-10

    [p,error,count, p_iterations] =  LazyNewton(x0,tol,Nmax)
    print('The number of iterations was: ', '%d' % count)
    print('The approximate root is: ', p)
    print('The error message reads: ', '%d' % error)
    print('Iterations: ')
    for it in range(count + 1):
        print('x value: ', '%16.16e' % p_iterations[it][0], 'y value: ', '%16.16e' % p_iterations[it][1])


def evalF(x): 

    F = np.zeros(2)
    F[0] = (x[0]**2) + (x[1]**2) - 4
    F[1] = np.exp(x[0]) + x[1] - 1

    return F
    
def evalJ(x): 

    
    J = np.array([[2*x[0], 2*x[1]],
                  [np.exp(x[0]), 1]])
    return J


def LazyNewton(x0,tol,Nmax):

    p_iterations = np.zeros([Nmax, 2])
    p_iterations[0] = x0
    J = evalJ(x0)
    Jinv = inv(J)
    for count in range(Nmax - 1):

       F = evalF(x0)
       x1 = x0 - Jinv.dot(F)
       p_iterations[count + 1] = x1
       
       if (norm(x1-x0) < tol):
           p = x1
           error = 0
           return[p,error,count + 1, p_iterations]
           
       x0 = x1
    
    p = x1
    error = 1
    return[p,error,Nmax, p_iterations]  

driver()