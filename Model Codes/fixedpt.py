# import libraries
import numpy as np
    
def driver():

    f = lambda x:  2 * np.sin(x)
    Nmax = 100
    tol = 1e-10
    x0 = 1

    [p,error,count] = fixedpt(f,x0,tol,Nmax)
    print('The number of iterations was: ', '%d' % count)
    print('The approximate root is: ', '%16.16e' % p)
    print('The error message reads: ', '%d' % error)
    



# define routines
def fixedpt(f,x0,tol,Nmax):

    count = 0
    while (count <Nmax):
       count += 1
       x1 = f(x0)
       if (abs((x1-x0) / x1) <tol):
          p = x1
          error = 0
          return [p,error,count]
       x0 = x1

    p = x1
    error = 1
    return [p, error,count]
    

driver()