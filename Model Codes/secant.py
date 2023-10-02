# import libraries
import numpy as np
        
def driver():

    f = lambda x: (x**6) - x - 1
    x0 = 2
    x1 = 1
    Nmax = 100
    tol = 1e-13

    (p, p_iterations, error, count) = secant(f,x0,x1,tol, Nmax)
    print('The number of iterations was: ', '%d' % count)
    print('The approximate root is: ', '%16.16e' % p)
    print('The error message reads: ', '%d' % error)




def secant(f,x0,x1,tol,Nmax):
   

    fx0 = f(x0)
    fx1 = f(x1)

    p_iterations = np.zeros(Nmax+1)
    p_iterations[0] = x1



    if(fx0 == 0):
        p = fx0
        error = 0
        return [p,np.trim_zeros(p_iterations),error, 0]
    if(fx1 == 0):
        p = fx1
        error = 0
        return [p,p_iterations, error, 0]
   
    for count in range(Nmax):
        if(fx0 - fx1 == 0):
            error = 1
            p = x1
            return [p, np.trim_zeros(p_iterations),error, count]
      
        x2 = x1 - ((fx1 * (x1 - x0)) / (fx1 - fx0))
        p_iterations[count + 1] = x2
        if(abs(x2 - x1) < tol):
            p = x2
            error = 0
            return [p, np.trim_zeros(p_iterations),error, count]

      
        x0 = x1
        x1 = x2
        fx0 = f(x0)
        fx1 = f(x1)
      

    p = x1
    error = 1
    return [p, p_iterations, error, Nmax]


        
driver()