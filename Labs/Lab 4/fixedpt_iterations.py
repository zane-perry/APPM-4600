# import libraries
import numpy as np
    
def driver():

# test functions 
     g = lambda x: (10 / (x + 4)) ** (1/2)


     Nmax = 100
     tol = 1e-10
     x0 = 1.5
     p = 1.3652300134140976
     
     [xstar,ier, count, iterations] = fixedpt(g,x0,tol,Nmax)
     
     

     print('the number of iterations was ', count)
     print('the approximate fixed point is:',xstar)
     if(ier == 0):
        [order, constant] = convergence(p, iterations)
        print('the convergence is of order ', order)
        print('with asymptotic error constant ', constant)
        print('Iterations: \n', iterations)
     else:
        print('the sequence did not converge')
     print('f1(xstar):',g(xstar))
     print('Error message reads:',ier)
     



# define routines
def fixedpt(f,x0,tol,Nmax):

    ''' x0 = initial guess''' 
    ''' Nmax = max number of iterations'''
    ''' tol = stopping tolerance'''

    count = 0
    iterations = np.zeros((Nmax + 1,1))
    iterations[0,0] = x0
    while (count <Nmax):
       count = count +1
       x1 = f(x0)
       iterations[count, 0] = x1
       if (abs(x1-x0) <tol):
          xstar = x1
          ier = 0
          return [xstar,ier, count, np.trim_zeros(iterations)]
       x0 = x1

    xstar = x1
    ier = 1
    return [xstar, ier, count, iterations]


def convergence(p, p_vector):

    numerator = abs(p_vector[p_vector.size - 1,0] - p)
    denominator = abs(p_vector[p_vector.size - 2, 0] - p)

    alpha = 1

    limit = numerator / (denominator ** alpha)

    while(limit < 1e-4):
        print(denominator)
        alpha += 1
        limit = numerator / (denominator ** alpha)

    return [alpha, limit]

driver()