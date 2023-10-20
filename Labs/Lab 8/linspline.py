import matplotlib.pyplot as plt
import numpy as np
import math
from numpy.linalg import inv 


def driver():
    
    f = lambda x: 1 / (1 + (10 * x) ** 2)
    a = -1
    b = 1
    
    ''' create points you want to evaluate at'''
    Neval = 100
    xeval =  np.linspace(a,b,Neval)
    
    ''' number of intervals'''
    Nint = 10
    
    '''evaluate the linear spline'''
    yeval = eval_lin_spline(xeval,Neval,a,b,f,Nint)
    
    ''' evaluate f at the evaluation points'''
    fex = np.zeros(Neval)
    for j in range(Neval):
      fex[j] = f(xeval[j]) 
      
    
    plt.figure()
    plt.plot(xeval,fex,'ro-', label='f(x)')
    plt.plot(xeval,yeval,'b--', label='Linear Spline')
    plt.legend()
    plt.title('f(x) and spline approximation')
    plt.show()
     
    err = abs(yeval-fex)
    plt.figure()
    plt.plot(xeval,err,'ro-')
    plt.title('Error of linear spline')
    plt.show()
    
    

    
    
def  eval_lin_spline(xeval,Neval,a,b,f,Nint):

    '''create the intervals for piecewise approximations'''
    xint = np.linspace(a,b,Nint+1)

    #j = np.arange(0,Nint+1,1)
    #h = 2 / (Nint - 1)
    #xint = -1 + ((j-1) * h)
    
    #j = np.arange(1, Nint+1, 1)
    #xint = np.cos((((2*j) - 1)*np.pi) / (2 * Nint))

   
    '''create vector to store the evaluation of the linear splines'''
    yeval = np.zeros(Neval) 
    
    
    for jint in range(Nint - 1):
        '''find indices of xeval in interval (xint(jint),xint(jint+1))'''
        '''let ind denote the indices in the intervals'''
        '''let n denote the length of ind'''
        ind = get_indices(xint[jint], xint[jint+1], xeval)
        n = ind.size
        
        '''temporarily store your info for creating a line in the interval of 
         interest'''
        a1= xint[jint]
        fa1 = f(a1)
        b1 = xint[jint+1]
        fb1 = f(b1)
        
        for kk in range(n):
           '''use your line evaluator to evaluate the lines at each of the points 
           in the interval'''
           '''yeval(ind(kk)) = call your line evaluator at xeval(ind(kk)) with 
           the points (a1,fa1) and (b1,fb1)'''
           yeval[ind[kk]] = line_evaluator(a1, fa1, b1, fb1, xeval[ind[kk]])

    return yeval


def get_indices(x0, x1, xeval):
    ind = np.where((xeval <= x1) & (xeval >= x0))
    return ind[0]


def line_evaluator(a1, fa1, b1, fb1, xk):
    
    l0 = lambda x: (x - b1) / (a1 - b1)
    l1 = lambda x: (x - a1) / (b1 - a1)

    return (fa1 * l0(xk)) + (fb1 * l1(xk))
           
           

driver()               
