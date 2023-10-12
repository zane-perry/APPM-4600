# import libraries
import numpy as np
        
def driver():
  
  f = lambda x: np.exp((x ** 2) + (7 * x) - 30) - 1
  fp = lambda x: ((2*x) + 7) * np.exp((x ** 2) + (7 * x) - 30)
  p0 = 4.5

  Nmax = 100
  tol = 1e-13

  (p,p_iterations,error,count) = newton(f,fp,p0,tol, Nmax)
  print('The number of iterations was: ', '%d' % count)
  print('The approximate root is: ', '%16.16e' % p)
  print('The error message reads: ', '%d' % error)
  print('Iterations: ')
  for it in range(count + 1):
    print('%16.16e' % p_iterations[it])
  


def newton(f,fp,p0,tol,Nmax):

  p_iterations = np.zeros(Nmax+1);
  p_iterations[0] = p0
  for count in range(Nmax):
      p1 = p0-f(p0)/fp(p0)
      p_iterations[count+1] = p1
      if (abs(p1-p0) < tol):
          p = p1
          error = 0
          return [p,p_iterations,error,count + 1]
      p0 = p1
  p = p1
  error = 1
  return [p,p_iterations,error,count + 1]
        
driver()