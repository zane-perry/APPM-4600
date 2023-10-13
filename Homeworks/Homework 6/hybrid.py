#libraries:
import matplotlib.pyplot as plt
import numpy as np
import math
from numpy.linalg import inv 
from numpy.linalg import norm


def driver():

    Nmax = 100
    x0= np.array([1/2,1/2,1/2])
    tol1 = 5e-2
    
    [p1,gval,error, count1, p_iterations1] = SteepestDescent(x0,tol1,Nmax)

    tol2 = 1e-6
    [p,error,count2, p_iterations2] =  Newton(p1,tol2,Nmax)

    print('The number of iterations was: ', '%d' % (count1 + count2))
    print('The approximate root is: ', p)
    print('The error message reads: ', '%d' % error)
    print('Steepest Descent Iterations: ')
    for it in range(count1 + 1):
        print('x value: ', '%16.16e' % p_iterations1[it][0], 'y value: ', '%16.16e' % p_iterations1[it][1], 'z value: ', '%16.16e' % p_iterations1[it][2])
    print('Newton Iterations:')
    for it in range(count2 + 1):
        print('x value: ', '%16.16e' % p_iterations2[it][0], 'y value: ', '%16.16e' % p_iterations2[it][1], 'z value: ', '%16.16e' % p_iterations2[it][2])

###########################################################
#functions:
def evalF(x):

    F = np.zeros(3)
    F[0] = x[0] + np.cos(x[0]*x[1]*x[2]) - 1
    F[1] = ((1-x[0])**(1/4)) + x[1] + (0.05 * (x[2]**2)) - (0.15 * x[2]) - 1
    F[2] = -(x[0]**2) - (0.1 * (x[1]**2)) + (0.01 * x[1]) + x[2] - 1
    return F

def evalJ(x): 

    J = np.array([[1-(x[1]*x[2]*np.sin(x[0]*x[1]*x[2])), -x[0]*x[2]*np.sin(x[0]*x[1]*x[2]), -x[0]*x[1]*np.sin(x[0]*x[1]*x[2])],
                   [(-1/4)*((1-x[0])**(-3/4)), 1, (0.1*x[2]) - 0.15],
                   [-2*x[0], (-0.2*x[1]) + 0.01, 1]])
    return J

def evalg(x):

    F = evalF(x)
    g = F[0]**2 + F[1]**2 + F[2]**2
    return g

def eval_gradg(x):
    F = evalF(x)
    J = evalJ(x)
    
    gradg = np.transpose(J).dot(F)
    return gradg


###############################
### steepest descent code

def SteepestDescent(x,tol,Nmax):

    p_iterations = np.zeros([Nmax, 3])
    p_iterations[0] = x
    
    for count in range(Nmax):
        g1 = evalg(x)
        z = eval_gradg(x)
        z0 = norm(z)

        if z0 == 0:
            print("zero gradient")
        z = z/z0
        alpha1 = 0
        alpha3 = 1
        dif_vec = x - alpha3*z
        g3 = evalg(dif_vec)

        while g3>=g1:
            alpha3 = alpha3/2
            dif_vec = x - alpha3*z
            g3 = evalg(dif_vec)
            
        if alpha3<tol:
            print("no likely improvement")
            error = 0
            return [x,g1,error, count + 1, p_iterations]
        
        alpha2 = alpha3/2
        dif_vec = x - alpha2*z
        g2 = evalg(dif_vec)

        h1 = (g2 - g1)/alpha2
        h2 = (g3-g2)/(alpha3-alpha2)
        h3 = (h2-h1)/alpha3

        alpha0 = 0.5*(alpha2 - h1/h3)
        dif_vec = x - alpha0*z
        g0 = evalg(dif_vec)

        if g0<=g3:
            alpha = alpha0
            gval = g0

        else:
            alpha = alpha3
            gval =g3

        x = x - alpha*z
        p_iterations[count + 1] = x

        if abs(gval - g1)<tol:
            error = 0
            return [x,gval,error, count + 1, p_iterations]

    print('max iterations exceeded')    
    error = 1        
    return [x,g1,error, Nmax, p_iterations]



def Newton(x0,tol,Nmax):

    ''' inputs: x0 = initial guess, tol = tolerance, Nmax = max its'''
    ''' Outputs: xstar= approx root, ier = error message, its = num its'''

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





