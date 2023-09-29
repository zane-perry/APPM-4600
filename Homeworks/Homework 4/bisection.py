# import libraries
import numpy as np
import scipy

def driver():

# use routines    
    Ts = -15
    Ti = 20
    alpha = 0.138e-6
    t = 60 * 60 * 24 * 60
    f = lambda x: ((Ti - Ts) * scipy.special.erf(x / (2 * np.sqrt(alpha * t)))) + Ts

    a = 0
    b = 1

    tol = 1e-13

    [r,ier, count] = bisection(f,a,b,tol)
    print('the number of iterations was ', count)
    print('the approximate root is',r)
    print('the error message reads:',ier)
    print('f(astar) =', f(r))




# define routines
def bisection(f,a,b,tol):


    fa = f(a)
    fb = f(b);
    if (fa*fb>0):
       ier = 1
       r = a
       return [r, ier, 0]

#   verify end points are not a root 
    if (fa == 0):
      r = a
      ier =0
      return [r, ier, 0]

    if (fb ==0):
      r = b
      ier = 0
      return [r, ier, 0]

    count = 0
    d = 0.5*(a+b)
    while (abs(d-a)> tol):
      fd = f(d)
      if (fd ==0):
        r = d
        ier = 0
        return [r, ier, count]
      if (fa*fd<0):
         b = d
      else: 
        a = d
        fa = fd
      d = 0.5*(a+b)
      count = count +1
#      print('abs(d-a) = ', abs(d-a))
      
    r = d
    ier = 0
    return [r, ier, count]
      
driver()

#1b
#the number of iterations was  43
#the approximate root is 0.6769618544819309

