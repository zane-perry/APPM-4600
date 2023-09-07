import numpy as np
import numpy.linalg as la
import math

def driver():

     n = 3
     z = np.linspace(0,np.pi,n)

# this is a function handle.  You can use it to define 
# functions instead of using a subroutine like you 
# have to in a true low level language.     
     f = lambda z: x**2 + 4*x + 2*np.exp(z)
     g = lambda z: 6*x**3 + 2*np.sin(z)

     #x = f(z)
     #y = g(z)

     x = np.array([0,1,0])
     y = np.array([1,0,1])


# evaluate the dot product of y and w     
     dp = dotProduct(x,y,n)

# print the output
     print('the dot product is : ', dp)


     return
     
def dotProduct(x,y,n):

     dp = 0.
     for j in range(n):
        dp = dp + x[j]*y[j]

     return dp  
     
driver()               
