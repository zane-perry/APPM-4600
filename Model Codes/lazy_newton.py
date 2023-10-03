import numpy as np
import math
from numpy.linalg import inv 
from numpy.linalg import norm



def driver():

    x0 = np.array([0.1, 0.1, -0.1])
    Nmax = 100
    tol = 1e-10

    [p,error,count] =  LazyNewton(x0,tol,Nmax)
    print('The number of iterations was: ', '%d' % count)
    print('The approximate root is: ', p)
    print('The error message reads: ', '%d' % error)


def evalF(x): 

    F = np.zeros(3)
    
    F[0] = 3*x[0]-math.cos(x[1]*x[2])-1/2
    F[1] = x[0]-81*(x[1]+0.1)**2+math.sin(x[2])+1.06
    F[2] = np.exp(-x[0]*x[1])+20*x[2]+(10*math.pi-3)/3
    return F
    
def evalJ(x): 

    
    J = np.array([[3.0, x[2]*math.sin(x[1]*x[2]), x[1]*math.sin(x[1]*x[2])], 
        [2.*x[0], -162.*(x[1]+0.1), math.cos(x[2])], 
        [-x[1]*np.exp(-x[0]*x[1]), -x[0]*np.exp(-x[0]*x[1]), 20]])
    return J


def LazyNewton(x0,tol,Nmax):

    ''' Lazy Newton = use only the inverse of the Jacobian for initial guess'''
    ''' inputs: x0 = initial guess, tol = tolerance, Nmax = max its'''
    ''' Outputs: xstar= approx root, ier = error message, its = num its'''

    J = evalJ(x0)
    Jinv = inv(J)
    for count in range(Nmax):

       F = evalF(x0)
       x1 = x0 - Jinv.dot(F)
       
       if (norm(x1-x0) < tol):
           p = x1
           error = 0
           return[p,error,count]
           
       x0 = x1
    
    p = x1
    error = 1
    return[p,error,count]  

driver()