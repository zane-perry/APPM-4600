import numpy as np
import math
from numpy.linalg import inv 
from numpy.linalg import norm


def driver():

    x0 = np.array([2,-4])
    Nmax = 100
    tol = 1e-10

    [p,error,count] =  fixedpt_system(x0,tol,Nmax)
    print('The number of iterations was: ', '%d' % count)
    print('The approximate root is: ', p)
    print('The error message reads: ', '%d' % error)


def evalF(x): 

    F = np.zeros(2)
    
    F[0] = ((1/np.sqrt(2)) * np.sqrt(1 + ((x[0] + x[1])**2))) - (2/3)
    F[1] = ((1/np.sqrt(2)) * np.sqrt(1 + ((x[0] - x[1])**2))) - (2/3)
    return F


def fixedpt_system(x0, tol, Nmax):

    count = 0

    while(count < Nmax):
        count += 1
        x1 = evalF(x0)
        if(norm(x1 - x0) < tol):
            p = x1
            error = 0
            return [p ,error, count]
        x0 = x1

    p = x1
    error = 1
    return [p, error, Nmax]



driver()






