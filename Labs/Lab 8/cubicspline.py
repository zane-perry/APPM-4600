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

    h = (b-a)/Nint


    
    '''evaluate the linear spline'''
    
    
    ''' evaluate f at the evaluation points'''
    fex = np.zeros(Neval)
    for j in range(Neval):
      fex[j] = f(xeval[j]) 

    

    xint = np.linspace(a,b,Nint+1)

    yint = np.zeros(Nint+1)
    for j in range(Nint+1):
        yint[j] = f(xint[j])

    M = build_coefficients(xint,yint,Nint + 1,h)

    yeval = eval_cubic_spline(xeval,Neval,f,Nint, xint, M)
      
    
    plt.figure()
    plt.plot(xeval,fex,'ro-', label='f(x)')
    plt.plot(xeval,yeval,'b--', label='Cubic Spline')
    plt.legend()
    plt.title('f(x) and spline approximation')
    plt.show()

    
    err = abs(yeval-fex)
    plt.figure()
    plt.plot(xeval,err,'ro-')
    plt.title('Error of cubic spline')
    plt.show()
    
    

    
    
def  eval_cubic_spline(xeval,Neval,f,Nint, xint, M):

   
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
           yeval[ind[kk]] = line_evaluator(a1, fa1, b1, fb1, M[jint], M[jint+1], xeval[ind[kk]])

    return yeval


def get_indices(x0, x1, xeval):
    ind = np.where((xeval <= x1) & (xeval >= x0))
    return ind[0]


def line_evaluator(a, fa, b, fb, Mi, Mi1, xk):
    
    h = b - a
    c = (fa / h) - (h * Mi/6)
    d = (fb / h) - (h*Mi1/6)

    s = lambda x: ((((b-x)**3)*Mi) / (6*h)) + ((((x-a)**3)*Mi1) / (6*h)) + (c*(b-x)) + (d*(x-a))


    return s(xk)


def build_coefficients(xint,yint,Nint,h):
    A = np.zeros([Nint-2,Nint-2])

    A[0][0] = 1/3
    A[0][1] = 1/12

    for ii in range(1, Nint - 3):
        A[ii][ii - 1] = 1/12
        A[ii][ii] = 1/3
        A[ii][ii + 1] = 1/12

    A[Nint-3][Nint-4] = 1/12
    A[Nint-3][Nint-3] = 1/3

    b = np.zeros(Nint - 2)

    for ii in range(Nint - 2):
        b[ii] = (yint[ii + 2] - (2 * yint[ii + 1]) + yint[ii]) / (2 * (h**2))

    Ainv = inv(A)

    M = np.array(Ainv.dot(b))

    M = np.insert(M , 0, 0)

    M = np.append(M, 0)

    print(b)

    return M

           
           

driver()   