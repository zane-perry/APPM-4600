import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt

def driver():


    f = lambda x: 1 / (1 + ((10 * x)**2))

    N = 19
    ''' interval'''
    a = -1
    b = 1
   
   
    i = np.arange(1,N+1,1)
    h = 2 / (N-1)
    xint = -1 + ((i-1) * h)

    #xint = np.cos((((2*i) - 1) * np.pi) / (2*N))

    
    ''' create interpolation data'''
    yint = f(xint)
    
    ''' create points for evaluating the Lagrange interpolating polynomial'''
    Neval = 1000
    xeval = np.linspace(a,b,Neval+1)
    yeval_m = np.zeros(Neval+1)

    a = monomialArray(xint,yint, N)


    for kk in range(Neval):
       yeval_m[kk] = eval_m(xeval[kk],a,N)
       

    ''' create vector with exact values'''
    fex = f(xeval)
       
    
    plt.figure()    
    plt.plot(xeval,fex,'r-', label='f(x)')
    plt.plot(xeval,yeval_m, 'b-', label='Monomial Approximation')
    plt.title('Monomial Approximation Graph for N={N}'.format(N=N))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()


def monomialArray(x,y,n):
   
    A = np.zeros([n,n])

    for i in range(n):
        for j in range(n):
            A[i][j] = x[i] ** j

    Ainv = la.inv(A)

    a = Ainv.dot(y)

    return a

def eval_m(xeval,a,n):

    yeval = 0.

    for jj in range(n):
        yeval += a[jj] * (xeval**jj)

    return yeval



driver()