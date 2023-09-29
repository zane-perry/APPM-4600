# import libraries
import numpy as np
import scipy

        
def driver():

  #Ts = -15
  #Ti = 20
  #alpha = 0.138e-6
  #t = 60 * 60 * 24 * 60
  #f = lambda x: ((Ti - Ts) * scipy.special.erf(x / (2 * np.sqrt(alpha * t)))) + Ts
  #fp = lambda x: ((Ti - Ts) / np.sqrt(np.pi * alpha * t)) * np.exp(-(x**2)/(4*alpha*t))
  #p0 = 1

  #f = lambda x: np.exp(3 * x) - (27 * (x**6)) + (27 * (x**4) * np.exp(x)) - (9 * (x**2) * np.exp(2 * x))
  #fp = lambda x: 3 * (np.exp(x) - (6 * x)) * ((np.exp(x) - (3 * (x**2))) ** 2)
  #fpp = lambda x: 3 * (np.exp(x) - (3 * (x**2))) * ((90 * (x**2)) - (3 * np.exp(x) * ((x**2) + (8 * x) + 2)) + (3 * np.exp(2 * x)))
  #p0 = 3
 
  #g = lambda x: f(x) / fp(x)
  #gp = lambda x: 1 - ((f(x) * fpp(x)) / (fp(x) ** 2))

  f = lambda x: (x**6) - x - 1
  fp = lambda x: (6 * (x**5)) - 1
  p0 = 2
  


  Nmax = 100
  tol = 1e-13

  (p,pstar,info,it) = newton(f,fp,p0,tol, Nmax)
  alpha = convergence(pstar, p)
  print('the approximate root is', '%16.16e' % pstar)
  print('the error message reads:', '%d' % info)
  print('Number of iterations:', '%d' % it)
  print('With approximate convergence of order: ', alpha)

  errors = abs(p - pstar)
  print('Errors:')
  for error in errors:
    print('{0:.16f}'.format(error))


def newton(f,fp,p0,tol,Nmax):

  p = np.zeros(Nmax+1);
  p[0] = p0
  for it in range(Nmax):
      p1 = p0-f(p0)/fp(p0)
      #p1 = p0 - (3 * (f(p0) / fp(p0)))
      p[it+1] = p1
      if (abs(p1-p0) < tol):
          pstar = p1
          info = 0
          return [np.trim_zeros(p),pstar,info,it]
      p0 = p1
  pstar = p1
  info = 1
  return [p,pstar,info,it]


def convergence(p, p_vector):

    index = 2
    error1 = abs(p_vector[p_vector.size - index] - p)
    while(error1 < 1e-4):
       index += 1
       error1 = abs(p_vector[p_vector.size - index] - p)
    error2 = abs(p_vector[p_vector.size - (index + 1)] - p)


    return np.log(error1) / np.log(error2)


        
driver()

#1ci
#Number of iterations: 4
#the approximate root is 6.7696185448193646e-01

#1cii
#Number of iterations: 4
#the approximate root is 6.7696185448193646e-01



#4i
#Number of iterations: 27
#the approximate root is 3.7330956674925440e+00
#With approximate convergence of order:  1.0524547395079755

#4ii
#Number of iterations: 17
#the approximate root is 3.7330656242115396e+00
#With approximate convergence of order:  2.0279842466295985

#4iii
#Number of iterations: 12
#the approximate root is 3.7330790036869175e+00
#With approximate convergence of order:  2.02476834360095

#5a
#Number of iterations: 8
#the approximate root is 1.1347241384015194e+00
#With approximate convergence of order:  1.7739775178691108