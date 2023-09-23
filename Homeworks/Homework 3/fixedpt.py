# import libraries
import numpy as np
    
def driver():

     f1 = lambda x:  -np.sin(2 * x) + ((5/4) * x) - (3/4)


     Nmax = 100
     tol = 0.5e-10


     x0 = 4.5
     [xstar,ier] = fixedpt(f1,x0,tol,Nmax)
     print('the approximate fixed point is:',xstar)
     print('f1(xstar):',f1(xstar))
     print('Error message reads:',ier)
    



# define routines
def fixedpt(f,x0,tol,Nmax):

    count = 0
    while (count <Nmax):
       count = count +1
       x1 = f(x0)
       if (abs((x1-x0) / x1) <tol):
          xstar = x1
          ier = 0
          return [xstar,ier]
       x0 = x1

    xstar = x1
    ier = 1
    return [xstar, ier]
    

driver()