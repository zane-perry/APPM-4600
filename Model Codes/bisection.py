# import libraries
import numpy as np

def driver():

# use routines    
    f = lambda x: np.exp((x ** 2) + (7 * x) - 30) - 1
    a = 2
    b = 4.5

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
