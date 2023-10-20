import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt

def driver():

    f = lambda x: 1 / (1 + ((10 * x)**2))

    N = 800
    ''' interval'''
    a = -1
    b = 1

    i = np.arange(1,N+1,1)
    #h = 2 / (N-1)
    #xint = -1 + ((i-1) * h)

    xint = np.cos((((2*i) - 1) * np.pi) / (2*N))

    yint = f(xint)

    Neval = 1000
    xeval = np.linspace(a,b,Neval+1)
    yeval_b = np.zeros(Neval+1)

    w = eval_w(xint,N)

    for kk in range(Neval):
       yeval_b[kk] = eval_bary(xeval[kk], xint, yint, w, N)

    fex = f(xeval)
       
    
    plt.figure()    
    plt.plot(xeval,fex,'r-', label='f(x)')
    plt.plot(xeval,yeval_b, 'b--', label='Barycentric Lagrange Approximation')
    plt.title('Barycentric Approximation Graph for N={N} (Chebyshev Nodes)'.format(N=N))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(loc='center right')
    plt.show()




def eval_phi(xint, xk):

    prod = 1

    for xi in xint:
        prod *= (xk - xi)

    return prod


def eval_w(xint, N):

    w = np.zeros(N)

    for j in range(N):
        prod = 1
        for i in range(N):
            if(i != j):
                prod *= (xint[j] - xint[i])

        w[j] = 1 / prod

    
    return w

def eval_bary(xeval, xint, yint, w, N):
    
    sum = 0

    phi = eval_phi(xint,xeval)

    for j in range(N):
        sum += ((w[j] / (xeval - xint[j])) * yint[j])

    return phi * sum

driver()