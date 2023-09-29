# import libraries
import numpy as np

def driver():

# use routines    
    f = lambda x: np.exp((x ** 2) + (7 * x) - 30) - 1
    fp = lambda x: ((2*x) + 7) * np.exp((x ** 2) + (7 * x) - 30)
    fpp = lambda x: (((2*x) + 7) ** 2) * np.exp((x ** 2) + (7 * x) - 30)
    a = 2
    b = 4.5
    tol = 1e-14
    Nmax = 100


    [p,ier, count] = hybrid(f,fp,fpp,a,b,Nmax, tol)
    print('the number of iterations was ', count)
    print('the approximate root is',p)
    print('the error message reads:',ier)
    print('f(pstar) =', f(p))




# define routines
def hybrid(f,fp,fpp,a,b, Nmax, tol):
    

    fa = f(a)
    fb = f(b);
    if (fa*fb>0):
       ier = 1
       astar = a
       return [astar, ier]

#   verify end points are not a root 
    if (fa == 0):
      astar = a
      ier =0
      return [astar, ier, 0]

    if (fb ==0):
      astar = b
      ier = 0
      return [astar, ier, 0]

    count = 0
    d = 0.5*(a+b)
    gp = abs((f(d) * fpp(d)) / (fp(d) ** 2))
    print(gp)
    while (gp > 1):
      fd = f(d)
      if (fd ==0):
        astar = d
        ier = 0
        return [astar, ier, count]
      if (fa*fd<0):
         b = d
      else: 
        a = d
        fa = fd
      d = 0.5*(a+b)
      gp = abs((f(d) * fpp(d)) / (fp(d) ** 2))
      count = count +1
      
    p0 = d
    p = np.zeros(Nmax+1);
    p[0] = d
    for it in range(Nmax):
      count += 1
      p1 = p0-f(p0)/fp(p0)
      p[it+1] = p1
      if (abs(p1-p0) < tol):
          pstar = p1
          info = 0
          return [pstar,info,count]
      p0 = p1
    pstar = p1
    info = 1
    return [pstar,info,count]
      




driver()       




