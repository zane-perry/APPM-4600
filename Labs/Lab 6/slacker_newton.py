import numpy as np
import math
from numpy.linalg import inv 
from numpy.linalg import norm



def driver():

    x0 = np.array([1,0])
    Nmax = 100
    tol = 1e-10

    [p,error,count, invCount] =  SlackerNewton(x0,tol,Nmax)
    print('The number of iterations was: ', '%d' % count)
    print('The approximate root is: ', p)
    print('The error message reads: ', '%d' % error)
    print('The number of inverses required: ', invCount)


def evalF(x): 

    F = np.zeros(2)
    
    F[0] = (4 * (x[0]**2)) + (x[1]**2) - 4
    F[1] = x[0] + x[1] - np.sin(x[0] - x[1])
    return F
    
def evalJ(x): 

    
    J = np.array([[8*x[0],2*x[1]],
                  [1-np.cos(x[0]-x[1]), 1+np.cos(x[0]-x[1])]])
    return J


def SlackerNewton(x0,tol,Nmax):

    J = evalJ(x0)
    Jinv = inv(J)
    invCount = 1
    for count in range(Nmax):

        F = evalF(x0)
        x1 = x0 - Jinv.dot(F)
       
        if (norm(x1-x0) < tol):
           p = x1
           error = 0
           return[p,error,count, invCount]
        
        if(norm(x1 - x0) > 1e-2):
            J = evalJ(x1)
            Jinv = inv(J)
            invCount += 1

           
        x0 = x1
    
    p = x1
    error = 1
    return[p,error,count, invCount]  

driver()