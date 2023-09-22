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
     
     
     print('FIXED POINT')
     print('the number of iterations was ', count)
     print('the approximate fixed point is:', xstar)
     if(ier == 0):
        [order, constant] = convergence(p, iterations)
        print('the convergence is of order ', order)
        print('with asymptotic error constant ', constant)
        print('Iterations: \n', iterations)
     else:
        print('the sequence did not converge')
     print('error message reads: ',ier)

     [xstar, iterations, ier, count] = aitken(iterations, count, tol)

     print('AITKENS')
     print('the number of iterations was ', count)
     print('the approximate fixed point is: ', xstar)

     if(ier == 0):
        [order, constant] = convergence(p, iterations)
        print('the convergence is of order ', order)
        print('with asymptotic error constant ', constant)
        print('Iterations: \n', iterations)
     else:
        print('the sequence did not converge')
     print('error message reads: ', ier)


     print('STEFFENSONS')

     [xstar, ier, count, iterations] = steffenson(g, x0, tol, Nmax)

     print('the number of iterations was ', count)
     print('the approximate fixed point is: ', xstar)

     if(ier == 0):
        [order, constant] = convergence(p, iterations)
        print('the convergence is of order ', order)
        print('with asymptotic error constant ', constant)
        print('Iterations: \n', iterations)
     else:
        print('the sequence did not converge')
     print('error message reads: ', ier)


     



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


def aitken(p_vector, Nmax, tol):
    
    aitken_iterations = np.zeros((Nmax, 1))

    count = 0

    pn = p_vector[count, 0]
    pn1 = p_vector[count + 1, 0]
    pn2 = p_vector[count + 2, 0]
    pn_hat = pn - (((pn1 - pn) ** 2) / (pn2 - (2 * pn1) + pn))
    aitken_iterations[count, 0] = pn_hat

    while(count < Nmax):
        count += 1
        pn = p_vector[count, 0]
        pn1 = p_vector[count + 1, 0]
        pn2 = p_vector[count + 2, 0]
        pn_hat = pn - (((pn1 - pn) ** 2) / (pn2 - (2 * pn1) + pn))
        aitken_iterations[count, 0] = pn_hat
        if(abs(aitken_iterations[count - 1] - pn_hat) < tol):
            ier = 0
            return [pn_hat, np.trim_zeros(aitken_iterations), ier, count]

    ier = 1
    return [pn_hat, aitken_iterations, ier, count]



def steffenson(f,x0,tol,Nmax):
    count = 0
    iterations = np.zeros((Nmax + 1,1))
    iterations[0,0] = x0

    while(count < Nmax - 2):
        
        a = x0

        count += 1
        b = f(x0)

        iterations[count, 0] = b
        if(abs(a-b) < tol):
            ier = 0
            return[b, ier, count, np.trim_zeros(iterations)]
        
        count += 1
        c = f(b)
        iterations[count, 0] = c

        if(abs(b-c) < tol):
            ier = 0
            return[c, ier, count, np.trim_zeros(iterations)]
        
        count += 1    
        x0 = a - (((b-a) ** 2) / (c - (2 * b) + a))
        iterations[count, 0] = x0

        if(abs(b-c) < tol):
            ier = 0
            return[x0, ier, count, np.trim_zeros(iterations)]
        
    ier = 1
    return[x0, ier, count, np.trim_zeros(iterations)]



driver()