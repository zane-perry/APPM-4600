# import libraries
import numpy as np
        
def driver():

  f = lambda x: (x**6) - x - 1
  x0 = 2
  x1 = 1

  Nmax = 100
  tol = 1e-13

  (p, r, ier, count) = secant(f,x0,x1,tol, Nmax)
  print('the approximate root is', '%16.16e' % r)
  print('the error message reads:', '%d' % ier)
  print('Number of iterations:', '%d' % count)

  errors = abs(p - r)
  print('Errors:')
  for error in errors:
    print('{0:.16f}'.format(error))



def secant(f,x0,x1,tol,Nmax):
   

   fx0 = f(x0)
   fx1 = f(x1)

   if(fx0 == 0):
      r = fx0
      ier = 0
      return [r, ier, 0]
   if(fx1 == 0):
      r = fx1
      ier = 0
      return [r, ier, 0]
   
   p = np.zeros(Nmax+1)
   p[0] = x1
   for it in range(Nmax):
      if(fx0 - fx1 == 0):
         ier = 1
         r = x1
         return [np.trim_zeros(p), r, ier, it]
      
      x2 = x1 - ((fx1 * (x1 - x0)) / (fx1 - fx0))
      p[it + 1] = x2
      if(abs(x2 - x1) < tol):
         r = x2
         ier = 0
         return [np.trim_zeros(p), r, ier, it]

      
      x0 = x1
      x1 = x2
      fx0 = f(x0)
      fx1 = f(x1)
      

   r = x1
   ier = 1
   return [p, r, 1, Nmax]


        
driver()

#5
#Number of iterations: 8
#the approximate root is 1.1347241384015194e+00