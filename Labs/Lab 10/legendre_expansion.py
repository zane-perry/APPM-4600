import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as la
import math
from scipy.integrate import quad

def driver():

#  function you want to approximate
    #f = lambda x: math.exp(x)
    f = lambda x: 1 / (1 + (x**2))

# Interval of interest    
    a = -1
    b = 1
# weight function    
    w = lambda x: 1.
    w1 = lambda x: 1 / math.sqrt(1 - (x**2))

# order of approximation
    n = 2

#  Number of points you want to sample in [a,b]
    N = 1000
    xeval = np.linspace(a,b,N+1)
    pval = np.zeros(N+1)

    for kk in range(N+1):
      pval[kk] = eval_legendre_expansion(f,a,b,w,n,xeval[kk])

    cval = np.zeros(N+1)

    for ii in range(N+1):
       cval[ii] = eval_chebyshev_expansion(f,a,b,w1,n,xeval[ii])
      
    # create vector with exact values
    fex = np.zeros(N+1)
    for kk in range(N+1):
        fex[kk] = f(xeval[kk])
        
    plt.figure()    
    plt.plot(xeval,fex,'r-', label= 'f(x)')
    plt.plot(xeval,pval,'b--',label= 'Legendre Expansion')
    plt.plot(xeval, cval, 'g--', label='Chebyshev Expansion')
    plt.legend()
    plt.title('L2 Approximation')
    plt.show()    
    
    err = abs(pval-fex)
    errc = abs(cval - fex)
    plt.semilogy(xeval,err,'r--',label='Legendre error')
    plt.semilogy(xeval, errc, 'b--', label='Chebyshev error')
    plt.legend()
    plt.title('Error of Approximation')
    plt.show()
    
      
    

def eval_legendre_expansion(f,a,b,w,n,x): 

#   This subroutine evaluates the Legendre expansion

#  Evaluate all the Legendre polynomials at x that are needed
# by calling your code from prelab 
  p = eval_legendre(n,x)
  # initialize the sum to 0 
  pval = 0.0    
  for j in range(0,n+1):
      # make a function handle for evaluating phi_j(x)
      phi_j = lambda x: eval_legendre(j,x)[j]
      # make a function handle for evaluating phi_j^2(x)*w(x)
      phi_j_sq = lambda x: (phi_j(x) ** 2) * w(x)
      # use the quad function from scipy to evaluate normalizations
      norm_fac,err = quad(phi_j_sq, a, b)
      # make a function handle for phi_j(x)*f(x)*w(x)/norm_fac
      func_j = lambda x: (phi_j(x) * f(x) * w(x)) / norm_fac
      # use the quad function from scipy to evaluate coeffs
      aj,err = quad(func_j, a, b)
      # accumulate into pval
      pval = pval+aj*p[j] 
       
  return pval


def eval_chebyshev_expansion(f,a,b,w,n,x): 

#   This subroutine evaluates the Legendre expansion

#  Evaluate all the Legendre polynomials at x that are needed
# by calling your code from prelab 
  p = eval_chebyshev(n,x)
  # initialize the sum to 0 
  pval = 0.0    
  for j in range(0,n+1):
      # make a function handle for evaluating phi_j(x)
      phi_j = lambda x: eval_chebyshev(j,x)[j]
      # make a function handle for evaluating phi_j^2(x)*w(x)
      phi_j_sq = lambda x: (phi_j(x) ** 2) * w(x)
      # use the quad function from scipy to evaluate normalizations
      norm_fac,err = quad(phi_j_sq, a, b)
      # make a function handle for phi_j(x)*f(x)*w(x)/norm_fac
      func_j = lambda x: (phi_j(x) * f(x) * w(x)) / norm_fac
      # use the quad function from scipy to evaluate coeffs
      aj,err = quad(func_j, a, b)
      # accumulate into pval
      pval = pval+aj*p[j] 
       
  return pval



def eval_legendre(n, x):
   
    if(n == 0):
       return np.array([1])
    
    if(n==1):
       return np.array([1,x])

    p = np.zeros(n+1)

    p[0] = 1
    p[1] = x

    for i in range(1, n):
       p[i + 1] = (1 / (i+1)) * (((2*i + 1) * x * p[i]) - (i * p[i-1]))

    return p

def eval_chebyshev(n, x):

    if(n == 0):
       return np.array([1])
    
    if(n==1):
       return np.array([1,x])

    p = np.zeros(n+1)

    p[0] = 1
    p[1] = x

    for i in range(1, n):
       p[i + 1] = (2 * x * p[i]) - p[i - 1]

    return p

       

    
if __name__ == '__main__':
  # run the drivers only if this is called from the command line
  driver()               
