import numpy as np
from numpy.linalg import norm

def driver():

    x0 = np.array([1,1,1])
    Nmax = 100
    tol = 1e-10

    f = lambda x: (x[0]**2) + (4*(x[1]**2)) + (4*(x[2]**2)) - 16

    [p,error,count, p_iterations] =  iteration(f, x0,tol,Nmax)
    print('The number of iterations was: ', '%d' % count)
    print('The approximate root is: ', p)
    print('The error message reads: ', '%d' % error)
    print('Iterations: ')
    print('Iterations: ')
    for it in range(count + 1):
        print('x value: ', '%16.16e' % p_iterations[it][0], 'y value: ', '%16.16e' % p_iterations[it][1], 'z value: ', '%16.16e' % p_iterations[it][2])

    print(f(p))





def evalD(f, x):
    
    D = np.zeros(3)

    D[0] = (f(x) / (((2*x[0])**2) + ((8*x[1])**2) + ((8*x[2])**2))) * (2*x[0])
    D[1] = (f(x) / (((2*x[0])**2) + ((8*x[1])**2) + ((8*x[2])**2))) * (8*x[1])
    D[2] = (f(x) / (((2*x[0])**2) + ((8*x[1])**2) + ((8*x[2])**2))) * (8*x[2])
    return D




def iteration(f, x0, tol, Nmax):

    p_iterations = np.zeros([Nmax, 3])
    p_iterations[0] = x0

    for count in range(Nmax):
        D = evalD(f,x0)

        x1 = x0 - D
        p_iterations[count + 1] = x1

        if(f(x1) == 0):
            p = x1
            error = 0
            return[p, error, count + 1, p_iterations]
        
        x0 = x1
    
    p = x1
    count = 1
    return[p,error,Nmax, p_iterations]


driver()