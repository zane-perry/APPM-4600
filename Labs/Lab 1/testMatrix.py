import numpy as np
import numpy.linalg as la
import math

def driver():

    m = 2
    n = 2

    A = np.array([[1,2],[3,4]])
    x = np.array([5,6])

    product = matrixByVector(A,x,m,n)

    print('the product is ', product)

    realProduct = np.matmul(A,x)

    print('the real product is supposed to be', realProduct)

    return
    




def matrixByVector(A,x,m,n):

    result = np.zeros(m)
    
    for i in range(m):
        result[i] = dotProduct(A[i],x,n)

    return result





def dotProduct(x,y,n):

    dp = 0.
    for j in range(n):
       dp = dp + x[j]*y[j]

    return dp


driver()