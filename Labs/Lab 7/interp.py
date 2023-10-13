import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt

def driver():


    f = lambda x: 1 / (1 + (10 * (x**2)))

    N = 10
    ''' interval'''
    a = -1
    b = 1
   
   
    ''' create equispaced interpolation nodes'''
    xint = np.linspace(a,b,N+1)

    #xint = np.zeros(N)

    #for j in range(N):
        #xint[j] = np.cos(((2*(j+1) - 1)*np.pi) / (2*N))
    
    ''' create interpolation data'''
    yint = f(xint)
    
    ''' create points for evaluating the Lagrange interpolating polynomial'''
    Neval = 1000
    xeval = np.linspace(a,b,Neval+1)
    yeval_m = np.zeros(Neval+1)
    yeval_l= np.zeros(Neval+1)
    yeval_dd = np.zeros(Neval+1)

    a = monomialArray(xint,yint, N+1)
  
    '''Initialize and populate the first columns of the 
     divided difference matrix. We will pass the x vector'''
    y = np.zeros( (N+1, N+1) )
     
    for j in range(N+1):
       y[j][0]  = yint[j]

    y = dividedDiffTable(xint, y, N+1)
    ''' evaluate lagrange poly '''
    for kk in range(Neval+1):
       yeval_m[kk] = eval_m(xeval[kk],a,N)
       yeval_l[kk] = eval_lagrange(xeval[kk],xint,yint,N)
       yeval_dd[kk] = evalDDpoly(xeval[kk],xint,y,N)
       

          

    


    ''' create vector with exact values'''
    fex = f(xeval)
       
    
    plt.figure()    
    plt.plot(xeval,fex,'r-', label='f(x)')
    plt.plot(xeval,yeval_m, 'b-', label='monomial')
    plt.plot(xeval,yeval_l,'b-', label='lagrange') 
    plt.plot(xeval,yeval_dd,'b-', label='Newton DD')
    plt.title('Graph for N={N}'.format(N=N))
    plt.legend()

    plt.figure()
    err_m = abs(yeval_m-fex)
    err_l = abs(yeval_l-fex)
    err_dd = abs(yeval_dd-fex)
    plt.semilogy(xeval,err_m,'b--', label='monomial')
    plt.semilogy(xeval,err_l,'b--',label='lagrange')
    plt.semilogy(xeval,err_dd,'b--',label='Newton DD')
    plt.legend()
    plt.title('Error for N={N}'.format(N=N))
    plt.show()
    

def eval_lagrange(xeval,xint,yint,N):

    lj = np.ones(N+1)
    
    for count in range(N+1):
       for jj in range(N+1):
           if (jj != count):
              lj[count] = lj[count]*(xeval - xint[jj])/(xint[count]-xint[jj])

    yeval = 0.
    
    for jj in range(N+1):
       yeval = yeval + yint[jj]*lj[jj]
  
    return(yeval)
  
    

def monomialArray(x,y,n):
   
    A = np.zeros([n,n])

    for i in range(n):
        for j in range(n):
            A[i][j] = x[i] ** j

    Ainv = la.inv(A)

    a = Ainv.dot(y)

    return a

def eval_m(xeval,a,n):

    yeval = 0.

    for jj in range(n+1):
        yeval += a[jj] * (xeval**jj)

    return yeval


    


''' create divided difference matrix'''
def dividedDiffTable(x, y, n):
 
    for i in range(1, n):
        for j in range(n - i):
            y[j][i] = ((y[j][i - 1] - y[j + 1][i - 1]) /
                                     (x[j] - x[i + j]));
    return y;
    
def evalDDpoly(xval, xint,y,N):
    ''' evaluate the polynomial terms'''
    ptmp = np.zeros(N+1)
    
    ptmp[0] = 1.
    for j in range(N):
      ptmp[j+1] = ptmp[j]*(xval-xint[j])
     
    '''evaluate the divided difference polynomial'''
    yeval = 0.
    for j in range(N+1):
       yeval = yeval + y[0][j]*ptmp[j]  

    return yeval

       

driver()        
