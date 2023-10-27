import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt

def driver():


    f = lambda x: 1 / (1 + (x**2))

    N = 20
    ''' interval'''
    a = -5
    b = 5
    
   
   
    ''' create equispaced interpolation nodes'''
    #xint = np.linspace(a,b,N+1)


    xint = np.zeros(N + 1)
    for j in range(1, N + 2):
        xint[N + 1 - j] = ((a+b) / 2) + (((b-a) / 2) * np.cos((((2*j) - 1)*np.pi) / (2*(N + 1))))

    
    
    ''' create interpolation data'''
    yint = f(xint)
    
    ''' create points for evaluating the Lagrange interpolating polynomial'''
    Neval = 1000
    xeval = np.linspace(a,b,Neval+1)
    yeval_l= np.zeros(Neval+1)



    ''' evaluate lagrange poly '''
    for kk in range(Neval+1):
       yeval_l[kk] = eval_lagrange(xeval[kk],xint,yint,N)
       

    ''' create vector with exact values'''
    fex = f(xeval)
       
    
    plt.figure()    
    plt.plot(xeval,fex,'r-', label='f(x)')
    plt.plot(xeval,yeval_l,'b--', label='Lagrange') 
    plt.title('Lagrange Graph for N={N}'.format(N=N))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()




def eval_lagrange(xeval,xint,yint,N):

    lj = np.ones(N+1)
    
    for count in range(N+1):
       for jj in range(N+1):
           if (jj != count):
              lj[count] = lj[count]*(xeval - xint[jj])/(xint[count]-xint[jj])

    yeval = 0
    
    for jj in range(N+1):
       yeval = yeval + yint[jj]*lj[jj]
  
    return(yeval)


driver()