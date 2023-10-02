# import libraries
import numpy as np

def driver():

# use routines    
  f = lambda x: np.exp((x ** 2) + (7 * x) - 30) - 1
  a = 2
  b = 4.5

  tol = 1e-13

  [p,error, count] = bisection(f,a,b,tol)
  print('The number of iterations was: ', count)
  print('The approximate root is: ',p)
  print('The error message reads: ', error)




# define routines
def bisection(f,a,b,tol):

  count = 0

  fa = f(a)
  fb = f(b);
  if (fa*fb>0):
    error = 1
    p = a
    return [p, error, count]

#   verify end points are not a root 
  if (fa == 0):
    p = a
    error = 0
    return [p, error, count]

  if (fb ==0):
    p = b
    error = 0
    return [p, error, count]

  d = 0.5*(a+b)
  while (abs(d-a)> tol):
    count += 1
    fd = f(d)
    if (fd ==0):
      p = d
      error = 0
      return [p, error, count]
    if (fa*fd<0):
      b = d
    else: 
      a = d
      fa = fd
    d = 0.5*(a+b)
      
  p = d
  ier = 0
  return [p, ier, count]
      
driver()               
